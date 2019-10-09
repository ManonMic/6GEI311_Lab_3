import threading
import time
import sys
import msvcrt
import tkinter as tk
from tkinter import filedialog
from pathlib import Path, PureWindowsPath

sys.path.append(".\\x64\\Release")
import videoplayer

# media_player = videoplayer.init()

# valid_commands = ('P', 'A', 'R', 'Q')

def callback():
	name = filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = [("avi files","*.avi")])
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
	videoplayer.vp_module('path', windows_path)

def window():
	window_button = tk.Tk()
	play_button = tk.Button(window_button, text="play", command=play_video)
	play_button.pack()
	fastforward_button = tk.Button(window_button, text="fastforward", command=fastforward_video)
	fastforward_button.pack()
	rewind_button = tk.Button(window_button, text="rewind", command=rewind_video)
	rewind_button.pack()
	openfile_button = tk.Button(window_button, text="Open File", command=select_path)
	openfile_button.pack()
	quit_button = tk.Button(window_button, text="quit", command=window_button.destroy, fg="red")
	quit_button.pack(side = "bottom")

	window_button.mainloop()

if __name__== "__main__":
	window()
