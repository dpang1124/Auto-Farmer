import threading
import time
import autoit
import keyboard
import tkinter as tk

# Global variables
timecounter = 0
running = False
time_thread = None

def count_time(): #sukuna use dante
    global timecounter, running

    running = True
    while running:
        timecounter += 1
        time_label.config(text=f"Time: {timecounter} cycles")

        # === STEP 1: PLACE UNIT 1 ===
        keyboard.press('3')  # Press '3' to select the unit
        time.sleep(0.1)  # Sleep for a moment to ensure it's selected
        keyboard.release('3')  # Release '3'
        time.sleep(0.02)

        # Move mouse to the first coordinate (1039, 452) and click to place the unit
        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)  # Small delay after clicking

        keyboard.press('q')  # Press 'q' to cancel
        time.sleep(0.02)
        keyboard.release('q')  # Release 'q'
        time.sleep(0.01)

        # === STEP 2: PLACE UNIT 2 ===
        keyboard.press('3')  # Press '3' to select the unit
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        # Move mouse to the second coordinate (944, 501) and click to place the unit
        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')  # Press 'q' to cancel
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        # === STEP 3: PLACE UNIT 3 ===
        keyboard.press('3')  # Press '3' to select the unit
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        # Move mouse to the third coordinate (1053, 555) and click to place the unit
        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')  # Press 'q' to cancel
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        # === STEP 4: UPGRADE UNIT 1 ===
        # Click on the first placed unit (1039, 452)
        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        # Click the upgrade button (395, 645)
        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)


        # === STEP 5: UPGRADE UNIT 2 ===
        # Click on the second placed unit (944, 501)
        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        # Click the upgrade button (395, 645)
        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)



        # === STEP 6: UPGRADE UNIT 3 ===
        # Click on the third placed unit (1053, 555)
        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        # Click the upgrade button (395, 645)
        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)


        # === STEP 7: RESTART AND VOTESKIP ===
        # Restart button (1164, 795)
        autoit.mouse_move(788, 817, speed=2)
        autoit.mouse_click()
        time.sleep(0.01)

        # Votekick button (902, 186)
        autoit.mouse_move(902, 186, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        #press X button on bounties
        autoit.mouse_move(1287, 242, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        if not running:
            break

def start_time_counter():
    global time_thread, running
    if not running:
        running = True
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
keyboard.add_hotkey('8', stop_time_counter)
keyboard.add_hotkey('0', quit_program)

# GUI setup
root = tk.Tk()
root.title("Fast Autoclicker")
root.geometry("300x300")

# Time display label
time_label = tk.Label(root, text="Time: 0 cycles", font=('Arial', 14))
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
