#!/usr/bin/env python3
# Jarvis assistant with text + speech, greeting, and name recall.

import os, re, sys, math, json, random, platform, webbrowser, pyttsx3
from datetime import datetime
from urllib.parse import quote_plus

try:
    import wikipedia
except:
    wikipedia = None

try:
    import requests
except:
    requests = None


# ----------------- Config / User -----------------
CONFIG_FILE = "Somwar_config.json"
DEFAULT_NAME = "Niggga"


def load_name():
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, "r") as f:
                return json.load(f).get("name", DEFAULT_NAME)
        except:
            return DEFAULT_NAME
    return DEFAULT_NAME


def save_name(name):
    with open(CONFIG_FILE, "w") as f:
        json.dump({"name": name}, f)


USER_NAME = load_name()


# ----------------- Voice Engine -----------------
engine = pyttsx3.init()
engine.setProperty("rate", 170)
engine.setProperty("volume", 1.0)
voices = engine.getProperty("voices")
if voices:
    engine.setProperty("voice", voices[0].id)          


def speak(text: str):
    print(f"Jarvis > {text}")
    engine.say(text)
    engine.runAndWait()


# ----------------- Helper functions -----------------
def safe_calc(expr):
    allowed = {k: getattr(math, k) for k in dir(math) if not k.startswith("_")}
    allowed.update({"abs": abs, "round": round})
    code = compile(expr, "<calc>", "eval")
    for name in code.co_names:
        if name not in allowed:
            raise ValueError(f"Illegal: {name}")
    return eval(code, {"__builtins__": {}}, allowed)


def web_search(query):
    url = f"https://duckduckgo.com/?q={quote_plus(query)}"
    webbrowser.open(url, new=1)


def open_site(site):
    if not re.match(r"^https?://", site):
        site = "https://" + site
    webbrowser.open(site, new=1)


def wiki_summary(topic):
    if not wikipedia:
        return "Wikipedia not installed. Run: pip install wikipedia"
    try:
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        return f"Wikipedia error: {e}"


def ddg_answer(query):
    if not requests:
        return "Requests not installed. Run: pip install requests"
    try:
        url = f"https://api.duckduckgo.com/?q={quote_plus(query)}&format=json&no_html=1&skip_disambig=1"
        r = requests.get(url, timeout=6)
        data = r.json()
        if data.get("AbstractText"):
            return data["AbstractText"]
        for item in (data.get("RelatedTopics") or []):
            if isinstance(item, dict) and item.get("Text"):
                return item["Text"]
        return "I couldn't find an instant answer. Try 'search <query>'."
    except Exception as e:
        return f"Search error: {e}"


def system_info():
    return (
        f"OS: {platform.system()} {platform.release()}\n"
        f"Machine: {platform.machine()}\n"
        f"Python: {platform.python_version()}\n"
        f"Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    )


# ----------------- Open Applications -----------------
def open_app(app_name):
    """Open common applications on Windows PC by name."""
    app_name = app_name.lower()

    apps = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
        "vs code": r"C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\Code.exe",
        "whatsapp": r"C:\Users\YourName\AppData\Local\WhatsApp\WhatsApp.exe",
        "file explorer": "explorer.exe",
        "vlc": r"C:\Program Files\VideoLAN\VLC\vlc.exe",
        "spotify": r"C:\Users\YourName\AppData\Roaming\Spotify\Spotify.exe"
    }

    if app_name in apps:
        try:
            os.startfile(apps[app_name])
            return f"Opening {app_name}."
        except Exception as e:
            return f"Error opening {app_name}: {e}"
    else:
        return f"App '{app_name}' not found in list."


# ----------------- Greeting -----------------
def opening_line(name: str) -> str:
    hour = datetime.now().hour
    if 5 <= hour < 12:
        return f"Good morning, {name}. Jarvis online and ready."
    elif 12 <= hour < 17:
        return f"Good afternoon, {name}. How may I assist you?"
    elif 17 <= hour < 22:
        return f"Good evening, {name}. I'm at your service."
    else:
        return f"Hello, {name}. It's late, but Jarvis is awake for you."


# ----------------- Command Handler -----------------
HELP_TEXT = """Commands:
  help               - show this help
  name <your name>   - set your name
  time / date        - show current time/date
  system             - system info
  calc <expr>        - calculate
  search <query>     - web search
  open <site>        - open website
  open app <name>    - open application
  wiki <topic>       - Wikipedia summary
  ask <question>     - quick web-based answer
  jarvis             - call Jarvis
  exit               - quit
"""

def handle(cmd_raw: str, user_name: str) -> str:
    cmd = cmd_raw.strip()
    if not cmd:
        return ""

    lcmd = cmd.lower()

    if lcmd in ("exit", "quit", "bye"):
        return "Goodbye, master."

    if lcmd == "help":
        return HELP_TEXT

    if lcmd.startswith("name "):
        new_name = cmd[5:].strip().title()
        if new_name:
            save_name(new_name)
            return f"Nice to meet you, {new_name}. I will remember that."
        return "Please provide a name."

    if lcmd == "Jarvis" or lcmd.startswith("hey Jarvis"):
        return f"At your service, {user_name}."

    if lcmd == "time":
        return datetime.now().strftime("Current time: %H:%M:%S")

    if lcmd == "date":
        return datetime.now().strftime("Today: %Y-%m-%d")

    if lcmd == "system":
        return system_info()

    m = re.match(r"^calc\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        try:
            return f"= {safe_calc(m.group(1))}"
        except Exception as e:
            return f"Calc error: {e}"

    m = re.match(r"^search\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        q = m.group(1)
        web_search(q)
        return f"Searching: {q}"

    m = re.match(r"^open\s+app\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        app = m.group(1)
        return open_app(app)

    m = re.match(r"^open\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        site = m.group(1)
        open_site(site)
        return f"Opening site: {site}"

    m = re.match(r"^wiki\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        return wiki_summary(m.group(1))

    m = re.match(r"^ask\s+(.+)$", cmd, re.IGNORECASE)
    if m:
        return ddg_answer(m.group(1))

    return ddg_answer(cmd)


# ----------------- Main -----------------
def main():
    user_name = load_name()
    greet = opening_line(user_name)
    speak(greet)

    while True:
        try:
            user_input = input("\nYou > ").strip()
        except (EOFError, KeyboardInterrupt):
            speak("Shutting down. Goodbye.")
            break

        if not user_input:
            continue

        reply = handle(user_input, load_name())
        if reply:
            speak(reply)
            if user_input.lower() in ("exit", "quit", "bye"):
                break


if __name__ == "__main__":
    main()
