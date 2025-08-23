from core.listener import recognize_speech
from core.command_handler import handle_command
from core.utilities import wish_me, listening_animated_text
import multiprocessing
import threading
from termcolor import colored
import sys

def main():
    """Main function to run the voice assistant."""
    # Create a queue for inter-process communication
    queue = multiprocessing.Queue()

    animation_thread_event = threading.Event()

    # Start the speech recognition process
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
                        animation_thread = threading.Thread(target=listening_animated_text, args=(animation_thread_event,))
                        animation_thread.daemon = True  # Ensure it ends when the main program ends
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
                        print(f"\n{colored("[You] >>>", "magenta", attrs=['bold'])} {query}\n")
                        handle_command(query)

    except KeyboardInterrupt:
        print("Stopping assistant...")
        speech_process.terminate()
        speech_process.join()

if __name__ == "__main__":
    main()