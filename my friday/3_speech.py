import speech_recognition as sr
import sounddevice as sd
import wavio

def recognize_speech(duration=5, fs=44100):
    print("🎤 Speak now... (recording)")
    # Record audio from microphone
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished

    # Save recording to a WAV file
    wavio.write("temp.wav", recording, fs, sampwidth=2)

    # Recognize speech from the WAV file
    recognizer = sr.Recognizer()
    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio)
        print(f"✅ You said: {text}")
    except sr.UnknownValueError:
        print("❌ Could not understand audio")
    except sr.RequestError:
        print("⚠️ Could not connect to Google API")

if __name__ == "__main__":
    recognize_speech()
