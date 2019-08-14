# -*- coding: utf-8 -*-
import tkinter 
import time
import Smart_File
import wifi
import voice
import os
long_click_flag = 0

def aa(event):
    global long_click_flag
    long_click_flag = time.time() 
    print("just click!")

def aaa():
    global long_click_flag
    if(time.time() - long_click_flag < 1.5):
        return
    print("long click")
    long_click_flag = time.time()

if __name__ == '__main__':
    window=tkinter.Tk()
    window.title("Graduation Project")
    window.geometry("640x400+100+100")
    #window.resizable(False, False)
    #frame = Frame(window, width=600, height=300)

    def toggle_fullscreen(event=None):
        window.state = not window.state  # Just toggling the boolean
        window.attributes("-fullscreen", window.state)
        return "break"    
    window.bind("<F11>", toggle_fullscreen)

    frame1=tkinter.Frame(window)
    button1 = tkinter.Button(frame1, text="와이파이 연결",
                             repeatdelay=100,
                             repeatinterval=100,
                             command = aaa, height = 10, width = 25)
    button1.bind("<Button-1>", aa)
    button1.pack()
    frame1.pack()
    window.mainloop
