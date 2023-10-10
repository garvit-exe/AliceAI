import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                  
from pyautogui import click
from os import startfile

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



while True:
    query = listen().lower()
    if 'alice' in query:
        speak('ALICE is a Virtual Assistant technology based on Artificial Intelligence. It uses the device’s mic to receive voice requests, process them, and send responses via the speaker. It is a combination of different technologies like Voice Interaction, Natural Language Processing and Voice Analysis.')        
    elif 'exit' in query or ('alice' in query and 'sleep' in query):
        speak('for sure, please call me when you need me')
        
    elif 'internet speed' in query:
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
        
        
        
        quit()
        
        
    
