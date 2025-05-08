import pyautogui
import time
import tkinter as tk
import threading
import keyboard

pyautogui.FAILSAFE = True
screenWidth, screenHeight = pyautogui.size()
currentMouseX, currentMouseY = pyautogui.position()

print(f"Current screen width: {screenWidth}\nCurrent screen height: {screenHeight}")
print(f"Mouse X position: {currentMouseX}\nMouse Y position: {currentMouseY}")

running = False
threadfarm = None

def beginfarm():
    global running
    running = True
    while running:
        pyautogui.click()
        time.sleep(0.001) 

def endfarm():
    global running
    running = False

def start_farm_thread():
    global threadfarm
    if threadfarm is None or not threadfarm.is_alive():
        threadfarm = threading.Thread(target=beginfarm)
        threadfarm.daemon = True
        threadfarm.start()


keyboard.add_hotkey('9', start_farm_thread)
keyboard.add_hotkey('0', endfarm)


root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x200")

start_button = tk.Button(root, text="Start / 9", command=start_farm_thread)
start_button.pack(padx=20, pady=20)

stop_button = tk.Button(root, text="Stop / 0", command=endfarm)
stop_button.pack(padx=20, pady=20)

root.mainloop()
