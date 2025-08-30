import speech_recognition as sr
import webbrowser
import requests
from openai import OpenAI
from gtts import gTTS
import os
import platform

# pip install speechrecognition gTTS openai requests

recognizer = sr.Recognizer()
newsapi = "<Your Key Here>"  # Add your NewsAPI key

# ---------------- SPEAK FUNCTION ---------------- #
def speak(text, lang="en"):
    tts = gTTS(text=text, lang=lang)
    filename = "temp.mp3"
    tts.save(filename)

    system = platform.system()
    if system == "Windows":
        os.system(f"start {filename}")
    elif system == "Darwin":  # macOS
        os.system(f"open {filename}")
    else:  # Linux
        os.system(f"xdg-open {filename}")

# ---------------- OPENAI FUNCTION ---------------- #
def aiProcess(command):
    client = OpenAI(api_key="<Your Key Here>")

    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a virtual assistant named Jarvis skilled in general tasks like Alexa and Google Cloud. Keep responses short."},
            {"role": "user", "content": command}
        ]
    )

    return completion.choices[0].message.content

# ---------------- COMMAND HANDLER ---------------- #
def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])
            for article in articles[:5]:  # Read only top 5 headlines
                speak(article['title'])
        else:
            speak("Sorry, I couldn't fetch the news right now.")

    else:
        output = aiProcess(c)
        speak(output)

# ---------------- MAIN PROGRAM ---------------- #
if __name__ == "__main__":
    speak("Initializing Jarvis....")
    while True:
        r = sr.Recognizer()
        print("recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)

            if word.lower() == "jarvis":
                speak("Yes?")
                with sr.Microphone() as source:
                    print("Jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)

        except Exception as e:
            print(f"Error: {e}")
