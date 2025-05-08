import tkinter as tk
import threading
import time
import autoit
import pyautogui
import keyboard

# Global variables
timecounter = 0
running = False
time_thread = None
x, y = pyautogui.position()
print(f"Initial mouse position - X: {x}, Y: {y}")

def count_time():
    global timecounter, running
    
    # Move mouse to bottom of screen
    screen_width, screen_height = pyautogui.size()
    
    
    running = True
    while running:
        timecounter += 1
        time_label.config(text=f"Time: {timecounter} seconds")
        if timecounter == 15:
            autoit.mouse_move(916, 962, speed=10)
            autoit.mouse_click()
            #clicks unit
        
        # After 10 seconds, move mouse up
        if timecounter == 47:
            autoit.mouse_move(1088, 517, speed=10)
            autoit.mouse_click()
            #places unit

        if timecounter == 390:
            autoit.mouse_click()
            time.sleep(0.5)
            autoit.mouse_click()
            time.sleep(0.5)
            autoit.mouse_click()
            time.sleep(0.5)
            autoit.mouse_click()
            time.sleep(1)
            #collects rewards or whatever first
            autoit.mouse_move(1164, 795, speed=2)
            autoit.mouse_click()
            time.sleep(2)
            autoit.mouse_move(880, 170, speed=10)
            autoit.mouse_click()
            time.sleep(2)
            autoit.mouse_move(1164, 795, speed=2)
            autoit.mouse_click()
            time.sleep(5)
            autoit.mouse_move(902, 186, speed=10)
            autoit.mouse_click()
            time.sleep(0.1)
            autoit.mouse_click()
            #clicks replay waits 7 seconds clicks voteskip
            timecounter = 0
            
            
        time.sleep(1)

def start_time_counter():
    global time_thread
    if time_thread is None or not time_thread.is_alive():
        time_thread = threading.Thread(target=count_time, daemon=True)
        time_thread.start()
        start_button.config(state=tk.DISABLED)
        stop_button.config(state=tk.NORMAL)

def stop_time_counter():
    global running
    running = False
    start_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)

def quit_program():
    global running
    running = False
    root.destroy()

keyboard.add_hotkey('9', start_time_counter)
keyboard.add_hotkey('0', quit_program)

# GUI setup
root = tk.Tk()
root.title("Mouse Mover with Timer")
root.geometry("300x300")

# Time display label
time_label = tk.Label(root, text="Time: 0 seconds", font=('Arial', 14))
time_label.pack(pady=20)

# Start button
start_button = tk.Button(root, text="Start", command=start_time_counter, width=10)
start_button.pack(pady=5)

# Stop button
stop_button = tk.Button(root, text="Stop", command=stop_time_counter, width=10, state=tk.DISABLED)
stop_button.pack(pady=5)

# Quit button
quit_button = tk.Button(root, text="Quit", command=quit_program, width=10)
quit_button.pack(pady=5)

root.mainloop()