import google.generativeai as genai
import speech_recognition as sr
from gtts import gTTS
import os
import platform

# ---------------- SETUP ---------------- #
API_KEY = "AIzaSyA0akqs0z7bwK4-qjp4NJEhaI_FXkK8Q6o"  # replace with your key
genai.configure(api_key=API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")
chat = model.start_chat()

recognizer = sr.Recognizer()

# ---------------- SPEAK FUNCTION ---------------- #
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "response.mp3"
    tts.save(filename)

    system = platform.system()
    if system == "Windows":
        os.system(f"start {filename}")
    elif system == "Darwin":  # macOS
        os.system(f"open {filename}")
    else:  # Linux
        os.system(f"xdg-open {filename}")

# ---------------- MAIN LOOP ---------------- #
print("🎤 Talk with Gemini! Say 'exit' to quit.")

while True:
    try:
        with sr.Microphone() as source:
            print("Listening...")
            audio = recognizer.listen(source)

        user_input = recognizer.recognize_google(audio)
        print("You:", user_input)

        if user_input.lower() == "exit":
            speak("Goodbye spodormon!")
            break

        response = chat.send_message(user_input)
        print("Gemini:", response.text)
        speak(response.text)

    except sr.UnknownValueError:
        print("❌ Could not understand audio.")
    except sr.RequestError as e:
        print("⚠️ Speech recognition error:", e)
    except Exception as e:
        print("⚠️ Error:", e)
