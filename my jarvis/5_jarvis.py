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

import vlc
import yt_dlp


# ----------------- Config -----------------
DATA_FILE = "jarvis_data.json"
DEFAULT_NAME = "User"
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
  play online <song> - play online song (YouTube/search/direct MP3)
  stop song          - stop current music
  jarvis             - call Jarvis
  exit               - quit
"""

# ----------------- Storage -----------------
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r") as f:
                return json.load(f)
        except:
            return {}
    return {}

def save_data(data):
    try:
        with open(DATA_FILE, "w") as f:
            json.dump(data, f)
    except:
        pass

data = load_data()
if "name" not in data:
    data["name"] = DEFAULT_NAME

# ----------------- Speech -----------------
engine = pyttsx3.init()
def speak(text):
    print("Jarvis:", text)
    try:
        engine.say(text)
        engine.runAndWait()
    except:
        pass

# ----------------- Greeting -----------------
def greet():
    h = datetime.now().hour
    if h < 12:
        return "Good morning"
    elif h < 18:
        return "Good afternoon"
    else:
        return "Good evening"

# ----------------- System Info -----------------
def system_info():
    return f"{platform.system()} {platform.release()} ({platform.version()})"

# ----------------- Web Search -----------------
def search_web(query):
    url = f"https://www.google.com/search?q={quote_plus(query)}"
    webbrowser.open(url)
    return f"Searching the web for {query}..."

# ----------------- Apps -----------------
APPS = {
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": r"C:\Users\Acer\AppData\Local\Programs\Microsoft VS Code\Code.exe",
    "whatsapp": r"C:\Users\Acer\AppData\Local\WhatsApp\WhatsApp.exe",
    "explorer": r"C:\Windows\explorer.exe",
}
def open_app(name):
    path = APPS.get(name.lower())
    if path and os.path.exists(path):
        os.startfile(path)
        return f"Opening {name}..."
    return f"App {name} not found."

# ----------------- Wikipedia -----------------
def wiki_summary(topic):
    if not wikipedia:
        return "Wikipedia module not installed."
    try:
        return wikipedia.summary(topic, sentences=2)
    except Exception as e:
        return f"Error: {e}"

# ----------------- Ask (DuckDuckGo API) -----------------
def ddg_answer(query):
    try:
        resp = requests.get(
            "https://api.duckduckgo.com/",
            params={"q": query, "format": "json"},
            timeout=5,
        )
        data = resp.json()
        if data.get("AbstractText"):
            return data["AbstractText"]
        elif data.get("Answer"):
            return data["Answer"]
        return "No instant answer available."
    except:
        return "Error fetching answer."

# ----------------- Music Player -----------------
vlc_player = None  # global player instance

def _resolve_audio_stream(query_or_url: str):
    """
    Returns (direct_stream_url, title) for YouTube/search/direct MP3.
    """
    ydl_opts = {
        "format": "bestaudio/best",
        "noplaylist": True,
        "quiet": True,
        "skip_download": True,
        "default_search": "ytsearch",
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(query_or_url, download=False)

        # Handle search result list
        if isinstance(info, dict) and "entries" in info and info["entries"]:
            info = next((e for e in info["entries"] if e), None)
            if not info:
                raise ValueError("No results found.")

        # Direct stream
        if "url" in info and info.get("protocol"):
            return info["url"], info.get("title")

        # Build from video page
        video_page = (
            info.get("webpage_url")
            or info.get("original_url")
            or (f"https://www.youtube.com/watch?v={info['id']}" if "id" in info else None)
        )
        if not video_page:
            return query_or_url, info.get("title")

        info2 = ydl.extract_info(video_page, download=False)
        if "url" not in info2:
            raise ValueError("Could not resolve a stream URL.")
        return info2["url"], info2.get("title")

def play_online_song(query_or_url: str):
    """Play an online song from YouTube/search text or a direct audio URL."""
    global vlc_player
    try:
        stream_url, title = _resolve_audio_stream(query_or_url)
        if vlc_player:
            vlc_player.stop()
        vlc_player = vlc.MediaPlayer(stream_url)
        vlc_player.play()
        speak(f"Streaming online: {title or query_or_url}")
        return "Streaming online song."
    except Exception as e:
        return f"Error playing online song: {e}"

def stop_song():
    global vlc_player
    if vlc_player:
        vlc_player.stop()
        return "Stopped the music."
    return "No song is playing."

# ----------------- Command Handler -----------------
def handle(cmd):
    lcmd = cmd.lower()

    if lcmd in ["help", "?"]:
        return HELP_TEXT
    if lcmd in ["exit", "quit", "bye"]:
        sys.exit(0)
    if lcmd in ["jarvis"]:
        return "Yes, I am here."

    if lcmd in ["time"]:
        return datetime.now().strftime("%H:%M:%S")
    if lcmd in ["date"]:
        return datetime.now().strftime("%Y-%m-%d")

    if lcmd in ["system"]:
        return system_info()

    m = re.match(r"name\s+(.+)", cmd, re.I)
    if m:
        data["name"] = m.group(1)
        save_data(data)
        return f"Nice to meet you, {data['name']}."

    m = re.match(r"calc\s+(.+)", cmd, re.I)
    if m:
        try:
            return str(eval(m.group(1), {"__builtins__": None}, math.__dict__))
        except Exception as e:
            return f"Error: {e}"

    m = re.match(r"search\s+(.+)", cmd, re.I)
    if m:
        return search_web(m.group(1))

    m = re.match(r"open\s+(\w+)$", cmd, re.I)
    if m:
        return open_app(m.group(1))

    m = re.match(r"wiki\s+(.+)", cmd, re.I)
    if m:
        return wiki_summary(m.group(1))

    m = re.match(r"ask\s+(.+)", cmd, re.I)
    if m:
        return ddg_answer(m.group(1))

    m = re.match(r"play\s+online\s+(.+)", cmd, re.I)
    if m:
        return play_online_song(m.group(1))

    if lcmd == "stop song":
        return stop_song()

    return ddg_answer(cmd)

# ----------------- Main Loop -----------------
if __name__ == "__main__":
    speak(f"{greet()}, {data['name']}. How can I help you?")
    while True:
        try:
            cmd = input(f"{data['name']}> ")
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not cmd.strip():
            continue
        response = handle(cmd.strip())
        if response:
            speak(response)
