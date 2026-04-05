!pip install pynput

from pynput.keyboard import Key, Listener

def keypress(key):
    print("Key Pressed:" , key)

def keyrelease(key):
    if key == Key.esc:
        return False

with Listener(on_press=keypress,on_release = keyrelease) as lst:
    lst.join()
