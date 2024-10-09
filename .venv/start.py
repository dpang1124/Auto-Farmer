import pyautogui
import time
import tkinter as tk
import threading
import keyboard

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
timecounter = 0
holder = False
threadfarm = None
threadcounter = None

def beginfarm():
    global running
    running = True
    while(running):
        pyautogui.click()
        time.sleep(1)
        if(holder):
            #move mouse to green bar
            pyautogui.moveTo(955, 990)
            pyautogui.click()
            time.sleep(1)
            pyautogui.moveTo(955, 512)
        if(holder):
            #generate movement pattern 1
            pyautogui.keyDown('w')
            time.sleep(2)
            pyautogui.keyUp('w')
            time.sleep(2)
            pyautogui.keyDown('a')
            time.sleep(2)
            pyautogui.keyUp('a')
        if(holder):
            #generate movement pattern 2
            pyautogui.keyDown('d')
            time.sleep(2)
            pyautogui.keyUp('d')
            time.sleep(2)
            pyautogui.keyDown('s')
            time.sleep(2)
            pyautogui.keyUp('s')
            

def endfarm():
    global running
    running = False

def start_farm_thread():
    global threadfarm 
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
    timecounter = 0
    while(timebool):
        timecounter+=1
        print(f"time = {timecounter}")
        time.sleep(1)

def start_time_counter():
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

#GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x300")
start_button = tk.Button(root, text="Start \ 9", command=start_farm_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop \ 0", command=endfarm)
stop_button.pack(padx=20, pady=20)
start_time = tk.Button(root, text="TimeCounter", command=start_time_counter)
start_time.pack(padx=20, pady=20)
stop_time = tk.Button(root, text="Stop and Reset Timer", command=StopAndReset_timer)
stop_time.pack(padx=20, pady=20)
root.mainloop()

'''
#move mouse to green bar
pyautogui.dragTo(955, 990, 0)
pyautogui.click()
time.sleep(1)
pyautogui.dragTo(955, 512, 0)
'''








"""
cheat sheet provided by pyautogui documentation:

screenWidth, screenHeight = pyautogui.size() # Get the size of the primary monitor.
currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of the mouse.

pyautogui.moveTo(100, 150) # Move the mouse to XY coordinates.
pyautogui.click() # Click the mouse.
pyautogui.click(100, 200)  # Move the mouse to XY coordinates and click it.
pyautogui.click('button.png') # Find where button.png appears on the screen and click it.
pyautogui.move(400, 0)      # Move the mouse 400 pixels to the right of its current position.
pyautogui.doubleClick()     # Double click the mouse.
pyautogui.moveTo(500, 500, duration=2, tween=pyautogui.easeInOutQuad)  # Use tweening/easing function to move mouse over 2 seconds.
pyautogui.write('Hello world!', interval=0.25)  # type with quarter-second pause in between each key
pyautogui.press('esc')     # Press the Esc key. All key names are in pyautogui.KEY_NAMES
with pyautogui.hold('shift'):  # Press the Shift key down and hold it.
        pyautogui.press(['left', 'left', 'left', 'left'])  # Press the left arrow key 4 times.
# Shift key is released automatically.
pyautogui.hotkey('ctrl', 'c') # Press the Ctrl-C hotkey combination.
pyautogui.alert('This is the message to display.') # Make an alert box appear and pause the program until OK is clicked.
"""