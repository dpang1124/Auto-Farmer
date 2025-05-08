import pyautogui
import time
import tkinter as tk 
import threading
import keyboard
import pyscreeze  # pip install pillow
from numpy import random
import autoit      # pip install pyautoit
import sys

# Emergency exit corner
pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position() 

print(f"Current screen width: {screenWidth}\nCurrent screen height: {screenHeight}")
print(f"Mouse x position: {currentMouseX}\nMouse y position: {currentMouseY}")

# Global variables
running = False
timebool = False
screenshot = False
timecounter = 1
holder = False
threadfarm = None
threadcounter = None
threadrejoin = None
secondtimecounter = 1

def gotobigmap():
    time.sleep(10)
    autoit.mouse_move(40, 626, speed=7)
    time.sleep(1)
    autoit.mouse_click()
    autoit.mouse_move(950, 716, speed=7)
    time.sleep(0.5)
    autoit.mouse_click()
    time.sleep(0.5)
    autoit.mouse_click()
    time.sleep(5)
    autoit.mouse_move(930, 509, speed=7)
    autoit.mouse_click()
    time.sleep(3)
    keyboard.press_and_release("esc")
    time.sleep(0.5)
    keyboard.press_and_release("r")
    time.sleep(0.5)
    keyboard.press_and_release("enter")
    time.sleep(8)
    keyboard.press('w')
    keyboard.press('space')
    time.sleep(0.75)
    keyboard.release('space')
    keyboard.release('w')

def beginfarm():
    global secondtimecounter
    global timecounter
    global running
    sells = 0
    gotobigmap()
    running = True
    while running:
        if timecounter >= 290:
            time.sleep(2)
            print(f"Activating rebirth {sells}")
            sells += 1
            autoit.mouse_move(968, 1019, speed=7)
            autoit.mouse_click("left")
            time.sleep(0.5)
            autoit.mouse_click("left")
            autoit.mouse_move(958, 500, speed=7)
            time.sleep(1)
            autoit.mouse_move(26, 1013, speed=7)
            time.sleep(0.5)
            autoit.mouse_click()
            time.sleep(0.5)
            autoit.mouse_move(962, 671, speed=7)
            time.sleep(0.5)
            autoit.mouse_click()
            autoit.mouse_move(1148, 340, speed=7)
            time.sleep(0.5)
            autoit.mouse_click()
            time.sleep(10)
            keyboard.press_and_release("esc")
            time.sleep(0.5)
            keyboard.press_and_release("r")
            time.sleep(0.5)
            keyboard.press_and_release("enter")
            time.sleep(8)
            keyboard.press('w')
            keyboard.press('space')
            time.sleep(0.75)
            keyboard.release('space')
            keyboard.release('w')
            timecounter = 0
        elif secondtimecounter >= 5450:
            timecounter = 0
            #print("Collecting rewards")
            autoit.mouse_move(968, 1019, speed=7)
            autoit.mouse_click("left")
            time.sleep(1)
            autoit.mouse_move(40, 560, speed=5)
            autoit.mouse_click("left")
            reward_coords = [
                (1080, 373), (1280, 373), (1480, 373),
                (1080, 560), (1280, 560), (1480, 560),
                (1080, 743), (1280, 743), (1480, 743)
            ]
            for x, y in reward_coords:
                autoit.mouse_move(x, y, speed=5)
                autoit.mouse_click("left")
                time.sleep(0.1)
                autoit.mouse_click("left")
                time.sleep(4)
            time.sleep(1)
            keyboard.press_and_release('alt+tab')
            running = False
            start_rejoin_thread()
        else:
            for _ in range(4):
                pyautogui.click()
                time.sleep(0.2)

def addtime():
    global timecounter, secondtimecounter
    secondtimecounter += 5450
    #timecounter += 60
    print(f"timecounter = {timecounter}")

def endfarm():
    global running
    running = False

def start_farm_thread():
    global threadfarm 
    if threadfarm is None or not threadfarm.is_alive():
        threadfarm = threading.Thread(target=beginfarm, daemon=True)
        threadfarm.start()

def count_time():
    global timebool, timecounter, secondtimecounter
    timebool = True
    timecounter = 1
    while timebool:
        timecounter += 1
        secondtimecounter += 1
        #print(f"timecounter = {timecounter}")
        #print(f"secondtimecounter = {secondtimecounter}")
        time.sleep(1)

def start_time_counter_thread():
    global threadcounter
    if threadcounter is None or not threadcounter.is_alive():
        threadcounter = threading.Thread(target=count_time, daemon=True)
        threadcounter.start()

def autorejoin():
    global timecounter, secondtimecounter, running, timebool
    running = False
    timebool = False
    time.sleep(1)
    autoit.mouse_move(586, 977, speed=5)
    autoit.mouse_click("left")
    time.sleep(8)
    autoit.mouse_click("left")
    time.sleep(2)
    autoit.mouse_move(958, 500, speed=7)
    autoit.mouse_click("left")
    timecounter = 0
    secondtimecounter = 0
    start_farm_thread()
    start_time_counter_thread()

def start_rejoin_thread():
    global threadrejoin
    if threadrejoin is None or not threadrejoin.is_alive():
        threadrejoin = threading.Thread(target=autorejoin, daemon=True)
        threadrejoin.start()

def quit_program(event=None):
    root.destroy()
    sys.exit()

def StopAndReset_timer():
    global timebool
    timebool = False

# Hotkeys
keyboard.add_hotkey('9', start_farm_thread)
keyboard.add_hotkey('0', endfarm)  
keyboard.add_hotkey('1', start_time_counter_thread)
keyboard.add_hotkey('2', StopAndReset_timer)  
keyboard.add_hotkey('p', addtime)
keyboard.add_hotkey('shift+a', quit_program)

# GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x400")
tk.Button(root, text="Click and Rewards / 9", command=start_farm_thread).pack(padx=20, pady=20)
tk.Button(root, text="Stop Above / 0", command=endfarm).pack(padx=20, pady=20)
tk.Button(root, text="TimeCounter and Movement / 1", command=start_time_counter_thread).pack(padx=20, pady=20)
tk.Button(root, text="Stop Above / 2", command=StopAndReset_timer).pack(padx=20, pady=20)
tk.Button(root, text="Add time test / p", command=addtime).pack(padx=20, pady=20)
tk.Button(root, text="Auto Rejoin", command=start_rejoin_thread).pack(padx=20, pady=20)
tk.Button(root, text="Quit / Shift+A", command=quit_program).pack(padx=20, pady=20)
root.mainloop()
