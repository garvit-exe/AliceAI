import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                  
from pyautogui import click
from os import startfile
import psutil

import requests
from bs4 import BeautifulSoup

import wikipedia


engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)
engine.setProperty('volume', 2.0)               
voices = engine.getProperty('voices')            
engine.setProperty('voice',voices[1].id)        

def speak(audio):                           
    engine.say(audio)
    engine.runAndWait()


def listen():                            
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening...')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:                                            
        print('Recognizing...')
        query = r.recognize_google(audio,language = 'en-in')  
        print(f'User said: {query}\n')

    except Exception as e :
        print('Say that again please...')  
        listen()   
        return 'None'  
    return query



def khyati(query):
        
    if 'internet speed' in query:
        import speedtest
        st = speedtest.Speedtest()
        dl = st.download()
        up = st.upload()
        speak(f'The download speed is : {dl} and the upload speed is : {up}')
        
    elif 'wikipedia' in query:
        speak("Searching Wikipedia...")
        query = query.replace("wikipedia","")
        results = wikipedia.summary(query,sentences = 2)
        print(results)
        speak(results)
        
    elif 'temperature' in query:
        search = 'temperature in bhopal'
        url = f"https://www.google.com/search?q={search}"   
        r = requests.get(url)     
        data = BeautifulSoup(r.text, 'html.parser')
        temp = data.find('div', class_= 'BNeawe').text
        speak(f'current{search} is {temp}')
        print()
        
    elif 'battery percentage' in query:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        speak(f'The battery percentage is {percentage}')
