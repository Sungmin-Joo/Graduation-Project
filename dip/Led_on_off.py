#-*-coding: utf-8 -*-
from tkinter import * #기본적인 윈도우를위한 import
from tkinter import ttk #label 쓰면서 import 했음 + button
from tkinter import messagebox #message import
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)
GPIO.output(21,False)
win = Tk()                   
#win.geometry('400x100+200+200')
win.attributes('-fullscreen',True)
def ok():                
	str = 'nothing selected'
	if radVar.get() == 1:
		str = "Radio 1 selected"
		GPIO.output(21,True)
	if radVar.get() == 2:
		str = "Radio 2 selceted"
		GPIO.output(21,False)
	messagebox.showinfo("Button Clikck", str)
	

'''
def finish():
	grobal win
	win.quit()
'''	
radVar = IntVar()
r1 = ttk.Radiobutton(win, text = "button_1", variable = radVar, value = 1)  
r1.grid(column=0, row=0)  
r2 = ttk.Radiobutton(win, text = "button_2", variable = radVar, value = 2)
r2.grid(column=0, row=1)
action = ttk.Button(win, text = "Click Me", command = ok)
action.grid(column = 0, row = 2)  
exit_button = ttk.Button(win, text = "Exit window", command = win.destroy)
exit_button.grid(column = 1, row = 2)
win.mainloop()   
