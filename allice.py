import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                  
import subprocess
from pythonpc_control import commands


engine = pyttsx3.init('sapi5')                   
voices = engine.getProperty('voices')            
engine.setProperty('voice',voices[1].id)        

def speak(audio):                           
    engine.say(audio)
    engine.runAndWait()                 

def startup():                                   
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('Good Morning')

    elif hour>=12 and hour<18:
        speak('Good Afternoon')

    else:
        speak('Good Evening')

    speak('Hello, I am ALICE, your Artificial intelligence assistant. Please tell me how may I help you')

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
        return 'None'  
    return query

if __name__ == '__main__' :           
    startup()
    while True:
        query = listen().lower() 
        
        if 'alice' in query and 'introduce' in query:
            speak("Sure, Hi, I am Alice, short for Artificial Linguistic Intelligent Computer Entity. I am an advanced AI voice assistant designed to understand and respond to human language. I have been developed by Team two seventy seven of VIT Bhopal University for the course Project Exhibition 1. You can interact with me by asking questions, seeking information, requesting assistance with various tasks, or simply engaging in a conversation. I'm here to provide helpful and informative responses to the best of my abilities.")     
        
        if 'exit' in query or ('alice' in query and 'sleep' in query):
            speak('for sure, please call me when you need me')
            quit()


        if "volume" in query or "brightness" in query or "keyboard lighting" in query:
            commands(query)

