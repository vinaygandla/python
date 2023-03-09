import speech_recognition as sr
import pyttsx3 as pt
import datetime
from time import sleep
import os
import wikipedia
from bs4 import BeautifulSoup
import requests
import instaloader
import pyautogui as gui
import pyscreeze
from wikipedia import exceptions
from wikipedia.wikipedia import search
import pyaudio
import keyboard
import webbrowser
import pyjokes
listener=sr.Recognizer()
engine=pt.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)
engine.setProperty('rate',145)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    os.system('cls')
    if hour>0 and hour<12:
        print("good morning!")
        speak("good morning!")
    elif hour>=12 and hour<18:
        print("good afternoon!")
        speak("good afternoon!")
    else:
        print("good evening!")
        speak("good evening")
def takecommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recognizing")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")
    except Exception as e:
        print("say that again please....")
        return "None"
    return query

def password():
    print("please tell me the password,because this file is password protected")
    speak("please tell me the password,because this file is password protected")
    pas2 = "subscribe"
    pas1 = takecommand()
    if pas1 == pas2:
        speak("correct password")
        print("correct password")
    else:
        speak("wrong password")
        print("wrong password")
        speak("program is closing in...")
        print("3")
        speak("3")
        print("2")
        speak("2")
        print("1")
        speak("1")
        sleep(2)
        os.system('cls')
        os.abort()
password()
def temperature():
    search = "temperature in hyderabad"
    url = f"https://www.google.com/search?q={search}"
    r = requests.get(url)
    data = BeautifulSoup(r.text, "html.parser")
    temp = data.find("div", class_="BNeawe").text
    speak(f"current {search} is {temp}")
    print(f"current {search} is {temp}")
def note():
    speak("ok sir opening notepad")
    keyboard.press_and_release("win + s")
    sleep(1)
    keyboard.write("notepad")
    sleep(3)
    keyboard.press_and_release("enter")
    sleep(1)
    speak("what should i notedown sir")
    note=takecommand()
    keyboard.write(note)
    sleep(1)
    speak("should i save this sir")
    sa=takecommand()
    if sa=="yes" or sa=="sure":
        keyboard.press_and_release("ctrl + s")
        sleep(1)
        speak("what name should i give it")
        na=takecommand()
        keyboard.write(na)
        keyboard.press_and_release("enter")
        speak("done")
        print("done")
    elif sa=="no":
        speak("ok sir")
if __name__=="__main__":
    wishMe()
    while True:
       query=takecommand().lower()
       if 'on wikipedia' in query:
           speak('searching in wikepedia')
           query=query.replace('on wikipedia','')
           query.replace('vinay','')
           query.replace('search','')
           results=wikipedia.summary(query,sentences=2)
           print(results)
           speak(results)
       elif 'temperature' in query:
          temperature()
       elif "search on youtube" in query or "on youtube" in query or "how to" in query:
           speak("searching")
           print("searching...")
           query = query.replace("neuron", "")
           query = query.replace("search", "")
           query = query.replace("on youtube", "")
           web = "https://youtube.com/results?search_query=" + query
           webbrowser.open(web)
       elif "search on google" in query or "on google" in query or "according to google" in query:
           speak("searching")
           print("searching...")
           query = query.replace("neuron", "")
           query = query.replace("search", "")
           query = query.replace("on google", "")
           web = "https://www.google.com/search?q=" + query
           webbrowser.open(web)
       elif "note" in query or "notedown" in query:
           note()
       elif "open whatsapp" in query or "whatsapp" in query:
           speak("opening whatsapp")
           print("opening whatsapp...")
           query = query.replace("neuron", "")
           query = query.replace("search", "")
           query = query.replace("open whatsapp", "")
           web = "https://web.whatsapp.com/" + query
           webbrowser.open(web)
       elif "joke" in query:
           joke=pyjokes.get_joke()
           print(joke)
           speak(joke)
       elif "instagram" in query or "instagram profile" in query:
           speak("sir,please enter the user name ")
           name=input("enter user name here:")
           webbrowser.open("www.instagram.com/"+name)
           speak("sir,here is the profile of the user"+name)
           sleep(5)
           speak("sir would you like to download the profile picture of this account")
           condition=takecommand().lower()
           if "yes" in condition:
               mod=instaloader.Instaloader()
               mod.download_profile(name,profile_pic_only=True)
               speak("i am done sir profile picture is saved in our folder,now i am ready for the next command")
           else:
               pass



