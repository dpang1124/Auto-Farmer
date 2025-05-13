import threading
import time
import autoit
import keyboard
import tkinter as tk


# Global variables
timecounter = 0
running = False
time_thread = None
farm_phase = True
extra_unit_placed = False
start_time = time.time()

farm_loop_counter = 0


def count_time():
    global timecounter, running, farm_phase, extra_unit_placed, farm_loop_counter, start_time

    running = True
    start_time = time.time()

    while running:
        elapsed_time = time.time() - start_time
        timecounter += 1
        time_label.config(text=f"Time: {timecounter} cycles")

        if elapsed_time >780: 
            # === RESTART & VOTESKIP & RESET TIMER SO FARM STARTS AGAIN ===
            autoit.mouse_move(788, 817, speed=2)
            autoit.mouse_click()
            time.sleep(0.01)

            autoit.mouse_move(902, 186, speed=10)
            autoit.mouse_click()
            time.sleep(0.01)

            farm_loop_counter = 0
            extra_unit_placed = False
            elapsed_time = 0
            start_time = time.time()

        # FARM PHASE (first 3 minutes)
        if elapsed_time < 150:

            # === PLACE FARM UNIT 5 ===
            keyboard.press_and_release('5')
            time.sleep(0.12)

            autoit.mouse_move(549, 550, speed=10)  # slightly more left
            autoit.mouse_click()
            time.sleep(0.01)

            keyboard.press_and_release('q')
            time.sleep(0.03)

            # === UPGRADE UNIT 5 ===
            autoit.mouse_move(549, 550, speed=10)
            autoit.mouse_click()
            time.sleep(0.01)
            autoit.mouse_move(395, 645, speed=10)
            autoit.mouse_click()
            time.sleep(0.01)


            # === PLACE FARM UNIT 6 (3 TIMES) ===
            unit6_positions = [(543, 669), (529, 777), (549, 870)]
            for pos in unit6_positions:
                keyboard.press_and_release('6')
                time.sleep(0.12)

                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)

                keyboard.press_and_release('q')
                time.sleep(0.03)

                # === UPGRADE UNIT 6 ===
                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)
                autoit.mouse_move(395, 645, speed=10)
                autoit.mouse_click()
                time.sleep(0.01)


            farm_loop_counter += 1

            # === After 10 loops, place special unit (4) ===
            if farm_loop_counter >= 10 and not extra_unit_placed:
                    for i in range(2):
                        time.sleep(1)
                        keyboard.press_and_release('4')
                        time.sleep(0.12)

                        autoit.mouse_move(950, 611, speed=10)
                        autoit.mouse_click()
                        time.sleep(0.01)

                        keyboard.press_and_release('q')
                        
                        extra_unit_placed = True
                        time.sleep(10)
                        autoit.mouse_click()

        else:
            # === NORMAL UNIT PLACEMENT CYCLE ===

            unit3_positions = [ #jeff positions
                (1039, 452), #whoevers in slot 3
                (944, 501),
                (1053, 555),
            ]

            for pos in unit3_positions:
                keyboard.press_and_release('3')
                time.sleep(0.12)

                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)

                keyboard.press_and_release('q')
                time.sleep(0.03)

            # === UPGRADE ALL 3 UNITS ===
            for pos in unit3_positions:
                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)
                autoit.mouse_move(395, 645, speed=10)
                autoit.mouse_click()
                time.sleep(0.01)

            unit4_positions = [
                (950, 611),
                (1049, 635),
                (1211, 586),
                (1127, 433),
            ]

            for pos in unit4_positions:
                keyboard.press_and_release('4')
                time.sleep(0.12)

                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)

                keyboard.press_and_release('q')
                time.sleep(0.03)

            # === UPGRADE ALL UNIT 4s ===
            for pos in unit4_positions:
                autoit.mouse_move(pos[0], pos[1], speed=10)
                autoit.mouse_click()
                time.sleep(0.01)
                autoit.mouse_move(395, 645, speed=10)
                autoit.mouse_click()
                time.sleep(0.01)

        if not running:
            break


def start_stop_time_counter():
    global running, time_thread
    if not running:
        start_time_counter()
    else:
        stop_time_counter()


def start_time_counter():
    global time_thread, running, farm_phase, extra_unit_placed, farm_loop_counter
    if not running:
        running = True
        farm_phase = True
        extra_unit_placed = False
        farm_loop_counter = 0

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


keyboard.add_hotkey('9', start_stop_time_counter)
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
