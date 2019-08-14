from tkinter import *
from tkinter import messagebox
'''
root = Tk()
Label(root, text = 'Hello World').pack()
root.mainloop()
'''

class Window(Frame):

    def __init__(self, master = None):
        Frame.__init__(self, master)
        self.master = master
        self.init_window()

    def init_window(self):

        self.master.title("GUI Window")
        self.pack(fill = BOTH, expand = 1)
        quitButton = Button(self, text = "Message", command = okClick)

        quitButton.place(x = 0, y = 0)

def okClick():
    messagebox.showinfo("box", "안녕하신가")

A = Tk()
A.geometry("500x400")

app = Window(A)
A.mainloop()
