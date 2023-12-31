import pyttsx3                                    
import datetime                                   
import speech_recognition as sr   
import subprocess
import os
from pythonpc_control import commands
from ficoppas import ficoppas
from automation import youtube, WhatsAppMsg, WhatsAppVoiceCall, WhatsAppVideoCall, WhatsAppVoiceRecording, SearchMusic, OpenPlaylist, SpotifyAuto, ChromeAuto
from khyati import khyati

import pyautogui
import time

engine = pyttsx3.init('sapi5')
# engine.setProperty('rate', 170)
# engine.setProperty('volume', 2.0)               
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

    # speak('Hello, I am ALICE, your Artificial intelligence assistant. Please tell me how may I help you')

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
        
        elif 'exit' in query or ('alice' in query and 'sleep' in query):
            speak('for sure, please call me when you need me')
            quit()


        # Riya's Section
        elif 'youtube' in query:
            youtube(query)
            
        elif 'whatsapp message' in query:
            name = query.replace("send whatsapp","")
            name = name.replace("message ","")
            name = name.replace("to ","")
            Name = str(name)
            speak("what is the message for {name}")
            MSG = listen()
            MSG = str(MSG)
            WhatsAppMsg(Name,MSG)

        elif 'voice call' in query :
            name = query.replace("whatsapp voice","")
            name = name.replace("call","")
            name = name.replace("to","")
            Name = str(name)
            speak("calling to {name}")
            WhatsAppVoiceCall(name)
            
        elif 'video call' in query:
            name = query.replace("whatsapp video","")
            name = name.replace("call","")
            name = name.replace("to","")
            Name = str(name)
            speak("calling to {name}")
            WhatsAppVideoCall(name)
            
        elif 'voice recording' in query:
            name = query.replace("send whatsapp voice ","")
            name = name.replace("recording","")
            name = name.replace("to","")
            Name = str(name)
            speak("calling to {name}")
            WhatsAppVideoCall(name)
            
            
        elif 'chrome ' in query:
            ChromeAuto(query)
        
        elif  'find song ' in query:
            name = query.replace("find song","")
            Name = str(name)
            SearchMusic(name)
            
        elif 'open playlist' in query:
            name = query.replace("open playlist","")
            Name = str(name)
            OpenPlaylist(name)
            
        elif 'spotify' in query:
            SpotifyAuto(query)
            
        # Khyati's Section
        khyati(query)
        
        # Garvit's Section
        if "volume" in query or "brightness" in query or "keyboard lighting" in query or "shutdown" in query or "sleep" in query or "restart" in query or "sign out" in query or "open application" in query:
            commands(query)

        # Shashidhar's Section
        if  "files" in query:
            ficoppas(query)
    
        if "open home" in query:
            time.sleep(1)
            pyautogui.press('h')
            pyautogui.press('enter')
            time.sleep(1)
            
        if "open gallery" in query:
            time.sleep(1)
            pyautogui.press('g')
            pyautogui.press('enter')

        if "open onedrive" in query:
            time.sleep(1)
            pyautogui.press('o')
            pyautogui.press('enter')

        if "open desktop" in query:
           time.sleep(1) 
           pyautogui.keyDown('d')
           pyautogui.keyUp('d')
           pyautogui.keyDown('enter')
           pyautogui.keyUp('enter')
        
        if "open downloads" in query:
           time.sleep(1)
           pyautogui.press('d',presses=2)
           pyautogui.press('enter')

        if "open documents" in query:
            time.sleep(1)
            pyautogui.press('d',presses=3)
            pyautogui.press('enter')

        if "open pictures" in query:
            time.sleep(1)
            pyautogui.press('p')
            pyautogui.press('enter')

        if "open music" in query:
            time.sleep(1)
            pyautogui.press('m')
            pyautogui.press('enter')

        if "open videos" in query:
            time.sleep(1)
            pyautogui.press('v')
            pyautogui.press('enter')

        if "open khajane 2 application" in query:
            time.sleep(1)
            pyautogui.press('k')
            pyautogui.press('enter')

        if "open screenshots" in query:
            time.sleep(1)
            pyautogui.press('s')
            pyautogui.press('enter')

        if "open alice" in query:
            time.sleep(1)
            pyautogui.press('a')
            pyautogui.press('enter')

        if "open another alice" in query:
            time.sleep(1)
            pyautogui.press('a',presses=2)
            pyautogui.press('enter')

        if "open class notes" in query:
            time.sleep(1)
            pyautogui.press('c')
            pyautogui.press('enter')

        if "open this pc" in query:
            time.sleep(1)
            pyautogui.press('t')
            pyautogui.press('enter')

        if "open windows c" in query:
            time.sleep(1)
            pyautogui.press('w')
            pyautogui.press('enter')

        if "open new volume"  in query:
            time.sleep(1)
            pyautogui.press('n')
            pyautogui.press('enter')

        if "open network" in query:
            time.sleep(1)
            pyautogui.press('n')
            pyautogui.press('enter')

        if "search" in query:
            time.sleep(1)
            pyautogui.keyDown('shift')
            time.sleep(1)
            pyautogui.press('tab',presses=3)
            time.sleep(1)
            pyautogui.keyUp('shift')
            time.sleep(1)
            query = query.replace('search', " ")
            pyautogui.write(query)
            time.sleep(5)
            pyautogui.press('tab',presses=4)
            pyautogui.press('down')
            pyautogui.press('up')

        if "open" in query:
            pyautogui.press('enter')
 
        if "copy" in query:
            pyautogui.hotkey('ctrl','c')
            pyautogui.hotkey('shift','tab')
            pyautogui.press('h')

        if "paste" in query:
            pyautogui.hotkey('ctrl','v')

        if "down" in query:
            pyautogui.press('down')

        if "up" in query:
            pyautogui.press('up')

        if "select" in query:
            pyautogui.keyDown('shift')

        if "release" in query:
            pyautogui.keyUp('shift')

        if "back" in query:
            pyautogui.press('backspace')
        
        # closes window
        if "close" in query:
            pyautogui.hotkey('alt','f4')

