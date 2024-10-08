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
timecounter = 1
holder = False
threadfarm = None
threadcounter = None

def beginfarm():
    global running
    running = True
    while(running):
        if(screenshot):
            #move mouse to green bar when green bar is full
            pyautogui.moveTo(955, 990)
            pyautogui.click()
            time.sleep(0.1)
            pyautogui.moveTo(955, 512)
        else:
            pyautogui.click()
            time.sleep(0.1)
        
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
    timecounter = 1
    while(timebool):
        timecounter+=1
        print(f"timecounter = {timecounter}")
        time.sleep(1)
        if(timecounter%10==0):
            #generate movement pattern 1 every 30 seconds
            print(f"\n MOD 10 COMPLETE NOW MOVE, TIMECOUNTER = {timecounter} \n")
        elif(timecounter%50==0):
            #generate movement pattern 2 every 50 seconds
            print(f"\n MOD 50 COMPLETE NOW MOVE, TIMECOUNTER = {timecounter} \n")

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
keyboard.add_hotkey('0', StopAndReset_timer)  

#GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x300")
start_button = tk.Button(root, text="Start / 9", command=start_farm_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop / 0", command=endfarm)
stop_button.pack(padx=20, pady=20)
start_time = tk.Button(root, text="TimeCounter / 1", command=start_time_counter_thread)
start_time.pack(padx=20, pady=20)
stop_time = tk.Button(root, text="Stop and Reset Timer / 2", command=StopAndReset_timer)
stop_time.pack(padx=20, pady=20)
root.mainloop()


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