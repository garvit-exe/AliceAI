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
            # brightness = ctypes.c_long()
            # ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(brightness))
            # brightness = brightness.value + 10  # Increase brightness by 10
            # ctypes.windll.powrprof.PowerSetActiveScheme(DISPLAY_BRIGHTNESS, brightness)
            # pyautogui.hotkey("fn", "f3", interval=0.25)
            # pyautogui.hotkey('fn','f3')
            #  with pyautogui.hold('fn'):
            #      pyautogui.press(['f3'])
            

 
# get current brightness value
            #  print(sbc.get_brightness())
              
             #set brightness to 50%
             sbc.set_brightness(100)
              
             print(sbc.get_brightness())
            # time.sleep(0.25)
            # pyautogui.keyDown('f3')
            # pyautogui.keyUp('f3')
            # pyautogui.keyUp('fn')
             if "slightly" in query:

                  sbc.set_brightness(70)
              
                  print(sbc.get_brightness())            


        elif "decrease" in query:
            # brightness = ctypes.c_long()
            # ctypes.windll.kernel32.GetPhysicallyInstalledSystemMemory(ctypes.byref(brightness))
            # brightness = brightness.value - 10  # Decrease brightness by 10
            # ctypes.windll.powrprof.PowerSetActiveScheme(DISPLAY_BRIGHTNESS, brightness)
            # pyautogui.hotkey("fn", "f2", interval=0.25)
             sbc.set_brightness(0)
              
             print(sbc.get_brightness())


             if "slightly" in query:

                  sbc.set_brightness(20)
              
                  print(sbc.get_brightness())  


    # if "keyboard lighting" in query:
    #     if "on" in query:
    #         time.sleep(2)
    #         # Simulate the fn+F4 keyboard shortcut to turn on keyboard lighting
    #         pyautogui.hotkey("fn", "f4")
    #     elif "off" in query:
    #         # Simulate the fn+F4 keyboard shortcut to turn off keyboard lighting
    #         pyautogui.hotkey("fn", "f4")

# if __name__ == '__main__':
if len(sys.argv) > 1:
    query = sys.argv[1]
    commands(query)
