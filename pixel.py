#this is used to grab coordinates, rgb, and hex values of the pixel your mouse is hovering over
#press f4 to start and f5 to stop

from ctypes import windll
import time
import keyboard
import pyautogui

hdc = windll.user32.GetDC(0)
def get_pixel_colour(i_x, i_y):
    global hdc
    return windll.gdi32.GetPixel(hdc, i_x, i_y)

def get_pixel_colour_rgb(i_x, i_y):
    i_colour = get_pixel_colour(i_x, i_y)
    return ((i_colour & 0x0ff), (i_colour & 0x0ff00) >> 8, (i_colour & 0x0ff0000) >> 16)

def get_pixel_colour_hex(i_x, i_y):
    return '%02x%02x%02x' % get_pixel_colour_rgb(i_x, i_y)

while True:
    if keyboard.is_pressed('f4'):
        mouse_x, mouse_y = pyautogui.position()
        print(mouse_x, + "," + mouse_y)
    if keyboard.is_pressed('f5'):
        break
