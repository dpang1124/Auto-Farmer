import threading
import time
import autoit
import keyboard
import tkinter as tk
import os

# Global variables
timecounter = 0
running = False
time_thread = None
farm_thread = None

# Constants
SPECIAL_ACTION_INTERVAL = 220  # seconds (test)

def farm_loop():
    global running
    last_special_action_time = 0

    first_minute_done = False

    start_time = timecounter  # Mark when we started

    while running:
        current_time = timecounter

        # === First minute sequence ===
        if not first_minute_done and (current_time - start_time) < 60:
            # Place one unit with key '5'
            keyboard.press('5')
            time.sleep(0.1)
            keyboard.release('5')
            time.sleep(0.1)

            autoit.mouse_move(1039, 452, speed=10)  # You can adjust coordinates if needed
            autoit.mouse_click()
            time.sleep(0.2)

            # Place 3 units with key '6'
            keyboard.press('6')
            time.sleep(0.1)
            keyboard.release('6')
            time.sleep(0.1)

            # First placement
            autoit.mouse_move(944, 501, speed=10)
            autoit.mouse_click()
            time.sleep(0.2)

            # Second placement
            autoit.mouse_move(1053, 555, speed=10)
            autoit.mouse_click()
            time.sleep(0.2)

            # Third placement
            autoit.mouse_move(849, 556, speed=10)
            autoit.mouse_click()
            time.sleep(0.2)

            # Now spam upgrades for the remaining of the 60 seconds
            while running and (timecounter - start_time) < 60:
                for x, y in [(1039, 452), (944, 501), (1053, 555), (849, 556)]:
                    autoit.mouse_move(x, y, speed=10)
                    autoit.mouse_click()
                    time.sleep(0.05)

                    keyboard.press('q')
                    time.sleep(0.02)
                    keyboard.release('q')
                    time.sleep(0.05)

            first_minute_done = True

        # === After first minute, continue normal farming sequence ===
        if (timecounter - last_special_action_time) >= SPECIAL_ACTION_INTERVAL:
            perform_special_action()
            last_special_action_time = timecounter

        # Your original farming code starts here
        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(1287, 242, speed=10)  # press X button on bounties
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(941, 805, speed=10)  # clicks retry if fail
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(788, 817, speed=2)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(902, 186, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)


def perform_special_action():
    autoit.mouse_move(33, 1005, speed=10)
    autoit.mouse_click()
    time.sleep(0.01)

    autoit.mouse_move(1179, 496, speed=10)
    autoit.mouse_click()
    time.sleep(0.01)

    autoit.mouse_move(849, 556, speed=10)
    autoit.mouse_click()
    time.sleep(0.01)

    autoit.mouse_move(957, 553, speed=10)
    autoit.mouse_click()
    time.sleep(0.01)

    autoit.mouse_move(902, 186, speed=10)
    autoit.mouse_click()
    time.sleep(0.01)

def timer_loop():
    global timecounter, running
    while running:
        timecounter += 1
        time_label.config(text=f"Time: {timecounter} seconds")
        time.sleep(1)

def farm_loop():
    global running
    last_special_action_time = 0

    while running:
        if (timecounter - last_special_action_time) >= SPECIAL_ACTION_INTERVAL:
            perform_special_action()
            last_special_action_time = timecounter

        # === Farming sequence ===
        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        keyboard.press('3')
        time.sleep(0.1)
        keyboard.release('3')
        time.sleep(0.02)

        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        keyboard.press('q')
        time.sleep(0.02)
        keyboard.release('q')
        time.sleep(0.01)

        autoit.mouse_move(1039, 452, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(944, 501, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(1053, 555, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(395, 645, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(569, 467, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        #cancel button
        autoit.mouse_move(960, 561, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        
        #press X button on bounties
        autoit.mouse_move(1287, 242, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        #clicks retry if fail
        autoit.mouse_move(941, 805, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)

        autoit.mouse_move(788, 817, speed=2)
        autoit.mouse_click()
        time.sleep(0.01) 

        autoit.mouse_move(902, 186, speed=10)
        autoit.mouse_click()
        time.sleep(0.01)



def start_time_counter():
    global time_thread, farm_thread, running
    if not running:
        running = True
        time_thread = threading.Thread(target=timer_loop)
        farm_thread = threading.Thread(target=farm_loop)
        time_thread.start()
        farm_thread.start()
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
    print("Exiting program...")  # Debugging
    root.quit()
    root.destroy()
    os._exit(0)  # Hard exit to make sure script dies

keyboard.add_hotkey('9', start_time_counter)
keyboard.add_hotkey('8', stop_time_counter)
keyboard.add_hotkey('0', quit_program)

# GUI setup
root = tk.Tk()
root.title("Fast Autoclicker")
root.geometry("300x300")

time_label = tk.Label(root, text="Time: 0 seconds", font=('Arial', 14))
time_label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_time_counter, width=10)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop_time_counter, width=10, state=tk.DISABLED)
stop_button.pack(pady=5)

quit_button = tk.Button(root, text="Quit", command=quit_program, width=10)
quit_button.pack(pady=5)

root.mainloop()
