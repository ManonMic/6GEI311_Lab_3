import threading
import time
import sys
import msvcrt
import tkinter as tk
from tkinter import filedialog
from pathlib import Path, PureWindowsPath

sys.path.append(".\\x64\\Release")
import videoplayer


def callback():
    name = filedialog.askopenfilename(initialdir="/", title="Select file", filetypes=[("avi files", "*.avi")])
    return name


def play_video():
    videoplayer.vp_module('P')


def rewind_video():
    videoplayer.vp_module('R')


def fastforward_video():
    videoplayer.vp_module('A')


def select_path():
    path = Path(callback())
    windows_path = str(PureWindowsPath(path))
    windows_path = windows_path.replace("\\", "\\\\")
    videoplayer.vp_module(windows_path)


def window():
    window_button = tk.Tk()
    label_welcome = tk.Label(window_button, text="Interface of our video player", font="Arial, 24", background="grey")
    label_welcome.pack(side="top", fill="x")
    label_name = tk.Label(window_button, text="Application made by Manon Michelet & Jean-Michel Plourde",
                          font="Arial, 18", background="grey")
    label_name.pack(side="top", fill="x")
    label_file = tk.Label(window_button, text="Please select a file first :", font="Arial, 16")
    label_file.pack(side="top", fill="x")
    openfile_button = tk.Button(window_button, text="Select File", font="Arial", command=select_path)
    openfile_button.pack(side="top")
    label_commands = tk.Label(window_button, text="Then, use the following commands to play the video selected :",
                              font="Arial, 16")
    label_commands.pack(side="top", fill="x")
    play_button = tk.Button(window_button, text="Play", font="Arial", command=play_video)
    play_button.pack()
    fastforward_button = tk.Button(window_button, text="Fast Forward", font="Arial", command=fastforward_video)
    fastforward_button.pack()
    rewind_button = tk.Button(window_button, text="Rewind", font="Arial", command=rewind_video)
    rewind_button.pack()

    window_button.mainloop()


if __name__ == "__main__":
    window()
