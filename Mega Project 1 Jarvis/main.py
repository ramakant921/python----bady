import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
from gtts import gTTS
from openai import OpenAI
import pygame
import os

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = ""


def speak_old(text):
    engine.say(text)
    engine.runAndWait()
    
def speak(text):
    tts = gTTS(text)
    tts.save("temp.mp3")
    
    # Initialize Pygame mixer
    pygame.mixer.init()

    # Load the MP3 file
    pygame.mixer.music.load('temp.mp3')

    # Play the MP3 file
    pygame.mixer.music.play()

    # Keep the program running until the music stops playing
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3") 
    
def aiProcess(command):
    client = OpenAI(api_key="",
    )
    
    completion = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a virtual assistant named jarvis skilled in general tasks like Alexa and Google Cloud. Give short responses please"},
        {"role": "user", "content": command}
    ]
    )
    
    return completion.choices[0].message.content
    
def processCommand(c):
    if c.lower() =="open google" in c.lower():
        webbrowser.open("https://google.com")
    elif c.lower() =="open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif c.lower() =="open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower() =="open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startwith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        webbrowser.open(link)
        
    elif "news" in c.lower():
        r = requests.get("")
        if r.status_code == 200:
        #   Parse the JSON response
            data = r.json()
            
            # Extract the articles
            articles = data.get('articles',[])
            
            # Print the headlines
            for article in articles:
                speak_old(article['title'])  
        
    else:
        # let openAI handle request
        output = aiProcess(c)
        speak_old(output)


if __name__ == "__main__":
    speak_old("Initialiazing Jarvis.........")
    
    while True:
        # Listen wake word from "Jarvis"
        # Obtain audio from the microphone
        r = sr.Recognizer()
        
        
        
    # Recognize speech using Sphinx
        print("recoginitizing...")
        try:
            with sr.Microphone() as source:       
                print("Listening.....")
                audio = r.listen(source, timeout = 2, phrase_time_limit = 1)
            word = r.recognize_google(audio)
            if(word.lower() == 'jarvis'):
                speak_old("Ya")
                with sr.Microphone() as source:
                    print("Jarvis active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)
                                 
        except Exception as e:
            print("Error; {0}" .format(e))