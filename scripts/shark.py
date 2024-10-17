import pyautogui
import time
import tkinter as tk
import threading
import keyboard
from numpy import random
import mouse

#import easyocr


#move mouse to corner of screen for emergency exit
pyautogui.FAILSAFE=True
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position() 
#reader = easyocr.Reader(['en'])

print(f"Current screen width: {screenWidth}\n Current screen height: {screenHeight}")
print(f"mouse x position: {currentMouseX}\n mouse y position: {currentMouseY}")


#autoclicker
running = False
timebool = False
screenshot = False
timecounter = 1
holder = False
threadfarm = None
threadcounter = None

def beginfarm():
    global timecounter
    global running
    global timebool
    running = True
    while(running):
            x = random.randint(10)
            y = random.randint(3)
            for int in range(x):
                    pyautogui.click()
                    time.sleep(y)
        

def endfarm():
    global running
    running = False

def start_farm_thread():
    global threadfarm 
    global timecounter
    if(threadfarm == None):
        threadfarm = threading.Thread(target=beginfarm)
        threadfarm.daemon = True
        threadfarm.start()
    elif(threadfarm.is_alive()==False):
        threadfarm = threading.Thread(target=beginfarm)
        threadfarm.daemon = True
        threadfarm.start()

def count_time():
    global timebool
    timebool = True
    global timecounter
    timecounter = 1
    while(timebool):
        timecounter+=1
        print(f"timecounter = {timecounter}")
        time.sleep(1)
        x=random.randint(9)
        y=random.randint(6)
        z=random.randint(6)
        if(x==0):
            time.sleep(3)
        elif(x==1):
            keyboard.press('w')
            time.sleep(y)
            keyboard.release('w')
        elif(x==2):
            keyboard.press('a')
            time.sleep(y)
            keyboard.release('a')
        elif(x==3):
            keyboard.press('s')
            time.sleep(y)
            keyboard.release('s')
        elif(x==4):
            keyboard.press('d')
            time.sleep(y)
            keyboard.release('d')
        elif(x==5):
            keyboard.press('space')
            pyautogui.mouseDown(button="right")
            time.sleep(y)
            keyboard.release('space')
            pyautogui.mouseUp(button="right")
        elif(x==6):
            keyboard.press('space')
            keyboard.press('w')
            keyboard.press('s')
            time.sleep(y)
            keyboard.release('space')
            keyboard.release('w')
            keyboard.release('s')
        elif(x==7):
            keyboard.press('w')
            keyboard.press('d')
            time.sleep(y)
            keyboard.release('w')
            keyboard.press('s')
            time.sleep(y)
            keyboard.release('d')
            time.sleep(y)
            keyboard.release('s')
        elif(x==8):
            keyboard.press('a')
            keyboard.press('w')
            time.sleep(y)
            keyboard.release('a')
            keyboard.press('d')
            time.sleep(y)
            keyboard.release('w')
            time.sleep(y)
            keyboard.release('d')
        

def start_time_counter_thread():
    global threadcounter
    if(threadcounter == None):
        threadcounter= threading.Thread(target=count_time)
        threadcounter.daemon = True
        threadcounter.start()
    elif(threadcounter.is_alive()==False):
        threadcounter = threading.Thread(target=count_time)
        threadcounter.daemon = True
        threadcounter.start()

def StopAndReset_timer():
    global timebool
    timebool = False

#you can use 'ctrl+s' for key combos
keyboard.add_hotkey('1', endfarm)  
keyboard.add_hotkey('2', StopAndReset_timer)  

#GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x300")
start_button = tk.Button(root, text="Random Clicks", command=start_farm_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop Random Clicks / 1", command=endfarm)
stop_button.pack(padx=20, pady=20)
start_time = tk.Button(root, text="Generate Movement", command=start_time_counter_thread)
start_time.pack(padx=20, pady=20)
stop_time = tk.Button(root, text="Stop Generated Movement / 2", command=StopAndReset_timer)
stop_time.pack(padx=20, pady=20)
root.mainloop()



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