#!/usr/bin/env python
# -*- coding: utf-8 -*-
# AGT
# Copyright 2019 Ariel H Garcia Traba <ariel.garcia.traba@gmail.com>

def limpiar():
	import os
	if os.name == 'nt':
		os.system('cls')
	else:
		os.system('clear')
from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)
        
        load = Image.open("brazo_robotico.jpg")
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)

        
root = Tk()
app = Window(root)
root.wm_title("Tkinter window")
root.geometry("400x300")
root.mainloop()
