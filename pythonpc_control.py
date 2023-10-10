# import pyautogui
import os
import ctypes
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



    

if __name__ == "__main__":
    commands()


if len(sys.argv) > 1:
    query = sys.argv[1]
    commands(query)
