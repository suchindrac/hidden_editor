import tkinter as tk
from tkinter.scrolledtext import ScrolledText
from pynput import keyboard

import os
import random

listener = None
sp_keys = {
            keyboard.Key.space: " ",
            keyboard.Key.enter: "\n",
        }

def on_press(key):
    global text_pad

    if key == keyboard.Key.f4:
        return False

    try:
        text_pad.insert(tk.INSERT, key.char)

    except AttributeError:
        if key == keyboard.Key.left:
            text_pad.mark_set(tk.INSERT, "insert-1c")
        elif key == keyboard.Key.right:
            text_pad.mark_set(tk.INSERT, "insert+1c")
        elif key == keyboard.Key.up:
            text_pad.mark_set(tk.INSERT, "insert-1l")
        elif key == keyboard.Key.down:
            text_pad.mark_set(tk.INSERT, "insert+1l")

        try:
            text_pad.insert(tk.INSERT, sp_keys[key])
            text += sp_keys[key]
        except:
            pass

def on_release(key):
    pass

def on_key(e):
    global listener
    if e.keycode == 67:
        #
        # Start listener upon key press event for F1 when editor is focused
        #
        listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
        listener.start()

if __name__ == "__main__":
    root = tk.Tk()

    root.title("Hidden Editor")
    root.geometry("800x800")
    root.bind_all('<Key>', on_key)

    text_pad = ScrolledText(root, width=800, height=800)
    text_pad.pack()

    #
    # Non-blocking listener
    #
    listener = keyboard.Listener(on_press=on_press, on_release=on_release, suppress=True)
    listener.start()

    root.mainloop()
