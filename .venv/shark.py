import pyautogui
import time
import tkinter as tk
import threading
import keyboard
import pyscreeze



#move mouse to corner of screen for emergency exit
pyautogui.FAILSAFE=True
screenWidth, screenHeight = pyautogui.size() 
currentMouseX, currentMouseY = pyautogui.position() 

running = False
timebool = False
screenshot = pyautogui.screenshot('disconnect.png')
timecounter = 1
holder = False
threadfarm = None
threadcounter = None

def checkdisconnect():

    global running
    running = True
    while(running):

        try:
            location = pyautogui.locateOnScreen('disconnect.png')
            print(f"location={location}")
        except pyautogui.ImageNotFoundException:
            print("Image not found, retrying...")
            time.sleep(3)
      
        
def endcheck():
    global running
    running = False

def start_check_thread():
    global threadfarm 
    if(threadfarm == None):
        threadfarm = threading.Thread(target=checkdisconnect)
        threadfarm.daemon = True
        threadfarm.start()
    elif(threadfarm.is_alive()==False):
        threadfarm = threading.Thread(target=checkdisconnect)
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
        if(timecounter%20==0):
            keyboard.press_and_release(' ')
        if(timecounter%9==0):
            keyboard.press('d')
            time.sleep(0.1)  
            keyboard.release('d')
            keyboard.press('a')
            time.sleep(0.1)  
            keyboard.release('a')

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
keyboard.add_hotkey('9', start_check_thread)
keyboard.add_hotkey('0', endcheck)  
keyboard.add_hotkey('1', start_time_counter_thread)
keyboard.add_hotkey('2', StopAndReset_timer)  

#GUI
root = tk.Tk()
root.title("AutoFarmer")
root.geometry("400x300")
start_button = tk.Button(root, text="Start / 9", command=start_check_thread)
start_button.pack(padx=20, pady=20)
stop_button = tk.Button(root, text="Stop / 0", command=endcheck)
stop_button.pack(padx=20, pady=20)
start_time = tk.Button(root, text="TimeCounter / 1", command=start_time_counter_thread)
start_time.pack(padx=20, pady=20)
stop_time = tk.Button(root, text="Stop and Reset Timer / 2", command=StopAndReset_timer)
stop_time.pack(padx=20, pady=20)
root.mainloop()
