import pyttsx3                                    
import datetime                                   
import speech_recognition as sr                  
import time
import webbrowser
import pyautogui
from keyboard import press
from keyboard import press_and_release
from keyboard import write
from pyautogui import click
from os import startfile

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

def youtube(command):
    query = str(command)
    if 'open' in query:
        webbrowser.open("www.youtube.com")
    elif 'pause' in query:
        press('space bar')
    elif 'resume' in query:
        press('space bar')
    elif 'fullscreen' in query:
        press('f')
    elif 'film screen' in query:
        press('t')
    elif 'skip' in query:
        press('l')
    elif 'back' in query:
        press('j')
    elif 'increse' in query:
        press_and_release('shift + >')
    elif 'decrese' in query:
        press_and_release('shift + <')
    elif 'previous' in query:
        press_and_release('shift + p')
    elif 'next' in query:
        press_and_release('shift + n')
    elif 'miniplayer' in query:
        press('i')
    elif 'mute' in query:
        press('m')
    elif 'search' in query:
        click(x=1735, y=28)
        search = listen()
        write(search)
        time.sleep(1)
        press('enter')
        
def WhatsAppMsg(name,message):
    startfile("C:\\Users\\rajee\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    time.sleep(10)
    press_and_release('ctrl + f')
    time.sleep(1)
    write(name)
    pyautogui.hotkey('pgdn')
    pyautogui.hotkey('enter')
    time.sleep(2)
    
    write(message)
    press('enter')       

def WhatsAppVoiceCall(name):
    startfile("C:\\Users\\rajee\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    time.sleep(10)
    press_and_release('ctrl + f')
    time.sleep(1)
    write(name)
    pyautogui.hotkey('pgdn')
    pyautogui.hotkey('enter')
    time.sleep(2)
    click(x=457, y=306)
    time.sleep(2)
    click(x=1797, y=107)
    
def WhatsAppVideoCall(name):
    startfile("C:\\Users\\rajee\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    time.sleep(10)
    press_and_release('ctrl + f')
    time.sleep(1)
    write(name)
    pyautogui.hotkey('pgdn')
    pyautogui.hotkey('enter')
    time.sleep(2)
    click(x=457, y=306)
    time.sleep(2)
    click(x=1674, y=119)

def WhatsAppVoiceRecording(name,t):
    startfile("C:\\Users\\rajee\\OneDrive\\Desktop\\WhatsApp - Shortcut.lnk")
    time.sleep(10)
    press_and_release('ctrl + f')
    time.sleep(1)
    write(name)
    pyautogui.hotkey('pgdn')
    pyautogui.hotkey('enter')
    time.sleep(2)
    click(x=457, y=306)
    time.sleep(2)
    click(x=1871, y=960)
    time.sleep(t+1)
    click(x=1803, y=972)
    
def SearchMusic(name):
    startfile("C:\\Users\\rajee\\AppData\\Roaming\\Spotify\\Spotify.exe")
    time.sleep(5)
    press_and_release('ctrl + L')
    time.sleep(2)
    write(name)
    press('enter')
    time.sleep(5)
    click(x=751, y=629)
    
def OpenPlaylist(name):
    startfile("C:\\Users\\rajee\\AppData\\Roaming\\Spotify\\Spotify.exe")
    time.sleep(5)
    press_and_release('ctrl + L')
    time.sleep(2)
    write(name)
    press('enter')
    time.sleep(5)
    click(x=751, y=629)
    
def SpotifyAuto(command):
    query = str(command)
    if 'next song' in query:
        press_and_release('ctrl'+'end')
    elif 'previous song' in query:
        press_and_release('ctrl'+'home')
    elif 'repeat song' in query:
        press_and_release('ctrl'+'r')

def ChromeAuto(command):
    query = str(command)
    if 'open' in query:
        startfile("C:\\Program Files\\Google\Chrome\\Application\\chrome.exe")
        time.sleep(2)
        click(x=905, y=480)
    elif 'new window' in query:
        press_and_release('ctrl+n')
    elif 'previous window' in query:
        press_and_release('alt'+'home')
    elif 'close current tab' in query:
        press_and_release('ctrl'+'w')
    elif 'minimize' in query:
        pyautogui.hotkey('alt'+'spacebar')
        pyautogui.hotkey('n')
    elif 'maximize' in query:
        pyautogui.hotkey('alt'+'spacebar')
        pyautogui.hotkey('x')
    elif 'quit chrome' in query:
        pyautogui.hotkey('alt'+'f')
        pyautogui.hotkey('x')
    elif 'bookmark' in query:
        press_and_release('ctrl + d')
        press ('enter')
    elif 'switch tab' in query:
        tab = query.replace("switch tab","")
        Tab = tab.replace("t","")
        num = Tab
        bb = f'ctrl + {num}'
        press_and_release(bb)

           
