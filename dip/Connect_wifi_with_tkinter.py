# -*- coding: utf-8 -*-
import tkinter 
import time
import Smart_File
import wifi

Shift_flag = 0
line = 1
double_key_flag = 0
little_array = ['`','1','2','3','4','5','6','7','8','9','0','-','=',
                'q','w','e','r','t','y','u','i','o','p','[' ,']',
                'a','s','d','f','g','h','j','k','l',';',
                'z','x','c','v','b','n','m',',','.','/','Space','Shift','Erase']
big_array = ['~','!','@','#','$','%','^','&','*','(',')','_','+',
             'Q','W','E','R','T','Y','U','I','O','P','{','}',
             'A','S','D','F','G','H','J','K','L',':',
             'Z','X','C','V','B','N','M','<','>','?','Space','Shift','Erase']
def Mapping(i):
    global double_key_flag
    if(double_key_flag):  
        global text_pw, Shift_flag
        if(i == 46):
            if(Shift_flag == 0):
                Shift_flag = 1
            else:
                Shift_flag = 0
        elif(i == 47):
            text_pw.delete(len(target.get())-1,tkinter.END)
            Shift_flag = 0
        elif(i == 45):
            text_pw.insert(tkinter.END," ")
            Shift_flag = 0
        else:
            if(Shift_flag == 0):
                text_pw.insert(tkinter.END,little_array[i])
            if(Shift_flag == 1):
                text_pw.insert(tkinter.END,big_array[i])
                Shift_flag = 0
        double_key_flag = 0
    else:
        print("키값에 해당하는 음성출력")

def keyboard_double(event):
    global double_key_flag
    double_key_flag = 1
    
def Make_button(Frame):
    temp_row = 0
    temp_col = 0
    for i in range(0,48):
        key_func = lambda x = i : Mapping(x)
        #Use lambda to mapping each button
        if(little_array[i] == 'q' or little_array[i] == 'a' or little_array[i] == 'z'):
            temp_row +=1
            if(temp_row >= 2):
                temp_col = 1
            else:
                temp_col = 0
        if(little_array[i] == 'Space'):
            temp = tkinter.Button(Frame,text = 'Space', overrelief="solid",command = key_func, width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=2,column = 11)
        elif(little_array[i] == 'Shift'):
            temp = tkinter.Button(Frame,text = 'Shift', overrelief="solid",command = key_func, width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=3,column = 11)
        elif(little_array[i] == 'Erase'):
            temp = tkinter.Button(Frame,text = 'Erase', overrelief="solid",command = key_func, width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=1,column = 12)
        else:
            temp = tkinter.Button(Frame,text = little_array[i] + '( '+ big_array[i] +' )', overrelief="solid",command = key_func, width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=temp_row,column = temp_col)
            temp_col += 1
        temp.bind("<Double-Button-1>", keyboard_double) 
            
def Connect_wifi():
    print("와이파이 연결 음성 출력")
    
def Connect_wifi_double(event):
    global line, text_pw
    wi = tkinter.Toplevel()
    wi.state = True
    wi.attributes("-fullscreen", wi.state)
    
    def Close(event=None):
        print("뒤로 가기 음성 출력")
        
    def Close_double(event=None):
        wi.destroy()
        Shift_flag = 0
        line = 1
        
    wi.bind("<F11>", Close_double)
    #------------------------------------top--------------------------------
    frame_top = tkinter.Frame(wi)

    frame_back=tkinter.Frame(frame_top)#back,id,pw input
    back = tkinter.Button(frame_back,text = "뒤로가기", overrelief="solid", height = 1,width=8, command=Close)
    back.bind("<Double-Button-1>", Close_double)
    back.pack()

    frame_back.grid(row=0,column=0)#grid

    frame_idpw=tkinter.Frame(frame_top)
    frame_id=tkinter.Frame(frame_idpw)
    label_ssid = tkinter.Label(frame_id, text="WiFi_ID : ",width = 10, anchor='e')
    label_ssid.pack(side ="left")
    text_ssid = tkinter.Entry(frame_id,width = 30)
    text_ssid.pack(side = "right")
    frame_id.pack()
        
    frame_pw=tkinter.Frame(frame_idpw)
    label_pw = tkinter.Label(frame_pw, text="Password : ",width = 10, anchor='e')
    label_pw.pack(side ="left")
    text_pw = tkinter.Entry(frame_pw,width = 30)
    text_pw.pack(side = "right")
    frame_pw.pack()
    frame_idpw.grid(row=0,column=1)#grid

    frame_button = tkinter.Frame(frame_top)
    button_connect = tkinter.Button(frame_button, text = "접속", overrelief="solid", height = 1,width=8, command=Close)
    button_connect.pack()
    button_connect.bind("<Double-Button-1>", Close_double)
    frame_button.grid(row=0,column=2)#grid
    
    frame_top.pack(side = "top")
    #-----------------------------------------------------------------------
   
    #----------------------------------left---------------------------------
    frame_left = tkinter.Frame(wi)
    
    frame_wifi = tkinter.Frame(frame_left)#wifi list
    def Ins():
        try:
            item = listbox.curselection()
            index = item[0]
            print(Wifi_list[index])
        except:
            pass
        
    def Ins_double(event):
        try:
            item = listbox.curselection()
            index = item[0]
            text_ssid.delete(0,30)
            text_ssid.insert(0,Wifi_list[index])
        except:
            pass
        
    def Search():
        wifilist = []
        cells = wifi.Cell.all('wlan0')

        for cell in cells:
            cell = str(cell)
            temp = cell.split('=')
            st = temp[1]
            wifilist.append(st[0:-1])
        return wifilist
    scrollbar = tkinter.Scrollbar(frame_wifi)
    
    scrollbar.pack(side="right", fill="y")
    listbox=tkinter.Listbox(frame_wifi, yscrollcommand = scrollbar.set)
    Wifi_list = Search()
    for name in Wifi_list:
       listbox.insert(line, name)
       line = line + 1

    def Retry():
        print("다시검색 하기")
    def Retry_double(event):
        global line
        for i in range(1,line+1):
            listbox.delete(0)
        
        Wifi_list = Search()
        line = 1
        for name in Wifi_list:
           listbox.insert(line, name)
           line = line + 1
        
    listbox.pack(side="left")
    scrollbar["command"]=listbox.yview
    
    frame_wifi.grid(row = 0, column = 0)#grid

    frame_under_list = tkinter.Frame(frame_left)
    frame_id_insert = tkinter.Frame(frame_under_list)
    button_select = tkinter.Button(frame_id_insert, text = "선택", overrelief="solid", height = 1,width=8, command=Ins)
    button_select.pack(side="left")
    button_select.bind("<Double-Button-1>", Ins_double)
    button_retry = tkinter.Button(frame_id_insert, text = "다시검색", overrelief="solid", height = 1,width=8, command=Retry)
    button_retry.pack(side="right")
    button_retry.bind("<Double-Button-1>", Retry_double)
    frame_id_insert.pack()
    frame_under_list.grid(row = 1, column = 0)#grid
    frame_left.pack(side = "left")
    #-----------------------------------------------------------------------
    #---------------------------------right---------------------------------
    frame_keyboard=tkinter.Frame(wi,padx = 80)#keyboard
    Make_button(frame_keyboard)
    frame_keyboard.pack(side = "right")
    #-----------------------------------------------------------------------

def Word_education():
    pass

def Regist_word():
    pass

def Update():
    pass

def Free_study():
    pass

def Setup():
    pass

if __name__ == '__main__':
    window=tkinter.Tk()
    window.title("Graduation Project")
    window.geometry("640x400+100+100")
    window.resizable(False, False)
    #frame = Frame(window, width=600, height=300)
    frame1=tkinter.Frame(window)
    button1 = tkinter.Button(frame1, text="와이파이 연결",command = Connect_wifi, height = 10, width = 25)
    button1.bind("<Double-Button-1>", Connect_wifi_double)
    button2 = tkinter.Button(frame1, text="단어 학습", command = Word_education, height = 10, width = 25)
    button3 = tkinter.Button(frame1, text="단어 등록", command = Regist_word, height = 10, width = 25)
    button4 = tkinter.Button(frame1, text="업데이트", command = Update, height = 10, width = 25)
    button5 = tkinter.Button(frame1, text="자율학습", command = Free_study, height = 10, width = 25)
    button6 = tkinter.Button(frame1, text="환경설정", command = Setup, height = 10, width = 25)
    
    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)
    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2) 
     #왼쪽 마우스 버튼 바인딩
    frame1.pack();
    window.mainloop()
