import webbrowser
import sys
import random
import time
import pyscreenshot as ImageGrab
import numpy as np
import cv2
import keyboard
import pyautogui

def random_code():
    code = ""
    for i in range(3):
        for j in range(3):
            code += random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        if i != 2:
            code += "-"
    return code

final = [""]
count= 1

try:
    while True:
        link = "https://www.fortnitechapter4.com/" + random_code() + "/"
        webbrowser.open_new(link)
        time.sleep(2)
        #start button
        pyautogui.click(932, 815)
        count += 1
        final.clear()
        s = random_code()
        print(s)
        print(count)
        time.sleep(5)
        #exit button to close tab
        pyautogui.click(473, 13)
        if keyboard.is_pressed('f5'):
            break
except KeyboardInterrupt:
    print("Stopped")

time.sleep(100)
print("Done")

# Made by DRQSuperior#0001