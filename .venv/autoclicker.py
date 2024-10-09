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

#autoclicker (change time.sleep(preferred_time) to control time pauses between clicks)
running = False

def beginfarm():
    global running
    running = True
    while(running):
        print(f"running = {running}")
        pyautogui.click()
        time.sleep(1)
        

def endfarm():
    global running
    running = False
    print(f"running = {running}")

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