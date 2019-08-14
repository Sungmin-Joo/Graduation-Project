# -*- coding: utf-8 -*-
import tkinter 
import time
import Smart_File
import wifi
import voice
import os
import Adafruit_PCA9685
import RPi.GPIO as GPIO
import speech_recognition as sr
import hbcvt
import gtts
import lim_code as srv
import random
from gtts import gTTS

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)


voice_flags = dict()
toggle_flag = dict()
word_double_flag = 0
Shift_flag = 0
line = 1
double_key_flag = 0
long_click_flag = 0
little_array = ['`','1','2','3','4','5','6','7','8','9','0','-','=',
                'q','w','e','r','t','y','u','i','o','p','[' ,']',
                'a','s','d','f','g','h','j','k','l',';',
                'z','x','c','v','b','n','m',',','.','/','Space','Shift','Erase']
big_array = ['~','!','@','#','$','%','^','&','*','(',')','_','+',
             'Q','W','E','R','T','Y','U','I','O','P','{','}',
             'A','S','D','F','G','H','J','K','L',':',
             'Z','X','C','V','B','N','M','<','>','?','Space','Shift','Erase']


Traffic_route_voice = "/home/pi/dip/sound/traffic/"
Traffic_route_data = "/home/pi/dip/dot_data/traffic/" 
word_trf_list = Smart_File.Find_dir_format(Traffic_route_data,".txt")
word_trf_len = len(word_trf_list)

Manual_route_voice = "/home/pi/dip/sound/manual/"
Manual_route_data = "/home/pi/dip/dot_data/manual/" 
word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")
word_manual_len = len(word_manual_list)

Food_root_voice = "/home/pi/dip/sound/food/"
Food_root_data = "/home/pi/dip/dot_data/food/" 
word_food_list = Smart_File.Find_dir_format(Food_root_data,".txt")
word_food_len = len(word_food_list)

Location_root_voice = "/home/pi/dip/sound/location/"
Location_root_data = "/home/pi/dip/dot_data/location/" 
word_location_list = Smart_File.Find_dir_format(Location_root_data,".txt")
word_location_len = len(word_location_list)

mp3_route = "mpg321 /home/pi/dip/sound/"
mp3_route_regit = "/home/pi/dip/sound/"
agree=['응','어','네','넵','그렇습니다','그래','엉','넹','으응']
r = sr.Recognizer()

    
####################### call lim's code  ########################
kit_list = srv.setup()
srv.clear_all(kit_list)


def word_sheet(root_data,root_sound,word_list,word_len,parent):
    global word_index
    Func_top = tkinter.Toplevel(background = "tan")
    Func_top.geometry("800x480")
    Func_top.attributes("-fullscreen", True)
    word_index = 0 
   
  
    def Map_wrd(x):
        voice_timmer_root(root_sound,x[0],x[0],2)
        data = Smart_File.Read_file(root_data,word_list[x[1]]).split('\n')
        print("-----------------------------------------------")
        print("단어 : " + word_list[x[1]])
        print("글자 수 : " + data[0])
        print("Dot data : " + data[1])
        d_list = []
        for i in data[1]:
            d_list.append(int(i))
        [d_list.append(0) for i in range(72-len(d_list))]
        print(d_list) #확인
        active(d_list,kit_list)
                     
    def make_button(index):
        global Func_frame
        color_flag=1
        if(index != 0):
            Func_frame.destroy()          
        Func_frame = tkinter.Frame(Func_top,background = "tan")
        Func_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)      
        for r in range(3):
            for c in range(7):
                if(color_flag):
                    color_= 'tan1'
                    color_flag=0
                else:
                    color_= 'burlywood1'
                    color_flag=1
                if(index < word_len):
                    wrd = lambda x = [str(word_list[index].replace(".txt","")), index]: Map_wrd(x)
                    word_button = tkinter.Button(Func_frame,
                                        text = str(word_list[index].replace(".txt","")),
                                        overrelief="solid",
                                        height = 5,
                                        width=8,
                                        bg=color_,
                                        command=wrd)
                    word_button.grid(row = r, column = c)
                    index = index + 1
                else:
                    word_button = tkinter.Button(Func_frame,
                                        text = '',
                                        overrelief="solid",
                                        height = 5,
                                        bg=color_,
                                        width=8)
                    word_button.grid(row = r, column = c)
        return index
    def Next(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Next","다음페이지",3)
    def Next_double():
        global long_click_flag, word_index
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        #voice_timmer("Push","버튼눌림",1)
        
        if(word_index < word_len):
            word_index_trf = make_button(word_index_trf)    
            print("다음 페이지 출력하는데 지금은 막아두겠습니다.")
        else:
            voice_timmer("Last","마지막페이지",5)
        long_click_flag = time.time()    
    word_index = make_button(word_index)
     #------뒤로가기랑 초기 화면 다음페이지 으로 부분------
    def Close_top(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
        
    def Close_top_double(event=None):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        voice_timmer("Move","이동완료",1)
        clear_all(kit_list)
        Func_top.destroy()
        long_click_flag = time.time()
    def Initialize(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Initial","초기화면",3)
        
    def Initialize_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        clear_all(kit_list)
        voice_timmer("Move","이동완료",1)
        Func_top.destroy()
        parent.destroy()
            
            
    Func_top.bind("<F11>", Close_top_double)
    frame_sel_exit = tkinter.Frame(Func_top, background = "tan")
    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3,expand=True)
    button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 15,
                             background = 'tan1')
    button1.bind("<Button-1>", Close_top)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 15,
                             background = 'tan1')
    button2.bind("<Button-1>", Initialize)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_sel_exit, text="다음 페이지",command = Next_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 15,
                             background = 'tan1')
    button3.bind("<Button-1>", Next)
    button3.grid(row = 0, column = 2)
   

def Mapping(i):
    #global double_key_flag
    #if(double_key_flag):  
    global text_pw, Shift_flag
    if(i == 46):
        if(Shift_flag == 0):
            Shift_flag = 1
        else:
            Shift_flag = 0
    elif(i == 47):
        text_pw.delete(len(text_pw.get())-1,tkinter.END)
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
            temp = tkinter.Button(Frame,text = 'Space', overrelief="solid",command = key_func,
                                  bg = 'burlywood1', width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=2,column = 11)
        elif(little_array[i] == 'Shift'):
            temp = tkinter.Button(Frame,text = 'Shift', overrelief="solid",command = key_func,
                                  bg = 'burlywood1', width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=3,column = 11)
        elif(little_array[i] == 'Erase'):
            temp = tkinter.Button(Frame,text = 'Erase', overrelief="solid",command = key_func,
                                  bg = 'burlywood1',width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=1,column = 12)
        else:
            temp = tkinter.Button(Frame,text = little_array[i] + '( '+ big_array[i] +' )',
                                  bg = 'burlywood1', overrelief="solid",command = key_func, width=3,repeatdelay=400, repeatinterval=80)
            temp.grid(row=temp_row,column = temp_col)
            temp_col += 1
        temp.bind("<Double-Button-1>", keyboard_double)
        
def voice_timmer(key, sound, minute):
    global voice_voice_flags
    if(voice_flags.get(key,0) == 0):
        voice_flags[key] = time.time() 
        os.system(mp3_route+sound+".mp3")
    else:
        if(time.time() - voice_flags.get(key,0) > minute):
            voice_flags[key] = time.time() 
            os.system(mp3_route+sound+".mp3")

def voice_timmer_root(root, key, sound, minute):
    global voice_voice_flags
    if(voice_flags.get(key,0) == 0):
        voice_flags[key] = time.time() 
        os.system("mpg321 "+root+sound+".mp3")
    else:
        if(time.time() - voice_flags.get(key,0) > minute):
            voice_flags[key] = time.time() 
            os.system("mpg321 "+root+sound+".mp3") 
    
def Connect_wifi(event):
    global long_click_flag
    long_click_flag = time.time()
    print("와이파이연결 음성 출력")
    voice_timmer("Wifi","wifi_toplevel",5)
            
def Connect_wifi_double():
    global line, text_pw, long_click_flag, text_ssid
    if(time.time() - long_click_flag < 2):
        return
    Wifi_list = []
    voice_timmer("Move","이동완료",1) 
    print("이동 음성 출력")
    long_click_flag = time.time()
    wi = tkinter.Toplevel(bg = 'tan', cursor='none')
    wi.geometry("800x480")
    wi.attributes("-fullscreen", True)

    def scroll_voice():
        voice_timmer("Scroll","스크롤",5)
    
    def Close(event=None):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)

    def Close_double(event=None):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        voice_timmer("Move","이동완료",1) 
        long_click_flag = time.time()
        wi.destroy()
        Shift_flag = 0
    

    def Connect_double():
        global text_pw, text_ssid
        voice_timmer("Connecnt_try","접속시도",2)
        
        if(text_ssid.get() == ''):
            voice_timmer("Connecnt_warnning","접속실패",2)
        else:
            flag = 0
            
            wifilist = []
            cells = wifi.Cell.all('wlan0')
            for cell in cells:
                if(cell.ssid==text_ssid.get()):
                    if cell.encrypted:
                        if(cell.encryption_type != 'wpa2'):
                            os.system('sed \'s/ENTER_ID/%s/\' /home/pi/dip/wifi_setting/wpa_supplicant_id_pw.conf > /home/pi/dip/wifi_setting/wpa_supplicant_id.conf' %cell.ssid)
                            os.system('sed \'s/ENTER_PW/%s/\' /home/pi/dip/wifi_setting/wpa_supplicant_id.conf > /home/pi/dip/wifi_setting/wpa_supplicant_pw.conf' %text_pw.get())
                            os.system('sudo cp -p /home/pi/dip/wifi_setting/wpa_supplicant_pw.conf /etc/wpa_supplicant/wpa_supplicant.conf')
                        else:
                            os.system('sudo wpa_passphrase %s %s>> /etc/wpa_supplicant/wpa_supplicant.conf' %(cell.ssid,text_pw.get()))
                    else:
                        os.system('sed \'s/ENTER_ID/%s/\' /home/pi/dip/wifi_setting/wpa_supplicant_only_id.conf > /etc/wpa_supplicant/wpa_supplicant.conf' %text_ssid.get())
                    break
            
            voice_timmer("Connecnt_good","접속성공",2)
            wi.destroy()
   
    

        
        
        
    wi.bind("<F11>", Close_double)
    #------------------------------------top--------------------------------
    frame_top = tkinter.Frame(wi,bg = 'tan')

    frame_back=tkinter.Frame(frame_top,bg = 'burlywood1')#back,id,pw input
    back = tkinter.Button(frame_back,text = "뒤로가기", overrelief="solid", height = 1,width=8,
                          repeatdelay=100,bg = 'burlywood1',
                          repeatinterval=100,command=Close_double)
    back.bind("<Button-1>", Close)
    back.pack()

    frame_back.grid(row=0,column=0)#grid

    frame_idpw=tkinter.Frame(frame_top,bg = 'tan')
    frame_id=tkinter.Frame(frame_idpw,bg = 'tan')
    label_ssid = tkinter.Label(frame_id, text="WiFi_ID : ",width = 10, anchor='e',bg = 'tan')
    label_ssid.pack(side ="left")
    text_ssid = tkinter.Entry(frame_id,width = 30)
    text_ssid.pack(side = "right")
    frame_id.pack()
        
    frame_pw=tkinter.Frame(frame_idpw,bg = 'tan')
    label_pw = tkinter.Label(frame_pw, text="Password : ",width = 10, anchor='e',bg = 'tan')
    label_pw.pack(side ="left")
    text_pw = tkinter.Entry(frame_pw,width = 30)
    text_pw.pack(side = "right")
    frame_pw.pack()
    frame_idpw.grid(row=0,column=1)#grid

    frame_button = tkinter.Frame(frame_top,bg = 'tan')
    button_connect = tkinter.Button(frame_button, text = "접속", overrelief="solid", height = 1,width=8,
                                    bg = 'burlywood1',command=Connect_double)
    button_connect.pack()
    
    frame_button.grid(row=0,column=2)#grid
    
    frame_top.pack(side = "top",expand=1)
    #-----------------------------------------------------------------------
   
    #----------------------------------left---------------------------------
    frame_left = tkinter.Frame(wi,bg = 'tan')
    frame_wifi = tkinter.Frame(frame_left,bg = 'tan')#wifi list
        
    def Ins_double():
        try:
            item = listbox.curselection()
            index = item[0]
            text_ssid.delete(0,30)
            text_ssid.insert(0,Wifi_list[index])
        except:
            voice_timmer("Miss","선택실패",5)
        
    def Search():
        time.sleep(1)
        wifilist = []
        cells = wifi.Cell.all('wlan0')
       
        for cell in cells:
            wifilist.append(cell.ssid)
        return wifilist
    
    scrollbar = tkinter.Scrollbar(frame_wifi, command = scroll_voice,bg = 'tan')#보류
    scrollbar.pack(side="right", fill="y")
    listbox=tkinter.Listbox(frame_wifi, yscrollcommand = scrollbar.set)
    line = 1
    Wifi_list = Search()
    
    for name in Wifi_list:
       listbox.insert(line, name)
       line = line + 1

    def Retry_double():
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
    button_select = tkinter.Button(frame_id_insert, text = "선택", overrelief="solid",
                                   height = 1,width=8, command=Ins_double,
                                   bg = 'burlywood1')
    button_select.pack(side="left")

    button_retry = tkinter.Button(frame_id_insert, text = "다시검색", overrelief="solid",
                                  height = 1,width=8, command=Retry_double,
                                  bg = 'burlywood1')
    button_retry.pack(side="right") 
    
    frame_id_insert.pack()
    frame_under_list.grid(row = 1, column = 0)#grid
    frame_left.pack(side = "left",expand=1)
    #-----------------------------------------------------------------------

    #---------------------------------right---------------------------------
    frame_keyboard=tkinter.Frame(wi, bg = 'tan')#keyboard
    Make_button(frame_keyboard)
    frame_keyboard.pack(side = "right",expand=1)
    #-----------------------------------------------------------------------

def Word_education(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Word","단어학습",5)
    
def Word_education_double():
    global long_click_flag
    if(time.time() - long_click_flag < 3):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()
    #모터 초기화 합시다.
    #voice_timmer("demo","데모",5)
    #------------------------------------------------------------
    Jamo = tkinter.Toplevel(background = "tan", cursor='none')
    Jamo.geometry("800x480")
    Jamo.attributes("-fullscreen", True)
    def Close(event=None):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
    def Close_double(event = None):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        Jamo.destroy()
        
    #------교통수단 파트------
    def Traffic(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Tra","교통수단",3)

    
    def Traffic_double():
        global long_click_flag, word_index_trf, Traffic_frame
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)

        word_sheet(Traffic_route_data,Traffic_route_voice,
                   word_trf_list,word_trf_len,Jamo)
        
    #------음식 파트------
    def Food(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Food","음식",3)
        
    
    def Food_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        word_sheet(Food_root_data,Food_root_voice,
                   word_food_list,word_food_len,Jamo)
        
        
    #------장소 파트------
    def Location(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Loc","장소",3)
        
    def Location_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        word_sheet(Location_root_data,Location_root_voice,
                   word_location_list,word_location_len,Jamo)
 
    def User_word(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("User","사용자지정",3)

    def User_word_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        word_sheet(Manual_route_data,Manual_route_voice,
                   word_manual_list,word_manual_len,Jamo)
        voice_timmer("Move","이동완료",1) 
        

    
        
        
    Jamo.bind("<F11>", Close_double)
    #---------탈것 음식 장소 사용자지정-----------------
    frame_edu = tkinter.Frame(Jamo, background = "tan")
    frame_edu.pack(side = "top", anchor = 'c',padx = 3, pady = 3,expand=True)
    button1 = tkinter.Button(frame_edu, text="교통수단",command = Traffic_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'burlywood1')
    button1.bind("<Button-1>", Traffic)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_edu, text="음식",command = Food_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'tan1')
    button2.bind("<Button-1>", Food)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_edu, text="장소",command = Location_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'burlywood1')
    button3.bind("<Button-1>", Location)
    button3.grid(row = 0, column = 2)

    button4 = tkinter.Button(frame_edu, text="사용자 지정",command = User_word_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'tan1')
    button4.bind("<Button-1>", User_word)
    button4.grid(row = 0, column = 3)

    #뒤로가기 버튼
    
    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")
    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
    button5 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 3, width = 20,
                             background = 'tan3')
    button5.bind("<Button-1>", Close)
    button5.pack()
        

    
def Update():
    voice_timmer("Update","업데이트",5)

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
  
def Free_study(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Free","수동모드", 3)
    #수동모드로 녹음 다시해야됩니다.
    #수동모드랑 단어학습에는 음소거 추가

def Free_study_double():
    global long_click_flag
    if(time.time() - long_click_flag < 2):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()
    #모터 초기화 합시다.
    #voice_timmer("demo","데모",5)
    #------------------------------------------------------------
    free = tkinter.Toplevel(background = "tan", cursor='none')
    free.geometry("800x480")
    free.attributes("-fullscreen", True)
    def Close(event=None):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
    def Close_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        clear_all(kit_list)
        voice_timmer("Move","이동완료",1) 
        free.destroy()
        
    free.bind("<F11>", Close_double)
    
    num = []
    for i in range(0,72):
        num.append(tkinter.IntVar())    
    
    def Sel(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Sel","적용",4)
        
    def Sel_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Select","적용완료",5) 
        d_list = []
                
        for i in range(0,72):
            d_list.append(int(num[i].get()))
            print(num[i].get(), end='')
        active(d_list,kit_list)
          
    def Map_vos(x):
        global toggle_flag
        if(toggle_flag.get(str(x[0])+str(x[1]),0) == 0):
            toggle_flag[str(x[0])+str(x[1])] = 1
            os.system(mp3_route+str(x[0])+str(x[1])+"1.mp3")
        else:
            toggle_flag[str(x[0])+str(x[1])] = 0
            os.system(mp3_route+str(x[0])+str(x[1])+"2.mp3")
        
  
    def Button_in(frame,i,index):
        for r in range(6):
            vos = lambda x = [i,r+1] : Map_vos(x)
            if((r+1) % 2):
                c=0
            else:
                c=1
            tkinter.Checkbutton(frame,
                                variable=num[index],
                                bg = "tan1",
                                padx = 1,
                                pady = 1,
                                command=vos,
                                width = 4,
                                height = 3).grid(row = (r//2), column = c)
            index += 1    
        i += 1
        return i, index
    #------------------------------------------------------------------
    
    ####################################################################
    #frame_dot = tkinter.Frame(free, background = "tan")
    frame_dot = tkinter.Frame(free, background = "tan")
    frame_dot.pack(anchor = 'c',padx = 3, pady = 3)
    #--------------------------top---------------------------------
    frame_up = tkinter.Frame(frame_dot, background = "tan")
    frame_up.pack(side = "top",anchor = 'c',padx = 3, pady = 3,fill="both",expand=True)
    i = 1
    index = 0
    
    frame_up_sub1 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub1.grid(row = 0, column = 0, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub1,i, index)
    
    frame_up_sub2 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub2.grid(row = 0, column = 1, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub2,i, index)

    frame_up_sub3 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub3.grid(row = 0, column = 2, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub3,i, index)

    frame_up_sub4 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub4.grid(row = 0, column = 3, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub4,i, index)

    frame_up_sub5 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub5.grid(row = 0, column = 4, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub5,i, index)

    frame_up_sub6 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub6.grid(row = 0, column = 5, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub6,i, index)
    #-------------------------------------------------------------------
    
    
    #------------------------bottom-----------------------------
    frame_down = tkinter.Frame(frame_dot, background = "tan")
    frame_down.pack(side = "bottom",anchor = 'c',padx = 3, pady = 3,fill="both")

    frame_up_sub7 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub7.grid(row = 1, column = 0, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub7,i, index)
    
    frame_up_sub8 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub8.grid(row = 1, column = 1, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub8,i, index)

    frame_up_sub9 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub9.grid(row = 1, column = 2, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub9,i, index)

    frame_up_sub10 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub10.grid(row = 1, column = 3, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub10,i, index)

    frame_up_sub11 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub11.grid(row = 1, column = 4, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub11,i, index)

    frame_up_sub12 = tkinter.Frame(frame_up, background = "tan")
    frame_up_sub12.grid(row = 1, column = 5, ipadx = 4, ipady = 3)
    i, index = Button_in(frame_up_sub12,i, index)
    
    
    ####################################################################
    frame_button = tkinter.Frame(free, background = "tan")
    frame_button.pack(anchor = 'c',padx = 30, pady = 10,expand=True)
    #-------------------------------------------------------------------
    frame_button_r = tkinter.Button(frame_button,
                                    text = "뒤로가기",
                                    overrelief="solid",
                                    height = 2,
                                    width=10,
                                    repeatdelay=100,
                                    repeatinterval=100,
                                    background = "burlywood1",
                                    command=Close_double)
    frame_button_r.pack(side = "left",anchor = 'c',padx = 3, pady = 3,expand=True)
    frame_button_r.bind("<Button-1>", Close)
    #-------------------------------------------------------------------
    frame_button_l = tkinter.Button(frame_button,
                                    text = "적용",
                                    overrelief="solid",
                                    height = 2,
                                    width=10,
                                    command=Sel_double,
                                    repeatdelay=100,
                                    repeatinterval=100,
                                    background = "burlywood1")
    frame_button_l.pack(side = "right",anchor = 'c',padx = 3, pady = 3,expand=True)
    frame_button_l.bind("<Button-1>",Sel)

  
def jamo_edu(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Jamo","자모학습",3)

def jamo_edu_double():
    global long_click_flag
    if(time.time() - long_click_flag < 3):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()
    #모터 초기화 합시다.
    #voice_timmer("demo","데모",5)
    #------------------------------------------------------------
    Jamo = tkinter.Toplevel(background = "tan", cursor='none')
    Jamo.geometry("800x480")
    Jamo.attributes("-fullscreen", True)
    
    def Close(event=None):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
    def Close_double(event = None):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        Jamo.destroy()
    Jamo.bind("<F11>", Close_double)
    
    def Chosung(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Cho","초성",3)
    
    #------초성 파트------
    def Chosung_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Chosung = tkinter.Toplevel(background = "tan")
        Chosung.geometry("800x480")
        Chosung.attributes("-fullscreen", True)
        cho_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','된소리']
        cho_val = [[0,1,0,0,0,0],
                   [1,1,0,0,0,0],
                   [0,1,1,0,0,0],
                   [0,0,0,1,0,0],
                   [1,0,0,1,0,0],
                   [0,1,0,1,0,0],
                   [0,0,0,0,0,1],
                   [0,1,0,0,0,1],
                   [0,0,0,1,0,1],
                   [1,1,1,0,0,0],
                   [1,0,1,1,0,0],
                   [1,1,0,1,0,0],
                   [0,1,1,1,0,0],
                   [0,0,0,0,0,1]]
        
        cho_frame = tkinter.Frame(Chosung,background = "red")
        cho_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)
        cho_index = 0

        def Map_act(x):
            voice_timmer("Cho_"+str(x), cho_list[x], 2)
            d_list = []
            for i in cho_val[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            print(d_list) #확인
            active(d_list,kit_list)
        
        for x in range(2):
            for y in range(7):
                act = lambda x = cho_index : Map_act(x)
                if(cho_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(cho_frame,text = cho_list[cho_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = 7,
                                width = 10,
                                command = act).grid(row = (x), column = y)
                cho_index += 1
                

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)
            
        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1) 
            Chosung.destroy()
            long_click_flag = time.time()

        def Initialize(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Initial","초기화면",3)
            
        def Initialize_double():
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            long_click_flag = time.time()
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1)
            Chosung.destroy()
            Jamo.destroy()
            
            
        Chosung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left");

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right");

        

    def Moum(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Moum","모음",3)
        
    #------모음 파트------
    def Moum_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Chosung = tkinter.Toplevel(background = "tan")
        Chosung.geometry("800x480")
        Chosung.attributes("-fullscreen", True)
        cho_list = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅔ','ㅚ','ㅘ',
                    'ㅝ','ㅢ','ㅖ','ㅟ','ㅒ','ㅙ','ㅞ']
        cho_val = [[1,0,1,0,0,1],
                   [0,1,0,1,1,0],
                   [0,1,1,0,1,0],
                   [1,0,0,1,0,1],
                   [1,0,0,0,1,1],
                   [0,1,0,1,0,0],
                   [0,1,0,0,1,1],
                   [1,1,0,0,1,0],
                   [1,1,0,0,0,1],
                   [0,1,1,0,0,1],
                   [1,0,0,1,1,0],
                   [1,0,1,1,1,0],
                   [1,1,0,1,1,0],
                   [1,1,0,1,1,1],
                   [1,0,1,0,1,1],
                   [1,1,1,0,1,0],
                   [0,1,1,1,0,1],
                   [0,1,0,0,1,0],
                   [1,1,0,0,1,0,1,0,1,1,1,0],
                   [0,1,0,1,1,0,1,0,1,1,1,0],
                   [1,0,1,0,1,1,1,0,1,1,1,0],
                   [1,1,1,0,1,0,1,0,1,1,1,0]]
        
        cho_frame = tkinter.Frame(Chosung,background = "red")
        cho_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)
        cho_index = 0

        def Map_act(x):
            voice_timmer("Cho_"+str(x), cho_list[x], 2)
            d_list = []
            for i in cho_val[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            print(d_list) #확인
            active(d_list,kit_list)
            print(cho_val[x])
        
        for x in range(3):
            for y in range(7):
                act = lambda x = cho_index : Map_act(x)
                if(cho_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(cho_frame,text = cho_list[cho_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = 5,
                                width = 10,
                                command = act).grid(row = (x), column = y)
                cho_index += 1
                

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)
            
        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1) 
            Chosung.destroy()
            long_click_flag = time.time()

        def Initialize(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Initial","초기화면",3)
            
        def Initialize_double():
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            long_click_flag = time.time()
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1)
            Chosung.destroy()
            Jamo.destroy()
            
            
        Chosung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left")

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right")
        
    
    def jongsung(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Jong","종성",3)
        
    def jongsung_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Chosung = tkinter.Toplevel(background = "tan")
        Chosung.geometry("800x480")
        Chosung.attributes("-fullscreen", True)
        cho_list = ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ']
        cho_val = [[1,0,0,0,0,0],
                   [0,0,1,1,0,0],
                   [0,0,0,1,1,0],
                   [0,0,1,0,0,0],
                   [0,0,1,0,0,1],
                   [1,0,1,0,0,0],
                   [0,0,0,0,1,0],
                   [0,0,1,1,1,1],
                   [1,0,0,0,1,0],
                   [0,0,1,0,1,0],
                   [0,0,1,1,1,0],
                   [0,0,1,0,1,1],
                   [0,0,1,1,0,0],
                   [0,0,0,1,1,1]]
        
        cho_frame = tkinter.Frame(Chosung,background = "red")
        cho_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)
        cho_index = 0

        def Map_act(x):
            voice_timmer("Cho_"+str(x), cho_list[x], 2)
            d_list = []
            for i in cho_val[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            print(d_list) #확인
            active(d_list,kit_list)
            print(cho_val[x])
        
        for x in range(2):
            for y in range(7):
                act = lambda x = cho_index : Map_act(x)
                if(cho_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(cho_frame,text = cho_list[cho_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = 7,
                                width = 10,
                                command = act).grid(row = (x), column = y)
                cho_index += 1
                

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)
            
        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1) 
            Chosung.destroy()
            long_click_flag = time.time()

        def Initialize(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Initial","초기화면",3)
            
        def Initialize_double():
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            long_click_flag = time.time()
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1)
            Chosung.destroy()
            Jamo.destroy()
            
            
        Chosung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left");

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right")
    
    def simple_h1(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Simple","1종약자",3)

    def simple_h1_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Chosung = tkinter.Toplevel(background = "tan")
        Chosung.geometry("800x480")
        Chosung.attributes("-fullscreen", True)
        cho_list = ['가','나','다','마','바','사','자','카','타','파','하','것','ㅆ',
                    '억','언','얼','연','열','영','옥','온','옹','운','울','은','을','인']
        cho_val = [[1,1,1,0,0,1],
                   [1,1,0,0,0,0],
                   [0,1,1,0,0,0],
                   [1,0,0,1,0,0],
                   [0,1,0,1,0,0],
                   [1,0,1,0,1,0],
                   [0,1,0,0,0,1],
                   [1,1,1,0,0,0],
                   [1,0,1,1,0,0],
                   [1,1,0,1,0,0],
                   [0,1,1,1,0,0],
                   [0,1,0,1,0,1,0,1,1,0,1,0],
                   [0,1,0,0,1,0],
                   [1,1,0,1,0,1],
                   [0,1,1,1,1,1],
                   [0,1,1,1,1,0],
                   [1,0,0,0,0,1],
                   [1,0,1,1,0,1],
                   [1,1,1,1,0,1],
                   [1,1,0,0,1,1],
                   [1,0,1,1,1,1],
                   [1,1,1,1,1,1],
                   [1,1,1,1,0,0],
                   [1,1,1,0,1,1],
                   [1,0,0,1,1,1],
                   [0,1,1,0,1,1],
                   [1,1,1,1,1,0]]
        
        cho_frame = tkinter.Frame(Chosung,background = "tan")
        cho_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)
        cho_index = 0

        def Map_act(x):
            voice_timmer("Cho_"+str(x), cho_list[x], 2)
            d_list = []
            for i in cho_val[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            print(d_list) #확인
            active(d_list,kit_list)
            print(cho_val[x])
        
        for x in range(3):
            for y in range(9):
                if(cho_index>=26):
                    break
                act = lambda x = cho_index : Map_act(x)
                if(cho_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(cho_frame,text = cho_list[cho_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = 7,
                                width = 10,
                                command = act).grid(row = (x), column = y)
                cho_index += 1
                

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)
            
        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1) 
            Chosung.destroy()
            long_click_flag = time.time()

        def Initialize(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Initial","초기화면",3)
            
        def Initialize_double():
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            long_click_flag = time.time()
            voice_timmer("Move","이동완료",1)
            Chosung.destroy()
            Jamo.destroy()
            
            
        Chosung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left");

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right")
    
    def simple_h2(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Simple","2종약자",3)

    def simple_h2_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Chosung = tkinter.Toplevel(background = "tan")
        Chosung.geometry("800x480")
        Chosung.attributes("-fullscreen", True)
        cho_list = ['그래서','그러나','그러면','그러므로','그런데','그리고']
        cho_val = [[1,0,0,0,0,0,0,1,1,0,1,0],
                   [1,0,0,0,0,0,1,1,0,0,0,0],
                   [1,0,0,0,0,0,0,0,1,1,0,0],
                   [1,0,0,0,0,0,0,0,1,0,0,1],
                   [1,0,0,0,0,0,1,1,0,1,1,0],
                   [1,0,0,0,0,0,1,0,0,0,1,1]]
        
        cho_frame = tkinter.Frame(Chosung,background = "tan")
        cho_frame.pack(side = "top", anchor = 'c',padx = 10, pady = 3,expand=True)
        cho_index = 0

        def Map_act(x):
            voice_timmer("Cho_"+str(x), cho_list[x], 2)
            d_list = []
            for i in cho_val[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            print(d_list) #확인
            active(d_list,kit_list)
            print(cho_val[x])
        
        for x in range(2):
            for y in range(3):
                act = lambda x = cho_index : Map_act(x)
                if(cho_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(cho_frame,text = cho_list[cho_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = 10,
                                width = 15,
                                command = act).grid(row = (x), column = y)
                cho_index += 1
                

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)
            
        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            voice_timmer("Move","이동완료",1) 
            Chosung.destroy()
            long_click_flag = time.time()

        def Initialize(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Initial","초기화면",3)
            
        def Initialize_double():
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            clear_all(kit_list)
            long_click_flag = time.time()
            voice_timmer("Move","이동완료",1)
            Chosung.destroy()
            Jamo.destroy()
            
            
        Chosung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left");

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 15,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right")
        
        
    Jamo.bind("<F11>", Close_double)
    #---------초성 모음 종성 약자 -----------------
    frame_edu = tkinter.Frame(Jamo, background = "tan")
    frame_edu.pack(side = "top", anchor = 'c',padx = 3, pady = 3,expand=True)
    button1 = tkinter.Button(frame_edu, text="초성",command = Chosung_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'burlywood1')
    button1.bind("<Button-1>", Chosung)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_edu, text="모음",command = Moum_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'tan1')
    button2.bind("<Button-1>", Moum)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_edu, text="종성",command = jongsung_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'burlywood1')
    button3.bind("<Button-1>", jongsung)
    button3.grid(row = 0, column = 2)

    button4 = tkinter.Button(frame_edu, text="1종 약자",command = simple_h1_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'tan1')
    button4.bind("<Button-1>", simple_h1)
    button4.grid(row = 0, column = 3)

    button5 = tkinter.Button(frame_edu, text="2종 약자",command = simple_h2_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 16, width = 18,
                             background = 'burlywood1')
    button5.bind("<Button-1>", simple_h2)
    button5.grid(row = 0, column = 4)

    #뒤로가기 버튼
    
    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")
    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)
    button5 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 3, width = 20,
                             background = 'tan3')
    button5.bind("<Button-1>", Close)
    button5.pack();
    
    #voice_timmer("demo","데모",5)

def Regist_word(event):
    global long_click_flag
    long_click_flag = time.time() 
    voice_timmer("Regist","단어등록",5)
    #사용자 단어는 업데이트해도 안 없어지게 짜야한다.
    
def Regist_word_double():
    global long_click_flag
    if(time.time() - long_click_flag < 2):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()
    #모터 초기화 합시다.
    #------------------------------------------------------------
    Regist = tkinter.Toplevel(background = "tan", cursor='none')
    Regist.geometry("800x480")
    Regist.attributes("-fullscreen", True)
    
    def Close(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
        
    def Close_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        Regist.destroy()
    Regist.bind("<F11>", Close_double)

    def choose_save(data, length, data_ko):
        global word_manual_list, word_manual_len
        time.sleep(0.5)
        os.system(mp3_route+"저장여부.mp3")
        while 1:
            try:
                with sr.Microphone() as source:
                    audio = r.listen(source)
                string = r.recognize_google(audio,language='ko_KO')
                string=string.replace(" ","")
                if string in agree:
                    os.system(mp3_route+"단어저장중.mp3")
                    f=open(Manual_route_data+data_ko+'.txt','w')
                    f.write(str(length)+'\n')
                    for _ in data:
                        f.write(str(_))
                    f.close()
                    tts = gTTS(text=data_ko, lang='ko')
                    tts.save(Manual_route_voice+data_ko+".mp3")
                    os.system(mp3_route+"저장성공.mp3")
                    word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")
                    word_manual_len = len(word_manual_list)
                else:
                    os.system(mp3_route+"저장실패.mp3")
                break
            except:
                os.system(mp3_route+"다시말해주세요.mp3")

        
    def Regit_word(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Regit","단어등록시작",3)
        
    def Regit_word_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        
        os.system(mp3_route+"음성입력전.mp3")
        with sr.Microphone() as source:
            audio = r.listen(source)

        os.system(mp3_route+"음성입력후.mp3")
        #입력 단어 분석
        try:
            string = r.recognize_google(audio,language='ko_KO')
            data = hbcvt.h2b.text(string.replace(" ",""))
            cnt=0
            dot_data=[]
            for i in data:
                for j in i:
                    for z in j:
                        for x in z:
                            for a in x:
                                if(type(a)==list):
                                    cnt+=a.count(1) + a.count(0)
                                    for b in a:
                                        dot_data.append(b)
            if(cnt>72):
                os.system(mp3_route+"음성입력제한.mp3")
                print(cnt)

            else:
                print("text: "+ string)
                print(cnt)
                tts = gTTS(text="입력된 단어는 "+ string + " 입니다.", lang='ko')
                tts.save(mp3_route_regit+"음성결과임시.mp3")
                os.system(mp3_route+"음성결과임시.mp3")
                choose_save(dot_data,len(string.replace(" ","")),string)
                print(dot_data)
        except:
            os.system(mp3_route+"단어분석실패.mp3")
            

    #뒤로가기, 단어등록 버튼
    
    frame_sel_exit = tkinter.Frame(Regist, background = "tan")
    frame_sel_exit.pack(anchor = 'c',expand=True)
    button_back = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 50,
                             background = 'tan1')
    button_back.bind("<Button-1>", Close)

    button_regist = tkinter.Button(frame_sel_exit, text="단어등록 시작",command = Regit_word_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 50,
                             background = 'burlywood1')
    button_regist.bind("<Button-1>", Regit_word)
    
    button_back.pack(side='left');
    button_regist.pack(side='right');

    
def exit_(event):
    global long_click_flag
    long_click_flag = time.time() 
    voice_timmer("Exit","사용종료",3)

def exit_double():
    global long_click_flag,window
    if(time.time() - long_click_flag < 3):
        return
    voice_timmer("Exit_true","사용을종료합니다",3)
    window.destroy()
    #clear_all(kit_list)
    long_click_flag = time.time()
    #motor 다 내리기
    #os.~~~ exit
def quiz(event):
    global long_click_flag
    long_click_flag = time.time() 
    voice_timmer("Quiz","퀴즈",2.5)

def quiz_double():
    global long_click_flag, now_data_k, now_data_b, now_voice_route
    if(time.time() - long_click_flag < 2):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()

    
    #모터 초기화 합시다.
    #------------------------------------------------------------
    Quiz = tkinter.Toplevel(background = "tan", cursor='none')
    Quiz.geometry("800x480")
    Quiz.attributes("-fullscreen", True)
    
    
    def Close(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",3)
        
    def Close_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        #초기화
        Quiz.destroy()
    Quiz.bind("<F11>", Close_double)

    
    def make_quize():
        num = random.randrange(1,4)
        if num == 1:
            q_d_route = Traffic_route_data
            q_v_route = Traffic_route_voice
            q_list = word_trf_list
        elif num == 2:
            q_d_route = Food_root_data
            q_v_route = Food_root_voice
            q_list = word_food_list
        else:
            q_d_route = Location_root_data
            q_v_route = Location_root_voice 
            q_list = word_location_list

        q_len = len(q_list)
        num = random.randrange(0,q_len)
        r_k_data = q_list[num]
        rand_data = Smart_File.Read_file(q_d_route,r_k_data).split('\n')
        print("-----------------------------------------------")
        print("단어 : " + r_k_data)
        print("글자 수 : " + rand_data[0])
        print("Dot data : " + rand_data[1])
        d_list = []
        for i in rand_data[1]:
            d_list.append(int(i))
        [d_list.append(0) for i in range(72-len(d_list))]
        print(d_list)
        print("점자 출력하는 부분")
        return r_k_data.replace('.txt',''), d_list, q_v_route

    now_data_k, now_data_b, now_voice_route = make_quize()
    
    def next_q(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Quiz_n","다음문제",2)
    
    def next_q_double():
        global long_click_flag, now_data_k, now_data_b, now_voice_route
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Quiz_re","문제갱신",2)
        now_data_k, now_data_b, now_voice_route = make_quize()


    def answer(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Quiz_a","정답말하기",3)
    
    def answer_double():
        global long_click_flag, now_data_k, now_data_b, now_voice_route
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        
        os.system(mp3_route+"음성입력전.mp3")
        with sr.Microphone() as source:
            audio = r.listen(source)

        os.system(mp3_route+"음성입력후.mp3")
        #입력 단어 분석
        try:
            string = r.recognize_google(audio,language='ko_KO')
            print(string.replace(' ',''),now_data_k.replace(' ',''))
            if string.replace(' ','') == now_data_k.replace(' ',''):
                os.system(mp3_route+"문제정답.mp3")
                now_data_k, now_data_b, now_voice_route = make_quize()
            else:
                os.system(mp3_route+"문제오답.mp3")
        
        except:
            os.system(mp3_route+"단어분석실패.mp3")
        

    def confirm(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Quiz_c","정답확인",3)

    def confirm_double():
        global long_click_flag, now_data_k, now_voice_route
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        os.system(mp3_route+"정답은.mp3")
        os.system('mpg321 '+now_voice_route+now_data_k+".mp3")
        os.system(mp3_route+"입니다.mp3")
    
    
    
    frame_sel_exit = tkinter.Frame(Quiz, background = "tan")
    frame_sel_exit.pack(anchor = 'c',expand=True)
    button_back = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 25,
                             background = 'tan1')
    button_back.bind("<Button-1>", Close)

    button_answer = tkinter.Button(frame_sel_exit, text="정답 말하기",command = answer_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 25,
                             background = 'burlywood1')
    button_answer.bind("<Button-1>", answer)

    button_confirm = tkinter.Button(frame_sel_exit, text="정답 확인",command = confirm_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 25,
                             background = 'tan1')
    button_confirm.bind("<Button-1>", confirm)

    button_next_q = tkinter.Button(frame_sel_exit, text="다음 문제",command = next_q_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 25, width = 25,
                             background = 'burlywood1')
    button_next_q.bind("<Button-1>", next_q)
    
    button_back.pack(side='left');
    button_next_q.pack(side='right');
    button_confirm.pack(side='right');
    button_answer.pack(side='right');
    

if __name__ == '__main__':
    global window
    #os.system("python3 ~/dip/logo.py")
    
    window=tkinter.Tk()
    window.title("Graduation Project")
    window.geometry("800x480")


    window.configure(background='gray60', cursor='none')
    window.attributes("-fullscreen", True)



    
 
    #window.configure(background='tan')    
    #최초 실행시 모터 초기화 및 각도세팅
    #window.resizable(False, False)
    #frame = Frame(window, width=600, height=300)

    def toggle_fullscreen(event=None):
        window.state = not window.state  # Just toggling the boolean
        window.attributes("-fullscreen", window.state)
        return "break"    
    window.bind("<F11>", toggle_fullscreen)

    frame1=tkinter.Frame(window,background="gray60")
    button1 = tkinter.Button(frame1, text="와이파이 연결",command = Connect_wifi_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = 'thistle4')
    button1.bind("<Button-1>", Connect_wifi)
    button2 = tkinter.Button(frame1, text="단어 학습", command = Word_education_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = "thistle3")

    button2.bind("<Button-1>", Word_education)

    button3 = tkinter.Button(frame1, text="자음,모음 및 약자 학습", command = jamo_edu_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = 'thistle4')
    button3.bind("<Button-1>", jamo_edu)
    
    button4 = tkinter.Button(frame1, text="업데이트",bg = 'thistle3',
                             command = Update,
                             relief = 'solid', height = 12, width = 22)
    button4.bind("<Double-Button-1>", Update_double)
    
    button5 = tkinter.Button(frame1, text="수동 모드", command = Free_study_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = "thistle4")
    button5.bind("<Button-1>", Free_study)
    
    button6 = tkinter.Button(frame1, text="단어 등록",command = Regist_word_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = 'thistle3')
    button6.bind("<Button-1>", Regist_word)
    
    button7 = tkinter.Button(frame1, text="사용 종료", command = exit_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = "thistle3")

    button7.bind("<Button-1>", exit_)

    button8 = tkinter.Button(frame1, text="문제풀기", command = quiz_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 12, width = 22,
                             relief = 'solid',
                             background = "thistle4")

    button8.bind("<Button-1>", quiz)

    
    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)
    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2)

    button7.grid(row = 0, column = 3)
    button8.grid(row = 1, column = 3)
     #왼쪽 마우스 버튼 바인딩
    frame1.pack(expand=True);
    window.mainloop()
    
