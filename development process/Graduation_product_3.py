# -*- coding: utf-8 -*-
import tkinter 
import time
import Smart_File
import wifi
import voice
import os

voice_flags = dict()
toggle_flag = dict()

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
        if(i == 46):
            if(Shift_flag == 0):
                os.system("mpg321 ./sound/shift.mp3")
            else:
                os.system("mpg321 ./sound/shift_cancel.mp3")
        elif(i == 47):
            os.system("mpg321 ./sound/erase.mp3")
        elif(i == 45):
            os.system("mpg321 ./sound/space.mp3")
        else:
            if(Shift_flag == 0):
                os.system("mpg321 ./sound/"+little_array[i]+".mp3")
                pass
            if(Shift_flag == 1):
                os.system("mpg321 ./sound/"+big_array[i]+".mp3")
                pass
        double_key_flag = 0
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
        
def voice_timmer(key, sound, minute):
    global voice_voice_flags
    if(voice_flags.get(key,0) == 0):
        voice_flags[key] = time.time() 
        os.system("mpg321 ./sound/"+sound+".mp3")
    else:
        if(time.time() - voice_flags.get(key,0) > minute):
            voice_flags[key] = time.time() 
            os.system("mpg321 ./sound/"+sound+".mp3") 
    
def Connect_wifi():
    voice_timmer("wifi","wifi_toplevel",5)
            
def Connect_wifi_double(event):
    global line, text_pw
    wi = tkinter.Toplevel()
    wi.attributes("-fullscreen", True)
    
    def Close(event=None):
        voice_timmer("Close","back",5)

    def Close_double(event=None):
        wi.destroy()
        Shift_flag = 0
        
        
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
            global voice_voice_flags
            if(voice_flags.get("Ins",0) == 0):
                voice_flags["Ins"] = time.time() 
                item = listbox.curselection()
                voice.make_voice_en(str(Wifi_list[index]))
            else:
                if(time.time() - voice_flags.get("Ins",0) > 8):
                    voice_flags["Ins"] = time.time() 
                    voice.make_voice_en(str(Wifi_list[index]))

            #print(Wifi_list[index])
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
    line = 1
    Wifi_list = Search()
    for name in Wifi_list:
       listbox.insert(line, name)
       line = line + 1

    def Retry():
        voice_timmer("Retry","retry",5)
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
    frame_keyboard=tkinter.Frame(wi)#keyboard
    Make_button(frame_keyboard)
    frame_keyboard.pack(side = "right")
    #-----------------------------------------------------------------------

def Word_education():
    voice_timmer("Word","단어학습",5)
    
def Word_education_double(event):
    voice_timmer("demo","데모",5)


def Regist_word():
    voice_timmer("regist","단어등록",5)
    
def Regist_word_double(event):
    voice_timmer("demo","데모",5)
    '''
    regist = tkinter.Toplevel()
    regist.attributes("-fullscreen", True)
    
    def Close(event=None):
        voice_timmer("Close","back",5)

    def Close_double(event=None):
        regist.destroy()   
    regist.bind("<F11>", Close_double)
    '''
def Update():
    voice_timmer("update","업데이트",5)

def Update_double(event):
    #os.system("mpg321 ./sound/데모.mp3")
    try:
        A = fff+123
        #일부러 안되는 코드 집어넣음, 인터넷이 연결안되거나 서버가 연결 됐을때만 실행되는부분
    except:
        voice_timmer("warning","서버경고",7)
        #pass
    '''
    Up = tkinter.Toplevel()
    def Check():
        pass      
    def Check_double(event):
        Up.destroy()
    Up.title("오류")
    Up.geometry("400x240+200+120")
    frame_la = tkinter.Frame(Up)
    label=tkinter.Label(frame_la, text="서버가 닫혀있거나 와이파이가 연결되어있지 않습니다.")
    label.grid(row = 0 , column = 0, pady="3m")
    button_la=tkinter.Button(frame_la, text = "확인", overrelief="solid", height = 1,width=8, command=Check)
    button_la.bind("<Double-Button-1>", Check_double)
    button_la.grid(row = 1 , column = 0, pady="3m")
    frame_la.pack(padx = "3m",pady="15m")
    voice_timmer("warning","서버경고",7)
    '''
  
def Free_study():
    voice_timmer("Free","자율학습", 4)

def Free_study_double(event):
    #voice_timmer("demo","데모",5)
    #------------------------------------------------------------
    free = tkinter.Toplevel()
    free.attributes("-fullscreen", True)
    def Close(event=None):
        voice_timmer("Close","back",5)
    def Close_double(event=None):
        free.destroy()   
    free.bind("<F11>", Close_double)
    
    num = []
    for i in range(0,72):
        num.append(tkinter.IntVar())    
    
    def Sel():
        voice_timmer("Sel","적용",5)
    def Sel_double(event):
        for i in range(0,72):
            print(num[i].get(), end='')
        #임시로 값만 출력하는 함수임
          
    def Map_vos(x):
        global toggle_flag
        if(x[2] <= 17):
            temp = "1"
        elif(x[2] <= 35):
            temp = "2"
        elif(x[2] <= 54):
            temp = "3"
        else:
            temp = "4"
        
        if(toggle_flag.get(temp+str(x[0])+str(x[1]),0) == 0):
            toggle_flag[temp+str(x[0])+str(x[1])] = 1
            os.system("mpg321 ./sound/"+temp+str(x[0])+str(x[1])+".mp3")     
        else:
            toggle_flag[temp+str(x[0])+str(x[1])] = 0
            if(temp == "1"):
                os.system("mpg321 ./sound/5"+str(x[0])+str(x[1])+".mp3")
            elif(temp == "2"):
                os.system("mpg321 ./sound/6"+str(x[0])+str(x[1])+".mp3")
            elif(temp == "3"):
                os.system("mpg321 ./sound/7"+str(x[0])+str(x[1])+".mp3")
            elif(temp == "4"):
                os.system("mpg321 ./sound/8"+str(x[0])+str(x[1])+".mp3")

  
    def Button_in(frame,i):
        for r in range(0,3):
            for c in range(0,6):
                vos = lambda x = [r, c, i] : Map_vos(x)
                tkinter.Checkbutton(frame,
                                    variable=num[i],
                                    bg = "tan",
                                    padx = 0,
                                    pady = 0,
                                    command=vos).grid(row = r, column = c)
                i += 1
        return i
    #------------------------------------------------------------------
    
    ####################################################################
    #frame_dot = tkinter.Frame(free, background = "tan")
    frame_dot = tkinter.Frame(free, background = "tan")
    frame_dot.pack(anchor = 'c',padx = 30, pady = 30)
    #-------------------------------------------------------------------
    frame_up = tkinter.Frame(frame_dot, background = "tan")
    frame_up.pack(side = "top",anchor = 'c',padx = 3, pady = 3,fill="both")

    frame_up_sub1 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub1.pack(side="left",anchor = 'c',padx = 3, pady = 3,fill="both")
    i = 0
    i = Button_in(frame_up_sub1,i)

    frame_up_sub2 = tkinter.Frame(frame_up)
    frame_up_sub2.pack(side="right",anchor = 'c',padx = 3, pady = 3,fill="both")
    i = Button_in(frame_up_sub2,i)
    
    #------------------------------------------------------------------
    frame_down = tkinter.Frame(frame_dot, background = "tan")
    frame_down.pack(side = "bottom",anchor = 'c',padx = 3, pady = 3,fill="both")

    frame_down_sub1 = tkinter.Frame(frame_down)
    frame_down_sub1.pack(side="left",anchor = 'c',padx = 3, pady = 3,fill="both")
    i = Button_in(frame_down_sub1,i)

    frame_down_sub2 = tkinter.Frame(frame_down)
    frame_down_sub2.pack(side="right",anchor = 'c',padx = 3, pady = 3,fill="both")
    i = Button_in(frame_down_sub2,i)
    #-------------------------------------------------------------------

    ####################################################################
    frame_button = tkinter.Frame(free)
    frame_button.pack(anchor = 'c',padx = 30, pady = 10)
    #-------------------------------------------------------------------
    frame_button_r = tkinter.Button(frame_button,
                                    text = "뒤로가기",
                                    overrelief="solid",
                                    height = 1,
                                    width=8,
                                    command=Close)
    frame_button_r.pack(side = "left",anchor = 'c',padx = 3, pady = 3)
    frame_button_r.bind("<Double-Button-1>", Close_double)
    #-------------------------------------------------------------------
    frame_button_l = tkinter.Button(frame_button,
                                    text = "적용",
                                    overrelief="solid",
                                    height = 1,
                                    width=8,
                                    command=Sel)
    frame_button_l.pack(side = "right",anchor = 'c',padx = 3, pady = 3)
    frame_button_l.bind("<Double-Button-1>",Sel_double)
    '''
    frame_mid = tkinter.Frame(free)
    frame_mid.pack(anchor = 'c',padx = 3, pady = 3)
    
    frame_button = tkinter.Frame(free, background = "black")
    frame_button.pack(side = "bottom",anchor = 'c',padx = 3, pady = 3,fill="both")
    '''
    
def Setup():
    voice_timmer("env","환경설정",5)

def Setup_double(event):
    voice_timmer("demo","데모",5)

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
    button1 = tkinter.Button(frame1, text="와이파이 연결",command = Connect_wifi, height = 10, width = 25)
    button1.bind("<Double-Button-1>", Connect_wifi_double)
    button2 = tkinter.Button(frame1, text="단어 학습", command = Word_education, height = 10, width = 25)
    button2.bind("<Double-Button-1>", Word_education_double)
    button3 = tkinter.Button(frame1, text="단어 등록", command = Regist_word, height = 10, width = 25)
    button3.bind("<Double-Button-1>", Regist_word_double)
    button4 = tkinter.Button(frame1, text="업데이트", command = Update, height = 10, width = 25)
    button4.bind("<Double-Button-1>", Update_double)
    button5 = tkinter.Button(frame1, text="자율 학습", command = Free_study, height = 10, width = 25)
    button5.bind("<Double-Button-1>", Free_study_double)
    button6 = tkinter.Button(frame1, text="환경설정", command = Setup, height = 10, width = 25)
    button6.bind("<Double-Button-1>", Setup_double)

    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)
    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2) 
     #왼쪽 마우스 버튼 바인딩
    frame1.pack();
    window.mainloop()
