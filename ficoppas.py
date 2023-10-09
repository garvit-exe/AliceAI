import pyautogui
import time 

def ficoppas(query):
    time.sleep(1)
    pyautogui.hotkey('win','e')
    time.sleep(1)
    pyautogui.hotkey('shift','tab')
    time.sleep(1)
    pyautogui.press('h')
    # 
    # pyautogui.keyUp('tab')
    # time.sleep(1)
    # pyautogui.keyUp('shift')
    # time.sleep(1)