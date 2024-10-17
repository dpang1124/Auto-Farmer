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



    '''
    im1 = '../images/reconnect.png'
    im2 = '../images/highdetailshark.png'
    im3 = '../images/play.png'
    im4 = '../images/sharkclose.png'
    while(running):
        
        try:
            location = pyautogui.locateOnScreen(im1)
            if location:
                print(f"Image found at: {location}")
                time.sleep(1)
                mouse.move(location.left, location.top, absolute=True, duration=2)
                mouse.click('left')
                time.sleep(1)
                mouse.click('left')
        except pyautogui.ImageNotFoundException:
            print("Image not found, retrying..")
        
        time.sleep(5)

        try:
            location2 = pyautogui.locateOnScreen(im2)
            if location2:
                print(f"Details found at: {location2}")
                time.sleep(1)
                mouse.move(location2.left, location2.top, absolute=True, duration=2)
                mouse.click('left')
                time.sleep(1)
                mouse.click('left')
        except pyautogui.ImageNotFoundException:
                print("detail image not found, retrying..")
            
        time.sleep(3)

        try:
            location3 = pyautogui.locateOnScreen(im3)
            if location3:
                print(f"Details found at: {location3}")
                time.sleep(1)
                mouse.move(location3.left, location3.top, absolute=True, duration=2)
                mouse.click('left')
                time.sleep(1)
                mouse.click('left')
        except pyautogui.ImageNotFoundException:
                print("play image not found, retrying..")
        
        time.sleep(3)

        try:
            location4 = pyautogui.locateOnScreen(im4)
            if location4:
                print(f"Details found at: {location4}")
                time.sleep(1)
                mouse.move(location4.left, location4.top, absolute=True, duration=2)
                mouse.click('left')
                time.sleep(1)
                mouse.click('left')
        except pyautogui.ImageNotFoundException:
                print("close image not found, retrying..")
        '''