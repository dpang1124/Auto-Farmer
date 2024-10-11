import pyautogui
import time
import tkinter as tk
import threading
import keyboard

screen_width = 1920
screen_height = 1080

# Bottom middle coordinates
# '''
target_x = 974
target_y =  978



# Function to smoothly move the mouse to a target position
def smooth_move(x, y, duration=2):
    current_x, current_y = pyautogui.position()  # Get the current mouse position
    pyautogui.moveTo(x, y, duration=duration)    # Smoothly move to the target position over 'duration'

# Move the mouse smoothly to the bottom middle of the screen
time.sleep(2)
smooth_move(target_x, target_y, duration=2)  
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position() 


