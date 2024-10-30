# PRODIGY_CS_04

Here’s a simple, educational example of a keylogger built in Python using the pynput library. This program will record keystrokes and save them to a local file. Ensure you have permission and a controlled environment for testing purposes only.

# Prerequisites
You’ll need the pynput library, which can be installed using:
pip install pynput

# Explanation
on_press(key): This function logs each keystroke to the file keylog.txt. It writes characters directly and represents special keys (like Enter, Shift) in a readable format.
on_release(key): This function stops the keylogger if the Esc key is pressed.
keyboard.Listener: This is an event listener that tracks key presses and releases.

# Important Ethical Notes
Only use this for educational purposes or with explicit consent in a controlled environment.
Ensure compliance with privacy laws and organizational policies if used in any professional or educational setting.
