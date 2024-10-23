import pyautogui
import time
import tkinter as tk
import threading
import keyboard
from numpy import random

import autoit #pip install pyautoit


#move mouse to corner of screen for emergency exit
pyautogui.FAILSAFE=True
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position() 

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
        if(timecounter%600==0):
            time.sleep(2)
            print("activating rebirth")
            #implement sell
            autoit.mouse_move(968, 1019, speed=7)
            autoit.mouse_click("left")
            time.sleep(0.5)
            autoit.mouse_click("left")
            autoit.mouse_move(958, 500, speed=7)
            time.sleep(1)
        elif(timecounter%5450==0):
            #implement collecting rewards
            time.sleep(1)
            #reward open gui
            autoit.mouse_move(39, 529, speed=5)
            autoit.mouse_click("left")
            
            #reward 1
            autoit.mouse_move(1080, 373, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 2
            autoit.mouse_move(1280, 373, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 3
            autoit.mouse_move(1480, 373, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 4
            autoit.mouse_move(1080, 560, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 5
            autoit.mouse_move(1280, 560, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 6
            autoit.mouse_move(1480, 560, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 7
            autoit.mouse_move(1080, 743, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 8
            autoit.mouse_move(1280, 743, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            #reward 9
            autoit.mouse_move(1480, 743, speed=5)
            autoit.mouse_click("left")
            time.sleep(0.1)
            autoit.mouse_click("left")
            time.sleep(4)
            time.sleep(1)
            #implement rejoin private server
            keyboard.press_and_release('alt+tab')
            time.sleep(1)
            autoit.mouse_move(587, 1012, speed=5)
            autoit.mouse_click("left")
            time.sleep(8)
            autoit.mouse_click("left")
            time.sleep(2)
            autoit.mouse_move(958, 500, speed=7)
            autoit.mouse_click("left")
            timecounter=0
        else:
            
            try:
                reconnectbutton = '../images/reconnect.png'
                location = pyautogui.locateOnScreen(reconnectbutton)
                if location:
                    print(f"Details found at: {location}")
                    time.sleep(1)
                    keyboard.press_and_release('alt+tab')
                    time.sleep(1)
                    autoit.mouse_move(587, 1012, speed=5)
                    autoit.mouse_click("left")
                    time.sleep(8)
                    autoit.mouse_click("left")
                    time.sleep(2)
                    autoit.mouse_move(958, 500, speed=7)
                    autoit.mouse_click("left")
                    timecounter=0
            except pyautogui.ImageNotFoundException:
                print("reconnect button not found")

            for x in range(3):
                pyautogui.click()
                time.sleep(0.2)
            time.sleep(1.5)
            

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
        x=random.randint(4)
        if(x==0):
            time.sleep(0)
        elif(x==1):
            keyboard.press('w')
            time.sleep(0.01)
            keyboard.release('w')
        elif(x==2):
            keyboard.press('a')
            time.sleep(0.01)
            keyboard.release('a')
        elif(x==3):
            keyboard.press('s')
            time.sleep(0.01)
            keyboard.release('s')
        elif(x==4):
            keyboard.press('d')
            time.sleep(0.01)
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
keyboard.add_hotkey('9', start_farm_thread)
keyboard.add_hotkey('0', endfarm)  
keyboard.add_hotkey('1', start_time_counter_thread)
keyboard.add_hotkey('2', StopAndReset_timer)  

#GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x300")
start_button = tk.Button(root, text="Click and Auto-Rejoin/ 9", command=start_farm_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop Above / 0", command=endfarm)
stop_button.pack(padx=20, pady=20)
start_time = tk.Button(root, text="TimeCounter and Movement / 1", command=start_time_counter_thread)
start_time.pack(padx=20, pady=20)
stop_time = tk.Button(root, text="Stop Above / 2", command=StopAndReset_timer)
stop_time.pack(padx=20, pady=20)
root.mainloop()
