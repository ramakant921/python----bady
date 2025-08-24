import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Listening...")
        recognizer.adjust_for_ambient_noise(source)  # reduce background noise
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)  # using Google Web Speech API
        print(f"✅ You said: {text}")
    except sr.UnknownValueError:
        print("❌ Sorry, I could not understand.")
    except sr.RequestError:
        print("⚠️ Could not request results, check your internet connection.")

if __name__ == "__main__":
    recognize_speech()
