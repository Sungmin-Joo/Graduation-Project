# -*- coding: utf-8 -*-
import tkinter 
import time
import Smart_File

def Photo_mode():
    global photo_count
    global img
    Pho = tkinter.Toplevel()
    #frame = Frame(Pho, width=300, height=300)
    Photo_list = Smart_File.Find_dir_format("./",'.gif') 
    print(Photo_list)
    photo_count = len(Photo_list)
    canvas = tkinter.Canvas(Pho,width = 960, height = 400)
    canvas.create_image(0, 0, anchor = tkinter.NW, image =img)
    def click_Pho(event):
        print("클릭위치", event.x, event.y)
        Pho.destroy()
    Pho.bind("<Double-Button-1>", click_Pho) 
    canvas.grid(row = 0, column = 0)
    main_label = tkinter.Label(Pho, text = "온도정보가 표시될 부분",width = None,height =2)
    main_label.grid(row = 1, column = 0)

def Regist_address():
    pass

def Connect_wifi():
    pass

def Control_air():
    pass

def Log_in():
    pass

window=tkinter.Tk()
window.title("Graduation Project")
#window.geometry("640x400+100+100")
window.resizable(False, False)
img = tkinter.PhotoImage(file = 'Ann_Joon.gif')
#frame = Frame(window, width=600, height=300)
button1 = tkinter.Button(window, text="Regist address", command = Regist_address, height = 15, width = 25)
button2 = tkinter.Button(window, text="Photo mode", command = Photo_mode, height = 15, width = 25)
button3 = tkinter.Button(window, text="Connect wifi", command = Connect_wifi, height = 15, width = 25)
button4 = tkinter.Button(window, text="Control air", command = Control_air, height = 15, width = 25)
#에어컨 자동 수동 전환
button5 = tkinter.Button(window, text="Log_in", command = Log_in, height = 15, width = 25)

button1.grid(row = 0, column = 0)
button2.grid(row = 0, column = 1)
button3.grid(row = 0, column = 2)
button4.grid(row = 1, column = 0)
button5.grid(row = 1, column = 1) 
 #왼쪽 마우스 버튼 바인딩

window.mainloop()
