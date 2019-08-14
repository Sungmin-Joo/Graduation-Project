# -*- coding: utf-8 -*-
import tkinter
import wifi
def Search():
    wifilist = []
    cells = wifi.Cell.all('wlan0')

    for cell in cells:
        cell = str(cell)
        temp = cell.split('=')
        st = temp[1]
        print(st[0:-1])
        wifilist.append(temp[1])
    return wifilist

def Full_screen():
    global window
    window.attributes("-fullscreen",True)
def Full_screen_re():
    global window
    window.attributes("-fullscreen",False)

if __name__ == '__main__':
    # Search WiFi and return WiFi list
    window=tkinter.Tk()
    window.title("Connect wifi")
    window.geometry("400x500+100+100")
    window.resizable(True, True)
    window.config(background = 'yellow',cursor='none')
    window.bind("<F11>", Full_screen())
    window.bind("<Escape>", Full_screen_re())
    label = tkinter.Label(window, text="---- wifi_list ----")
    label.pack()
    
    
    frame1=tkinter.Frame(window)
    scrollbar=tkinter.Scrollbar(frame1)
    scrollbar.pack(side="right", fill="y")
    listbox=tkinter.Listbox(frame1, yscrollcommand = scrollbar.set)
    Wifi_list = Search()
    line = 1
    for name in Wifi_list:
       listbox.insert(line, name)
       line = line + 1

    def retry():
        global line
        for i in range(1,line+1):
            listbox.delete(0)
        
        Wifi_list = Search()
        line = 1
        for name in Wifi_list:
           listbox.insert(line, name)
           line = line + 1    
        print(line)

            
    listbox.pack(side="left")
    
    scrollbar["command"]=listbox.yview
    
    frame1.pack()
    
    count=0
    def countUP():
        global count
        count +=1
        #label.config(text=str(count))
    
    
    frame2=tkinter.Frame(window)
    button1 = tkinter.Button(frame2,text = "검색", overrelief="solid", width=15, command=retry)
    button1.pack(side = "left")
    button2 = tkinter.Button(frame2,text = "접속", overrelief="solid", width=15, command=countUP)
    button2.pack(side = "right")
    frame2.pack()
    
    frame3_ssid=tkinter.Frame(window)
    label_ssid = tkinter.Label(frame3_ssid, text="와이파이 이름 : ")
    label_ssid.pack(side ="left")
    text_ssid = tkinter.Text(frame3_ssid,width = 30,height = 1)
    text_ssid.pack(side = "right")
    frame3_ssid.pack()
    
    frame4_pw=tkinter.Frame(window) 
    label_pw = tkinter.Label(frame4_pw, text="와이파이 암호 : ")
    label_pw.pack(side ="left")
    text_pw = tkinter.Text(frame4_pw,width = 30,height = 1)
    text_pw.pack(side = "right")
    frame4_pw.pack()

    frame5=tkinter.Frame(window) 
    button3 = tkinter.Button(frame5,text = "전체화면", overrelief="solid", width=15, command=Full_screen)
    button3.pack(side = "left")
    button4 = tkinter.Button(frame5,text = "원래대로", overrelief="solid", width=15, command=Full_screen_re)
    button4.pack(side = "right")
    frame5.pack()
        
    window.mainloop()
else:
    print('Func_called - imported') 

