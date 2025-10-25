import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from openai import OpenAI
from gtts import gTTs
import pygame
import os

# pip install pocketsphinx


recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "0c50feaaf730430ea90d750160c36c40"


def speak_old(text):
    engine.say(text)
    engine.runAndWait()

def speak(text):
    tts = gTTs(text)
    tts.save("temp.mp3")  

    pygame.mixer.init()

    pygame.mixer.music.load("temp.mp3")

    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.clock().tick(10)

    pygame.mixer.music.unload()
    os.remove("temp.mp3")
    


def aiProcess(command):
    client = OpenAI(
    api_key="AIzaSyBahAJw0LZ9lD7IVjVcqvf6z8QeH9PGJ34")

    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual    assistant named jarvis skilled in general tasks like   Alexa and Google Cloud. Give short responses please."},
        {"role": "user", "content": command}
    ]
    )

    return completion.choices[0].message.content    

def processCommand(c):  
    if "open firefox" in c.lower():
        webbrowser.open("https://www.firefox.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://www.whatsapp.com")   
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")   
    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/")   
    elif "open linkedin" in c.lower():
        webbrowser.open("https://open.linkedin.com/")   
    elif "open my app" in c.lower():
        webbrowser.open("https://backup-mindless-website.onrender.com/") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get('articles',[])

            for article in articles:
                speak(article['title'])

    else:
         output = aiProcess(c)
         speak(output)



if __name__=="__main__":
    speak("Initializing Jarvis........")
    while True:
        r=sr.Recognizer()
        

        print("Recognizing....")
        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=2,phrase_time_limit=1)
            word=r.recognize_google(audio)
            if(word.lower()=="jarvis"):
                speak("Ya")
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command=r.recognize_google(audio)

                    processCommand(command)



        except Exception as e:
            print("Error; {0}".formet(e))