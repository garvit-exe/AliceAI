# import pyautogui
import os
import ctypes
import pyautogui
import sys
import time
import screen_brightness_control as sbc



# Define constants for volume control
VK_VOLUME_UP = 0xAF
VK_VOLUME_DOWN = 0xAE

# Define constants for brightness control
DISPLAY_BRIGHTNESS = -1  # Use -1 to indicate the primary display

def commands(query):
    query = query.lower()

    if "volume" in query:
        if "increase" in query:
            ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 0, 0)
            ctypes.windll.user32.keybd_event(VK_VOLUME_UP, 0, 2, 0)
        elif "decrease" in query:
            ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, 0, 0)
            ctypes.windll.user32.keybd_event(VK_VOLUME_DOWN, 0, 2, 0)

    if "brightness" in query:
        if "increase" in query:
 
             sbc.set_brightness(100)
              
             print(sbc.get_brightness())
           
             if "slightly" in query:

                  sbc.set_brightness(70)
              
                  print(sbc.get_brightness())            


        elif "decrease" in query:
    
             sbc.set_brightness(0)
              
             print(sbc.get_brightness())


             if "slightly" in query:

                  sbc.set_brightness(20)
              
                  print(sbc.get_brightness())  


    if "shutdown" in query:
        pyautogui.hotkey('win','x')
        time.sleep(1)
        pyautogui.press('up',presses=2)
        pyautogui.press('enter')
        pyautogui.press('up',presses=2)
        pyautogui.press('enter')
        
    if "sleep" in query:
        pyautogui.hotkey('win','x')
        time.sleep(1)
        pyautogui.press('up',presses=2)
        pyautogui.press('enter')
        pyautogui.press('down')
        pyautogui.press('enter')

    if "restart" in query:
        pyautogui.hotkey('win','x')
        time.sleep(1)
        pyautogui.press('up',presses=2)
        pyautogui.press('enter')
        pyautogui.press('up')
        pyautogui.press('enter')
        
    if "sign out" in query:
        pyautogui.hotkey('win','x')
        time.sleep(1)
        pyautogui.press('up',presses=2)
        pyautogui.press('enter',presses=2)

    if "open application" in query:
            pyautogui.hotkey('win','s')
            query=query.replace("open application ","")
            time.sleep(1)
            pyautogui.write(query)   
            pyautogui.press('enter')    


if len(sys.argv) > 1:
    query = sys.argv[1]
    commands(query)
