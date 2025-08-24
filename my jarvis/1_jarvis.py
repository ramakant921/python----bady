#!/usr/bin/env python3
# jarvis_text_assistant.py
# Text-only “Jarvis”-style assistant. No audio dependencies.

import os
import re
import sys
import json
import math
import time
import shutil
import ctypes
import platform
import subprocess
import webbrowser
from datetime import datetime
from urllib.parse import quote_plus

# Optional deps (install: pip install wikipedia requests)
try:
    import wikipedia
except Exception:
    wikipedia = None

try:
    import requests
except Exception:
    requests = None


# ---------- Utilities ----------

def is_windows():
    return os.name == "nt"

def is_macos():
    return sys.platform == "darwin"

def is_linux():
    return sys.platform.startswith("linux")

def println(msg=""):
    print(msg, flush=True)

def safe_eval_expr(expr: str):
    """
    Safely evaluate simple math expressions.
    Supports +, -, *, /, **, %, //, parentheses, and math module functions.
    """
    allowed_names = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed_names.update({"abs": abs, "round": round})
    code = compile(expr, "<calc>", "eval")
    for name in code.co_names:
        if name not in allowed_names:
            raise ValueError(f"Illegal name in expression: {name}")
    return eval(code, {"__builtins__": {}}, allowed_names)


# ---------- Browser Control ----------

def register_known_browsers():
    """
    Register common browsers with webbrowser, so users can call them by name.
    We attempt multiple typical install paths per OS. Missing ones are skipped.
    """
    # Helper: try to register if executable exists
    def try_register(name, path, args=None):
        if path and shutil.which(path) is None and not os.path.isfile(path):
            return
        try:
            if args:
                controller = webbrowser.BackgroundBrowser(f'"{path}" {args}')
            else:
                controller = webbrowser.BackgroundBrowser(f'"{path}"')
            webbrowser.register(name, None, controller, preferred=False)
        except Exception:
            pass

    if is_windows():
        paths = {
            "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
            "chrome_x86": r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
            "edge": r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
            "edge_alt": r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
            "firefox": r"C:\Program Files\Mozilla Firefox\firefox.exe",
            "firefox_x86": r"C:\Program Files (x86)\Mozilla Firefox\firefox.exe",
            "brave": r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe",
            "brave_x86": r"C:\Program Files (x86)\BraveSoftware\Brave-Browser\Application\brave.exe",
            "opera": r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera\launcher.exe",
            "opera_gx": r"C:\Users\%USERNAME%\AppData\Local\Programs\Opera GX\launcher.exe",
            "vivaldi": r"C:\Users\%USERNAME%\AppData\Local\Vivaldi\Application\vivaldi.exe",
        }
        for key, p in paths.items():
            p = os.path.expandvars(p)
            browser_name = key.replace("_x86", "")
            try_register(browser_name, p)

        # Also register default "windows-default"
        try:
            webbrowser.register("windows-default", None, webbrowser.get())
        except Exception:
            pass

    elif is_macos():
        # macOS can open by bundle id via "open -a"
        # Register common names mapping to 'open -a BrowserName'
        common = {
            "safari": "/Applications/Safari.app/Contents/MacOS/Safari",
            "chrome": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "firefox": "/Applications/Firefox.app/Contents/MacOS/firefox",
            "brave": "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
            "edge": "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
            "opera": "/Applications/Opera.app/Contents/MacOS/Opera",
            "vivaldi": "/Applications/Vivaldi.app/Contents/MacOS/Vivaldi",
        }
        for name, path in common.items():
            try_register(name, path)

    elif is_linux():
        # Linux: rely on PATH or common flatpak/snap names
        for name in ["xdg-open", "google-chrome", "google-chrome-stable", "chromium", "brave-browser", "firefox", "microsoft-edge", "opera", "vivaldi"]:
            if shutil.which(name):
                try_register(name.split("-")[0], name)


def open_with_browser_name(browser_name: str, url: str = "about:blank") -> bool:
    """
    Try to open URL with a specific browser name previously registered,
    else fallback to default webbrowser.
    Returns True if launched.
    """
    browser_name = browser_name.lower().strip()
    candidates = [browser_name]

    # Some friendly aliases
    alias = {
        "google": "chrome",
        "google chrome": "chrome",
        "edge": "edge",
        "msedge": "edge",
        "firefox": "firefox",
        "mozilla": "firefox",
        "brave": "brave",
        "opera gx": "opera",
        "default": None,  # means fallback
    }
    if browser_name in alias:
        canonical = alias[browser_name]
        if canonical:
            candidates = [canonical]
        else:
            candidates = []

    # Try direct
    for name in candidates:
        try:
            controller = webbrowser.get(name)
            controller.open(url, new=1)
            return True
        except Exception:
            pass

    # Fallback to default
    try:
        webbrowser.open(url, new=1)
        return True
    except Exception:
        return False


# ---------- Knowledge (Search / Wikipedia) ----------

def ddg_instant_answer(query: str) -> str:
    """
    Use DuckDuckGo Instant Answer API for lightweight Q&A and summaries.
    (No API key required.)
    """
    if not requests:
        return "Install 'requests' to enable web answers (pip install requests)."

    try:
        url = f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&no_html=1&skip_disambig=1"
        r = requests.get(url, timeout=8)
        r.raise_for_status()
        data = r.json()
        abstract = data.get("Abstract")
        if abstract:
            return abstract.strip()

        # Fallback to first related topic
        related = data.get("RelatedTopics") or []
        for item in related:
            if isinstance(item, dict) and item.get("Text"):
                return item["Text"].strip()
        return "I couldn't find a direct answer. Try 'search <your query>' to open results."
    except Exception as e:
        return f"Web lookup failed: {e}"


def wiki_summary(topic: str, sentences: int = 3) -> str:
    if not wikipedia:
        return "Install 'wikipedia' to enable Wikipedia answers (pip install wikipedia)."
    try:
        wikipedia.set_lang("en")
        return wikipedia.summary(topic, sentences=sentences)
    except wikipedia.DisambiguationError as e:
        # Show a few options
        opts = ", ".join(e.options[:8])
        return f"That topic is ambiguous. Did you mean: {opts} ..."
    except Exception as e:
        return f"Wikipedia lookup failed: {e}"


# ---------- System helpers ----------

def show_system_info() -> str:
    parts = []
    parts.append(f"OS: {platform.system()} {platform.release()} ({platform.version()})")
    parts.append(f"Machine: {platform.machine()}")
    parts.append(f"Python: {platform.python_version()}")
    parts.append(f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    if is_windows():
        try:
            # Check admin
            is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
            parts.append(f"Admin: {is_admin}")
        except Exception:
            pass
    return "\n".join(parts)


def open_site(url: str) -> bool:
    # Prepend scheme if missing
    if not re.match(r"^[a-zA-Z]+://", url):
        url = "https://" + url
    try:
        webbrowser.open(url, new=1)
        return True
    except Exception:
        return False


def perform_web_search(query: str, browser_hint: str | None = None) -> bool:
    url = f"https://duckduckgo.com/?q={quote_plus(query)}"
    if browser_hint:
        return open_with_browser_name(browser_hint, url)
    return open_site(url)


# ---------- Command Router ----------

HELP_TEXT = """
Commands you can use:
  help                                Show this help
  exit / quit                         Exit the assistant
  time                                Show current time
  date                                Show current date
  system                              Show basic system info
  calc <expression>                   Calculate (e.g., calc (3+5)*2 or calc sqrt(16)+cos(0))
  search <query>                      Open web search results in your browser
  open <site or URL>                  Open a website in your default browser (e.g., open youtube.com)
  open browser <name> [url]           Open a specific browser (chrome, brave, edge, firefox, opera...) optionally at a URL
  wiki <topic>                        Summarize from Wikipedia
  ask <question>                      Quick web-based answer (DuckDuckGo Instant Answer)

Examples:
  open browser chrome
  open browser brave https://chat.openai.com
  search python pathlib write file
  wiki Albert Einstein
  calc sin(pi/2) + log(10, 10)
"""

def handle_command(cmd: str) -> str:
    cmd = cmd.strip()
    if not cmd:
        return ""

    # Exit
    if cmd.lower() in {"exit", "quit", "q"}:
        raise SystemExit

    # Help
    if cmd.lower() in {"help", "h", "?"}:
        return HELP_TEXT

    # Time / Date
    if cmd.lower() == "time":
        return datetime.now().strftime("Current time: %H:%M:%S")
    if cmd.lower() == "date":
        return datetime.now().strftime("Today's date: %Y-%m-%d")

    # System info
    if cmd.lower() == "system":
        return show_system_info()

    # calc
    m = re.match(r"^calc\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        expr = m.group(1).strip()
        try:
            val = safe_eval_expr(expr)
            return f"= {val}"
        except Exception as e:
            return f"Calculation error: {e}"

    # open browser <name> [url]
    m = re.match(r"^open\s+browser\s+([a-zA-Z0-9 _-]+)(?:\s+(.*))?$", cmd, re.IGNORECASE)
    if m:
        name = m.group(1).strip()
        url = (m.group(2) or "about:blank").strip()
        ok = open_with_browser_name(name, url)
        return f"Launching {name} -> {url}" if ok else f"Couldn't launch {name}. Try installing or use 'open <url>'."

    # open <site>
    m = re.match(r"^open\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        site = m.group(1).strip()
        ok = open_site(site)
        return f"Opening {site}" if ok else f"Couldn't open {site}"

    # search <query>
    m = re.match(r"^search\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        q = m.group(1).strip()
        ok = perform_web_search(q)
        return f"Searching the web for: {q}" if ok else "Couldn't launch the web browser."

    # wiki <topic>
    m = re.match(r"^wiki\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        topic = m.group(1).strip()
        return wiki_summary(topic, sentences=3)

    # ask <question> (DuckDuckGo IA)
    m = re.match(r"^ask\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        q = m.group(1).strip()
        return ddg_instant_answer(q)

    # Fallback: treat as a general question via instant answer
    return ddg_instant_answer(cmd)


# ---------- Main Loop ----------

def main():
    register_known_browsers()

    banner = (
        "Jarvis (text-only) ready. Type 'help' for commands. Type 'exit' to quit."
    )
    println(banner)

    # REPL
    while True:
        try:
            line = input("\nYou > ").strip()
        except (EOFError, KeyboardInterrupt):
            println("\nExiting. Goodbye!")
            break

        if not line:
            continue

        try:
            response = handle_command(line)
            if response:
                println(f"Jarvis > {response}")
        except SystemExit:
            println("Exiting. Goodbye!")
            break
        except Exception as e:
            println(f"Jarvis > Error: {e}")

if __name__ == "__main__":
    main()
