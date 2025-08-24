import speech_recognition as sr
import multiprocessing
import threading
import itertools
import sys
import time
import webbrowser
import datetime
from termcolor import colored

# ==============================
# Utilities
# ==============================
def wish_me():
    """Greet the user depending on time of day."""
    hour = datetime.datetime.now().hour
    if hour < 12:
        greeting = "Good morning"
    elif 12 <= hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

    print(colored(f"[Jarvis] >>> {greeting}, sir!", "cyan", attrs=['bold']))

def listening_animated_text(event):
    """Show animated listening text while waiting for commands."""
    for c in itertools.cycle(['.', '..', '...']):
        if not event.is_set():
            break
        sys.stdout.write(f"\r[Jarvis] >>> Listening{c}   ")
        sys.stdout.flush()
        time.sleep(0.5)
    sys.stdout.write("\r")
    sys.stdout.flush()

# ==============================
# Listener (Speech Recognition)
# ==============================
def recognize_speech(queue):
    """Continuously recognize speech and send results to the queue."""
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        recognizer.adjust_for_ambient_noise(source)

    while True:
        try:
            with mic as source:
                audio = recognizer.listen(source)
            query = recognizer.recognize_google(audio)
            queue.put(query)
        except sr.UnknownValueError:
            queue.put("could not understand the audio")
        except Exception as e:
            queue.put(f"error: {str(e)}")
        time.sleep(0.1)

# ==============================
# Command Handler
# ==============================
def handle_command(query: str):
    """Handle user commands."""
    if "time" in query:
        now = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"[Jarvis] >>> The time is {now}")

    elif "open youtube" in query:
        webbrowser.open("https://youtube.com")
        print("[Jarvis] >>> Opening YouTube")
        
    elif "open spotify" in query:
        webbrowser.open("https://spotify.com")
        print("[Jarvis] >>> Opening Spotify")

    elif "open google" in query:
        webbrowser.open("https://google.com")
        print("[Jarvis] >>> Opening Google")

    elif "shutdown" in query:
        print("[Jarvis] >>> Shutting down the system (disabled for safety)")
        # Uncomment if you want real shutdown:
        # import os; os.system("shutdown /s /t 1")

    else:
        print("[Jarvis] >>> Sorry, I don’t know how to do that yet.")

# ==============================
# Main Program
# ==============================
def main():
    """Main function to run the voice assistant."""
    queue = multiprocessing.Queue()
    animation_thread_event = threading.Event()

    speech_process = multiprocessing.Process(target=recognize_speech, args=(queue,))
    speech_process.start()

    animation_thread_started = False

    print("Main process is running...\n")
    wish_me()

    try:
        while True:
            if not queue.empty():
                query = queue.get().lower()
                if query == "listening":
                    if not animation_thread_started:
                        animation_thread = threading.Thread(
                            target=listening_animated_text,
                            args=(animation_thread_event,)
                        )
                        animation_thread.daemon = True
                        animation_thread.start()
                        animation_thread_started = True
                        animation_thread_event.set()
                else:
                    animation_thread_event.clear()
                    if "could not understand the audio" in query:
                        sys.stdout.write("\033[K")
                        sys.stdout.flush()
                    else:
                        sys.stdout.write("\033[F")
                        sys.stdout.write("\033[K")
                        sys.stdout.flush()
                        print(f"\n{colored('[You] >>>', 'magenta', attrs=['bold'])} {query}\n")
                        handle_command(query)

    except KeyboardInterrupt:
        print("Stopping assistant...")
        speech_process.terminate()
        speech_process.join()

if __name__ == "__main__":
    main()
