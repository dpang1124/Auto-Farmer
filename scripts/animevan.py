import tkinter as tk
import autoit
import pyautogui
import keyboard
import time
import threading

def perform_clicks():
    # Sequence of mouse clicks without delays from a timer

    # Click unit
    autoit.mouse_move(916, 962, speed=10)
    autoit.mouse_click()

    # Place unit
    autoit.mouse_move(1088, 517, speed=10)
    autoit.mouse_click()

    # Collect rewards or perform repeated clicks
    for _ in range(4):
        autoit.mouse_click()
        time.sleep(0.5)

    # Click other coordinates as in original sequence
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

def start_clicks():
    threading.Thread(target=perform_clicks, daemon=True).start()

def quit_program():
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Mouse Clicker")
root.geometry("300x200")

start_button = tk.Button(root, text="Start", command=start_clicks, width=10)
start_button.pack(pady=10)

quit_button = tk.Button(root, text="Quit", command=quit_program, width=10)
quit_button.pack(pady=10)

keyboard.add_hotkey('9', start_clicks)
keyboard.add_hotkey('0', quit_program)

root.mainloop()
