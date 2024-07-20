import speech_recognition as sr
import webbrowser
import pyttsx3  #for voice assisstance
import music_lib
from gtts import gTTS
import pygame
import os
recognizer=sr.Recognizer()
engine=pyttsx3.init()
def speak_old(text):
    engine.say(text)
    engine.runAndWait()
def speak(text):
    #to change the voice
    tts=gTTS(text)
    tts.save("temp.mp3")
    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")
def process_command(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song=c.lower().split(" ")[1]
        link=music_lib.music[song]
        webbrowser.open(link)
if __name__=="__main__":
    speak("Initializing Jarvis....")
    while True:
        #listen for the wake word "Jarvis"
        #to obtain audio from microphone 
        r=sr.Recognizer()
        print("recognizing....")
        try:
            with sr.Microphone() as source:
                print("listening...")
                audio=r.listen(source, timeout=2,phrase_time_limit=1)
            command= r.recognize_google(audio)
            if (command.lower()=="jarvis"):
                speak("ya how may I help you!")
                #listen for word!
                with sr.Microphone() as source:
                    print("jarvis active...")
                    audio=r.listen(source)
                    command=r.recognize_google(audio)
                    process_command(command)
        except Exception as e:
            print("error; {0}".format(e))

#finished!!!



