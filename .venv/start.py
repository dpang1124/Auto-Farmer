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

def beginfarm():
    global running
    running = True
    while(running):
        pyautogui.click()
        time.sleep(1)

def endfarm():
    global running
    running = False

def start_farm_thread():
    threadfarm.daemon = True
    threadfarm.start()

#you can use 'ctrl+s' for key combinations if you want to change
keyboard.add_hotkey('9', start_farm_thread)
keyboard.add_hotkey('0', endfarm)  

#GUI
threadfarm = threading.Thread(target=beginfarm)
root = tk.Tk()
root.title("AutoFarm Gui")
root.geometry("300x200")
start_button = tk.Button(root, text="Start \ 9", command=start_farm_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop \ 0", command=endfarm)
stop_button.pack(padx=20, pady=20)
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