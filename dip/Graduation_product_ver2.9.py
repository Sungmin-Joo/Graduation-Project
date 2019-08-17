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

import down_module as dm

import pyautogui

from gtts import gTTS

from tkinter import messagebox as mb

 

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)

 

wifi_flag=0

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

 

 

Food_root_voice = "/home/pi/dip/sound/food/"

Food_root_data = "/home/pi/dip/dot_data/food/" 

word_food_list = Smart_File.Find_dir_format(Food_root_data,".txt")

word_food_len = len(word_food_list)

 

Location_root_voice = "/home/pi/dip/sound/location/"

Location_root_data = "/home/pi/dip/dot_data/location/" 

word_location_list = Smart_File.Find_dir_format(Location_root_data,".txt")

word_location_len = len(word_location_list)

 

Traffic_route_voice = "/home/pi/dip/sound/traffic/"

Traffic_route_data = "/home/pi/dip/dot_data/traffic/" 

word_trf_list = Smart_File.Find_dir_format(Traffic_route_data,".txt")

word_trf_len = len(word_trf_list)

 

d_list=[Food_root_data, Location_root_data, Traffic_route_data]

v_list=[Food_root_voice, Location_root_voice, Traffic_route_voice]

 

Manual_route_voice = "/home/pi/dip/sound/manual/"

Manual_route_data = "/home/pi/dip/dot_data/manual/" 

word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")

word_manual_len = len(word_manual_list)

 

version_dir='/home/pi/dip/setting/version.txt'

 

mp3_route = "mpg321 /home/pi/dip/sound/"

mp3_route_regit = "/home/pi/dip/sound/"

agree=['��','��','��','��','�׷����ϴ�','�׷�','��','��','����','�¾ƿ�','����']

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

        print("�ܾ� : " + word_list[x[1]])

        print("���� �� : " + data[0])

        print("Dot data : " + data[1])

        d_list = []

        for i in data[1]:

            d_list.append(int(i))

        [d_list.append(0) for i in range(72-len(d_list))]

        print(d_list) #Ȯ��

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

        voice_timmer("Next","����������",3)

    def Next_double():

        global long_click_flag, word_index

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        #voice_timmer("Push","��ư����",1)

        

        if(word_index < word_len):

            word_index_trf = make_button(word_index_trf)    

            print("���� ������ ����ϴµ� ������ ���Ƶΰڽ��ϴ�.")

        else:

            voice_timmer("Last","������������",5)

        long_click_flag = time.time()    

    word_index = make_button(word_index)

     #------�ڷΰ���� �ʱ� ȭ�� ���������� ���� �κ�------

    def Close_top(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Close","back",3)

        

    def Close_top_double(event=None):

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        voice_timmer("Move","�̵��Ϸ�",1)

        clear_all(kit_list)

        Func_top.destroy()

        long_click_flag = time.time()

    def Initialize(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Initial","�ʱ�ȭ��",3)

        

    def Initialize_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        clear_all(kit_list)

        voice_timmer("Move","�̵��Ϸ�",1)

        Func_top.destroy()

        parent.destroy()

            

            

    Func_top.bind("<F11>", Close_top_double)

    frame_sel_exit = tkinter.Frame(Func_top, background = "tan")

    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3,expand=True)

    button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 3, width = 15,

                             background = 'tan1')

    button1.bind("<Button-1>", Close_top)

    button1.grid(row = 0, column = 0)

 

    button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 3, width = 15,

                             background = 'tan1')

    button2.bind("<Button-1>", Initialize)

    button2.grid(row = 0, column = 1)

 

    button3 = tkinter.Button(frame_sel_exit, text="���� ������",command = Next_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 3, width = 15,

                             background = 'tan1')

    button3.bind("<Button-1>", Next)

    button3.grid(row = 0, column = 2)

   

 

def Mapping(i):  

    global text_pw, Shift_flag

    if(i == 46):

        if(Shift_flag == 0):

            Shift_flag = 1

        else:

            Shift_flag = 0

        return

    elif(i == 47):

        pyautogui.press('backspace')

    elif(i == 45):

        pyautogui.press('space')

    else:

        if(Shift_flag == 0):

            pyautogui.typewrite(little_array[i])

        if(Shift_flag == 1):

            pyautogui.typewrite(big_array[i])

    Shift_flag = 0

 

def keyboard_double(event):

    global double_key_flag

    double_key_flag = 1

    

def Make_button(Frame):

    temp_row = 0

    temp_col = 0

    for i in range(0,48):

        key_func = lambda x = i : Mapping(x)

        if little_array[i] in ['`','q','Erase','Space','Shift','=',']','-']:

            ssize=8

        else:

            ssize=5

        #Use lambda to mapping each button

        if(little_array[i] == 'q' or little_array[i] == 'a' or little_array[i] == 'z'):

            temp_row +=1

            if(temp_row >= 2):

                temp_col = 1

            else:

                temp_col = 0

        if(little_array[i] == 'Space'):

            temp = tkinter.Button(Frame,text = 'Space', overrelief="solid",command = key_func,

                                  bg = 'burlywood1', width=ssize,height=2,repeatdelay=400, repeatinterval=80)

            temp.grid(row=3,column = 0)

        elif(little_array[i] == 'Shift'):

            temp = tkinter.Button(Frame,text = 'Shift', overrelief="solid",command = key_func,

                                  bg = 'burlywood1', width=ssize,height=2,repeatdelay=400, repeatinterval=80)

            temp.grid(row=3,column = 11)

        elif(little_array[i] == 'Erase'):

            temp = tkinter.Button(Frame,text = 'Erase', overrelief="solid",command = key_func,

                                  bg = 'burlywood1',width=ssize,height=2,repeatdelay=400, repeatinterval=80)

            temp.grid(row=2,column = 0)

        else:

            temp = tkinter.Button(Frame,text = little_array[i] + '( '+ big_array[i] +' )',

                                  bg = 'burlywood1', overrelief="solid",command = key_func, width=ssize,height=2,

                                  repeatdelay=400, repeatinterval=80)

            if(temp_row == 0 and temp_col == 12):

                temp.grid(row=2,column = 11)

            else:

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

    voice_timmer("Wifi","����",2)

            

def Connect_wifi_double():

    global line, text_pw, long_click_flag, text_ssid, text_ip, wifi_flag

    if(time.time() - long_click_flag < 2):

        return

    #������¶����� �˰����� �и��°��� �����ϴ� flag

    '''

    if wifi_flag == 0:

        wifi_flag = 1

        os.system(mp3_route+"��ȣ������.mp3")

        time.sleep(0.3)

        os.system(mp3_route+"��ȣ������1.mp3")

        time.sleep(0.3)

        os.system(mp3_route+"��ȣ������2.mp3")

        

        with sr.Microphone() as source:

            audio = r.listen(source)

        wifi_flag=0

        try:

            string = r.recognize_google(audio,language='ko_KO')

            string=string.replace(" ","")

            print(string)

            if "������" in string:

                os.system(mp3_route+"��ȣ������3.mp3")

            else:

                os.system(mp3_route+"��ȣ������4.mp3")

                return

        except:

            os.system(mp3_route+"��ȣ������4.mp3")

            wifi_flag=0

            return

    else:

        return

        '''

    Wifi_list = []

    os.system(mp3_route+"��ȣ������3.mp3")

    #voice_timmer("Move","�̵��Ϸ�",2)

    f=open('/home/pi/dip/setting/setip.txt','r')

    ip=f.read()

    f.close()

    long_click_flag = time.time()

    wi = tkinter.Toplevel(bg = 'tan', cursor='none')

    wi.geometry("800x480")

    #wi.attributes("-fullscreen", True)

 

    def scroll_voice():

        voice_timmer("Scroll","��ũ��",5)

    

    def Close(event=None):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Close","back",3)

 

    def Close_double(event=None):

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        voice_timmer("Move","�̵��Ϸ�",1) 

        long_click_flag = time.time()

        wi.destroy()

        Shift_flag = 0

    

 

    def Connect_double():

        global text_pw, text_ssid

        #voice_timmer("Connecnt_try","���ӽõ�",2)

        if(text_ssid.get() == ''):

            #voice_timmer("Connecnt_warnning","���ӽ���",2)

            mb.showinfo('warning','WiFi_ID�� Ȯ�����ּ���',parent=wi)

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

                            os.system('sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant.conf')

                            os.system('sudo chmod 777 /etc/wpa_supplicant/wpa_supplicant_temp.conf')

                            os.system('sudo cp /etc/wpa_supplicant/wpa_supplicant_temp.conf /etc/wpa_supplicant/wpa_supplicant.conf')

                            os.system('sudo wpa_passphrase %s %s>> /etc/wpa_supplicant/wpa_supplicant.conf' %(cell.ssid,text_pw.get()))

                    else:

                        os.system('sed \'s/ENTER_ID/%s/\' /home/pi/dip/wifi_setting/wpa_supplicant_only_id.conf > /etc/wpa_supplicant/wpa_supplicant.conf' %text_ssid.get())

                    break

            

            #voice_timmer("Connecnt_good","���Ӽ���",2)

            mb.showinfo('complete','����� �� ����˴ϴ�.',parent=wi)

            wi.destroy()

            

    def Set_ip():

        dm.set_ip(text_ip.get())

        #voice_timmer("Setip","����",2)

        mb.showinfo('complete','���� �Ϸ�',parent=wi)

        

        

        

    wi.bind("<F11>", Close_double)

 

 

    #-----------------------------------------------------------------------

    top_grid_frame=tkinter.Frame(wi,bg = 'tan')

    frame_top = tkinter.Frame(top_grid_frame,bg = 'tan')

    frame_idpw=tkinter.Frame(frame_top,bg = 'tan')

    

    frame_ip=tkinter.Frame(frame_idpw,bg = 'tan')

    label_ip = tkinter.Label(frame_ip, text="IP : ",width = 10, anchor='e',bg = 'tan')

    label_ip.pack(side ="left")

    text_ip = tkinter.Entry(frame_ip,width = 30)

    text_ip.insert(tkinter.END,ip)

    text_ip.pack(side = "right")

    frame_ip.pack(pady=7)

    

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

    frame_idpw.grid(row=0,column=0)

    

 

    frame_button = tkinter.Frame(frame_top,bg = 'tan')

    

    button_connect = tkinter.Button(frame_button, text = "����", overrelief="solid", height = 1,width=8,

                                    bg = 'burlywood1',command=Set_ip)

    button_connect.pack(pady=4)

    

    button_connect = tkinter.Button(frame_button, text = "����", overrelief="solid", height = 2,width=8,

                                    bg = 'burlywood1',command=Connect_double)

    button_connect.pack()

    

    frame_button.grid(row=0,column=1)

    

    #------------------------------ back button --------------------------------

    back = tkinter.Button(wi,text = "�ڷΰ���", overrelief="solid", height = 1,width=200,

                          repeatdelay=100,bg = 'burlywood1',

                          repeatinterval=100,command=Close_double)

    back.bind("<Button-1>", Close)

    back.pack(side = "bottom")

 

    frame_keyboard=tkinter.Frame(wi, bg = 'tan')#keyboard

    Make_button(frame_keyboard)

    frame_keyboard.pack(side = "bottom")

    frame_top.pack(side = "right")

    

    #----------------------------------wifi list---------------------------------

    frame_left = tkinter.Frame(top_grid_frame,bg = 'tan')

    frame_wifi = tkinter.Frame(frame_left,bg = 'tan')#wifi list

        

    def Ins_double():

        try:

            item = listbox.curselection()

            index = item[0]

            text_ssid.delete(0,30)

            text_ssid.insert(0,Wifi_list[index])

        except:

            voice_timmer("Miss","���ý���",5)

        

    def Search():

        time.sleep(1)

        wifilist = []

        cells = wifi.Cell.all('wlan0')

       

        for cell in cells:

            wifilist.append(cell.ssid)

        return wifilist

    

    scrollbar = tkinter.Scrollbar(frame_wifi, command = scroll_voice,bg = 'tan')#����

    scrollbar.pack(side="right", fill="y")

    listbox=tkinter.Listbox(frame_wifi, yscrollcommand = scrollbar.set,height=7)

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

    button_select = tkinter.Button(frame_id_insert, text = "����", overrelief="solid",

                                   height = 1,width=8, command=Ins_double,

                                   bg = 'burlywood1')

    button_select.pack(side="left")

 

    button_retry = tkinter.Button(frame_id_insert, text = "�ٽð˻�", overrelief="solid",

                                  height = 1,width=8, command=Retry_double,

                                  bg = 'burlywood1')

    button_retry.pack(side="right") 

    

    frame_id_insert.pack()

    frame_under_list.grid(row = 1, column = 0)#grid

    frame_left.pack(side = "left")

    #-----------------------------------------------------------------------

    top_grid_frame.pack(pady=40) #������ ����

 

def Word_education(event):

    global long_click_flag

    long_click_flag = time.time()

    voice_timmer("Word","�ܾ��н�",5)

    

def Word_education_double():

    global long_click_flag

    if(time.time() - long_click_flag < 3):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    #���� �ʱ�ȭ �սô�.

    #voice_timmer("demo","����",5)

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

        voice_timmer("Move","�̵��Ϸ�",1)

        Jamo.destroy()

        

    #------������� ��Ʈ------

    def Traffic(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Tra","�������",3)

 

    

    def Traffic_double():

        global long_click_flag, word_index_trf, Traffic_frame

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1)

 

        word_sheet(Traffic_route_data,Traffic_route_voice,

                   word_trf_list,word_trf_len,Jamo)

        

    #------���� ��Ʈ------

    def Food(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Food","����",3)

        

    

    def Food_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1)

        word_sheet(Food_root_data,Food_root_voice,

                   word_food_list,word_food_len,Jamo)

        

        

    #------��� ��Ʈ------

    def Location(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Loc","���",3)

        

    def Location_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        word_sheet(Location_root_data,Location_root_voice,

                   word_location_list,word_location_len,Jamo)

 

    def User_word(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("User","���������",3)

 

    def User_word_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        word_sheet(Manual_route_data,Manual_route_voice,

                   word_manual_list,word_manual_len,Jamo)

        voice_timmer("Move","�̵��Ϸ�",1) 

        

 

    

        

        

    Jamo.bind("<F11>", Close_double)

    #---------Ż�� ���� ��� ���������-----------------

    frame_edu = tkinter.Frame(Jamo, background = "tan")

    frame_edu.pack(side = "top", anchor = 'c',padx = 3, pady = 3,expand=True)

    button1 = tkinter.Button(frame_edu, text="�������",command = Traffic_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'burlywood1')

    button1.bind("<Button-1>", Traffic)

    button1.grid(row = 0, column = 0)

 

    button2 = tkinter.Button(frame_edu, text="����",command = Food_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'tan1')

    button2.bind("<Button-1>", Food)

    button2.grid(row = 0, column = 1)

 

    button3 = tkinter.Button(frame_edu, text="���",command = Location_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'burlywood1')

    button3.bind("<Button-1>", Location)

    button3.grid(row = 0, column = 2)

 

    button4 = tkinter.Button(frame_edu, text="����� ����",command = User_word_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'tan1')

    button4.bind("<Button-1>", User_word)

    button4.grid(row = 0, column = 3)

 

    #�ڷΰ��� ��ư

    

    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")

    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

    button5 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 3, width = 20,

                             background = 'tan3')

    button5.bind("<Button-1>", Close)

    button5.pack()

        

def Free_study(event):

    global long_click_flag

    long_click_flag = time.time()

    voice_timmer("Free","�������", 3)

    #�������� ���� �ٽ��ؾߵ˴ϴ�.

    #�������� �ܾ��н����� ���Ұ� �߰�

 

def Free_study_double():

    global long_click_flag

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    #���� �ʱ�ȭ �սô�.

    #voice_timmer("demo","����",5)

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

        voice_timmer("Move","�̵��Ϸ�",1) 

        free.destroy()

        

    free.bind("<F11>", Close_double)

    

    num = []

    for i in range(0,72):

        num.append(tkinter.IntVar())    

    

    def Sel(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Sel","����",4)

        

    def Sel_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Select","����Ϸ�",5) 

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

                                    text = "�ڷΰ���",

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

                                    text = "����",

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

    voice_timmer("Jamo","�ڸ��н�",3)

 

def jamo_edu_double():

    global long_click_flag

    if(time.time() - long_click_flag < 3):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    #���� �ʱ�ȭ �սô�.

    #voice_timmer("demo","����",5)

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

        voice_timmer("Move","�̵��Ϸ�",1)

        Jamo.destroy()

    Jamo.bind("<F11>", Close_double)

    

    def Chosung(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Cho","�ʼ�",3)

    

    #------�ʼ� ��Ʈ------

    def Chosung_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.geometry("800x480")

        Chosung.attributes("-fullscreen", True)

        cho_list = ['��','��','��','��','��','��','��','��','��','��','��','��','��','�ȼҸ�']

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

            print(d_list) #Ȯ��

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

                

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

            long_click_flag = time.time()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            long_click_flag = time.time()

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1)

            Chosung.destroy()

            Jamo.destroy()

            

            

        Chosung.bind("<F11>", Close_top_double)

 

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")

        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

        button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button1.bind("<Button-1>", Close_top)

        button1.pack(side = "left");

 

        button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button2.bind("<Button-1>", Initialize)

        button2.pack(side = "right");

 

        

 

    def Moum(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Moum","����",3)

        

    #------���� ��Ʈ------

    def Moum_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.geometry("800x480")

        Chosung.attributes("-fullscreen", True)

        cho_list = ['��','��','��','��','��','��','��','��','��','��','��','��','��','��',

                    '��','��','��','��','��','��','��']

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

            print(d_list) #Ȯ��

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

                

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

            long_click_flag = time.time()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            long_click_flag = time.time()

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1)

            Chosung.destroy()

            Jamo.destroy()

            

            

        Chosung.bind("<F11>", Close_top_double)

 

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")

        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

        button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button1.bind("<Button-1>", Close_top)

        button1.pack(side = "left")

 

        button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button2.bind("<Button-1>", Initialize)

        button2.pack(side = "right")

        

    

    def jongsung(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Jong","����",3)

        

    def jongsung_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.geometry("800x480")

        Chosung.attributes("-fullscreen", True)

        cho_list = ['��','��','��','��','��','��','��','��','��','��','��','��','��','��']

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

            print(d_list) #Ȯ��

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

                

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

            long_click_flag = time.time()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            long_click_flag = time.time()

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1)

            Chosung.destroy()

            Jamo.destroy()

            

            

        Chosung.bind("<F11>", Close_top_double)

 

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")

        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

        button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button1.bind("<Button-1>", Close_top)

        button1.pack(side = "left");

 

        button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button2.bind("<Button-1>", Initialize)

        button2.pack(side = "right")

    

    def simple_h1(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Simple","1������",3)

 

    def simple_h1_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.geometry("800x480")

        Chosung.attributes("-fullscreen", True)

        cho_list = ['��','��','��','��','��','��','��','ī','Ÿ','��','��','��','��',

                    '��','��','��','��','��','��','��','��','��','��','��','��','��','��']

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

            print(d_list) #Ȯ��

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

                

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

            long_click_flag = time.time()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            long_click_flag = time.time()

            voice_timmer("Move","�̵��Ϸ�",1)

            Chosung.destroy()

            Jamo.destroy()

            

            

        Chosung.bind("<F11>", Close_top_double)

 

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")

        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

        button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button1.bind("<Button-1>", Close_top)

        button1.pack(side = "left");

 

        button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button2.bind("<Button-1>", Initialize)

        button2.pack(side = "right")

    

    def simple_h2(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Simple","2������",3)

 

    def simple_h2_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.geometry("800x480")

        Chosung.attributes("-fullscreen", True)

        cho_list = ['�׷���','�׷���','�׷���','�׷��Ƿ�','�׷���','�׸���']

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

            print(d_list) #Ȯ��

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

                

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

            long_click_flag = time.time()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            clear_all(kit_list)

            long_click_flag = time.time()

            voice_timmer("Move","�̵��Ϸ�",1)

            Chosung.destroy()

            Jamo.destroy()

            

            

        Chosung.bind("<F11>", Close_top_double)

 

        frame_sel_exit = tkinter.Frame(Chosung, background = "tan")

        frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

        button1 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_top_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button1.bind("<Button-1>", Close_top)

        button1.pack(side = "left");

 

        button2 = tkinter.Button(frame_sel_exit, text="�ʱ� ȭ������",command = Initialize_double,

                                 repeatdelay=100,

                                 repeatinterval=100,

                                 height = 3, width = 15,

                                 background = 'tan1')

        button2.bind("<Button-1>", Initialize)

        button2.pack(side = "right")

        

        

    Jamo.bind("<F11>", Close_double)

    #---------�ʼ� ���� ���� ���� -----------------

    frame_edu = tkinter.Frame(Jamo, background = "tan")

    frame_edu.pack(side = "top", anchor = 'c',padx = 3, pady = 3,expand=True)

    button1 = tkinter.Button(frame_edu, text="�ʼ�",command = Chosung_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'burlywood1')

    button1.bind("<Button-1>", Chosung)

    button1.grid(row = 0, column = 0)

 

    button2 = tkinter.Button(frame_edu, text="����",command = Moum_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'tan1')

    button2.bind("<Button-1>", Moum)

    button2.grid(row = 0, column = 1)

 

    button3 = tkinter.Button(frame_edu, text="����",command = jongsung_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'burlywood1')

    button3.bind("<Button-1>", jongsung)

    button3.grid(row = 0, column = 2)

 

    button4 = tkinter.Button(frame_edu, text="1�� ����",command = simple_h1_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'tan1')

    button4.bind("<Button-1>", simple_h1)

    button4.grid(row = 0, column = 3)

 

    button5 = tkinter.Button(frame_edu, text="2�� ����",command = simple_h2_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 16, width = 18,

                             background = 'burlywood1')

    button5.bind("<Button-1>", simple_h2)

    button5.grid(row = 0, column = 4)

 

    #�ڷΰ��� ��ư

    

    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")

    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

    button5 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 3, width = 20,

                             background = 'tan3')

    button5.bind("<Button-1>", Close)

    button5.pack();

    

    #voice_timmer("demo","����",5)

 

def Regist_word(event):

    global long_click_flag

    long_click_flag = time.time() 

    voice_timmer("Regist","�ܾ���",5)

    #����� �ܾ�� ������Ʈ�ص� �� �������� ¥���Ѵ�.

    

def Regist_word_double():

    global long_click_flag

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    #���� �ʱ�ȭ �սô�.

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

        voice_timmer("Move","�̵��Ϸ�",1)

        Regist.destroy()

    Regist.bind("<F11>", Close_double)

 

    def choose_save(data, length, data_ko):

        global word_manual_list, word_manual_len

        time.sleep(0.5)

        os.system(mp3_route+"���忩��.mp3")

        while 1:

            try:

                with sr.Microphone() as source:

                    audio = r.listen(source)

                string = r.recognize_google(audio,language='ko_KO')

                string=string.replace(" ","")

                if string in agree:

                    os.system(mp3_route+"�ܾ�������.mp3")

                    f=open(Manual_route_data+data_ko+'.txt','w')

                    f.write(str(length)+'\n')

                    for _ in data:

                        f.write(str(_))

                    f.close()

                    tts = gTTS(text=data_ko, lang='ko')

                    tts.save(Manual_route_voice+data_ko+".mp3")

                    os.system(mp3_route+"���强��.mp3")

                    word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")

                    word_manual_len = len(word_manual_list)

                else:

                    os.system(mp3_route+"�������.mp3")

                break

            except:

                os.system(mp3_route+"�ٽø����ּ���.mp3")

 

        

    def Regit_word(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Regit","�ܾ��Ͻ���",3)

        

    def Regit_word_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        

        os.system(mp3_route+"�����Է���.mp3")

        with sr.Microphone() as source:

            audio = r.listen(source)

 

        os.system(mp3_route+"�����Է���.mp3")

        #�Է� �ܾ� �м�

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

                os.system(mp3_route+"�����Է�����.mp3")

                print(cnt)

 

            else:

                print("text: "+ string)

                print(cnt)

                tts = gTTS(text="�Էµ� �ܾ�� "+ string + " �Դϴ�.", lang='ko')

                tts.save(mp3_route_regit+"��������ӽ�.mp3")

                os.system(mp3_route+"��������ӽ�.mp3")

                choose_save(dot_data,len(string.replace(" ","")),string)

                print(dot_data)

        except:

            os.system(mp3_route+"�ܾ�м�����.mp3")

            

 

    #�ڷΰ���, �ܾ��� ��ư

    

    frame_sel_exit = tkinter.Frame(Regist, background = "tan")

    frame_sel_exit.pack(anchor = 'c',expand=True)

    button_back = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 25, width = 50,

                             background = 'tan1')

    button_back.bind("<Button-1>", Close)

 

    button_regist = tkinter.Button(frame_sel_exit, text="�ܾ��� ����",command = Regit_word_double,

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

    voice_timmer("Exit","�������",3)

 

def exit_double():

    global long_click_flag,window

    if(time.time() - long_click_flag < 3):

        return

    voice_timmer("Exit_true","����������մϴ�",3)

    window.destroy()

    #clear_all(kit_list)

    long_click_flag = time.time()

    #motor �� ������

    #os.~~~ exit

def quiz(event):

    global long_click_flag

    long_click_flag = time.time() 

    voice_timmer("Quiz","����",2.5)

 

def quiz_double():

    global long_click_flag, now_data_k, now_data_b, now_voice_route

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

 

    

    #���� �ʱ�ȭ �սô�.

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

        voice_timmer("Move","�̵��Ϸ�",1)

        #�ʱ�ȭ

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

        print("�ܾ� : " + r_k_data)

        print("���� �� : " + rand_data[0])

        print("Dot data : " + rand_data[1])

        d_list = []

        for i in rand_data[1]:

            d_list.append(int(i))

        [d_list.append(0) for i in range(72-len(d_list))]

        print(d_list)

        print("���� ����ϴ� �κ�")

        return r_k_data.replace('.txt',''), d_list, q_v_route

 

    now_data_k, now_data_b, now_voice_route = make_quize()

    

    def next_q(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Quiz_n","��������",2)

    

    def next_q_double():

        global long_click_flag, now_data_k, now_data_b, now_voice_route

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        voice_timmer("Quiz_re","��������",2)

        now_data_k, now_data_b, now_voice_route = make_quize()

 

 

    def answer(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Quiz_a","���主�ϱ�",3)

    

    def answer_double():

        global long_click_flag, now_data_k, now_data_b, now_voice_route

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        

        os.system(mp3_route+"�����Է���.mp3")

        with sr.Microphone() as source:

            audio = r.listen(source)

 

        os.system(mp3_route+"�����Է���.mp3")

        #�Է� �ܾ� �м�

        try:

            string = r.recognize_google(audio,language='ko_KO')

            print(string.replace(' ',''),now_data_k.replace(' ',''))

            if string.replace(' ','') == now_data_k.replace(' ',''):

                os.system(mp3_route+"��������.mp3")

                now_data_k, now_data_b, now_voice_route = make_quize()

            else:

                os.system(mp3_route+"��������.mp3")

        

        except:

            os.system(mp3_route+"�ܾ�м�����.mp3")

        

 

    def confirm(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Quiz_c","����Ȯ��",3)

 

    def confirm_double():

        global long_click_flag, now_data_k, now_voice_route

        if(time.time() - long_click_flag < 2):

            return

        long_click_flag = time.time()

        os.system(mp3_route+"������.mp3")

        os.system('mpg321 '+now_voice_route+now_data_k+".mp3")

        os.system(mp3_route+"�Դϴ�.mp3")

    

    

    

    frame_sel_exit = tkinter.Frame(Quiz, background = "tan")

    frame_sel_exit.pack(anchor = 'c',expand=True)

    button_back = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 25, width = 25,

                             background = 'tan1')

    button_back.bind("<Button-1>", Close)

 

    button_answer = tkinter.Button(frame_sel_exit, text="���� ���ϱ�",command = answer_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 25, width = 25,

                             background = 'burlywood1')

    button_answer.bind("<Button-1>", answer)

 

    button_confirm = tkinter.Button(frame_sel_exit, text="���� Ȯ��",command = confirm_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             relief = 'solid',

                             height = 25, width = 25,

                             background = 'tan1')

    button_confirm.bind("<Button-1>", confirm)

 

    button_next_q = tkinter.Button(frame_sel_exit, text="���� ����",command = next_q_double,

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

 

def Update(event):

    global long_click_flag

    long_click_flag = time.time()  

    voice_timmer("Update","������Ʈ",3)

 

def Update_double():

    global long_click_flag,word_food_list,word_food_len,word_location_list,word_location_len\

           ,word_trf_list,word_trf_len,d_list,v_list

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","������Ʈ����",4) 

    long_click_flag = time.time()

    time.sleep(1)

    try:

        signal = dm.down_func(d_list,v_list,version_dir)

        if signal == 'complete':

            word_food_list = Smart_File.Find_dir_format(Food_root_data,".txt")

            word_food_len = len(word_food_list)

 

            word_location_list = Smart_File.Find_dir_format(Location_root_data,".txt")

            word_location_len = len(word_location_list)

 

            word_trf_list = Smart_File.Find_dir_format(Traffic_route_data,".txt")

            word_trf_len = len(word_trf_list)

 

            d_list=[Food_root_data, Location_root_data, Traffic_route_data]

            v_list=[Food_root_voice, Location_root_voice, Traffic_route_voice]

            os.system(mp3_route+"������Ʈ�Ϸ�.mp3")

        else:

            os.system(mp3_route+"�ֽŹ���.mp3")

    

    except:

        voice_timmer("warning","�������",7)

        #pass

    

 

if __name__ == '__main__':

    global window

    #os.system("python3 ~/dip/logo.py")

    

    window=tkinter.Tk()

    window.title("Graduation Project")

    window.geometry("800x480")

 

 

    window.configure(background='tan', cursor='none')

    window.attributes("-fullscreen", True)

 

 

 

    

 

    #window.configure(background='tan')    

    #���� ����� ���� �ʱ�ȭ �� ��������

    #window.resizable(False, False)

    #frame = Frame(window, width=600, height=300)

 

    def toggle_fullscreen(event=None):

        window.state = not window.state  # Just toggling the boolean

        window.attributes("-fullscreen", window.state)

        return "break"    

    window.bind("<F11>", toggle_fullscreen)

 

    frame1=tkinter.Frame(window,background="tan")

    button1 = tkinter.Button(frame1, text="����",command = Connect_wifi_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = 'tan1')

    button1.bind("<Button-1>", Connect_wifi)

    button2 = tkinter.Button(frame1, text="�ܾ� �н�", command = Word_education_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = "burlywood1")

 

    button2.bind("<Button-1>", Word_education)

 

    button3 = tkinter.Button(frame1, text="����,���� �� ���� �н�", command = jamo_edu_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = 'tan1')

    button3.bind("<Button-1>", jamo_edu)

    

    button4 = tkinter.Button(frame1, text="������Ʈ", command = Update_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = "burlywood1")

    button4.bind("<Button-1>", Update)

    

    button5 = tkinter.Button(frame1, text="���� ���", command = Free_study_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = "tan1")

    button5.bind("<Button-1>", Free_study)

    

    button6 = tkinter.Button(frame1, text="�ܾ� ���",command = Regist_word_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = 'burlywood1')

    button6.bind("<Button-1>", Regist_word)

    

    button7 = tkinter.Button(frame1, text="��� ����", command = exit_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = "burlywood1")

 

    button7.bind("<Button-1>", exit_)

 

    button8 = tkinter.Button(frame1, text="����Ǯ��", command = quiz_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 12, width = 22,

                             relief = 'solid',

                             background = "tan1")

 

    button8.bind("<Button-1>", quiz)

 

    

    button1.grid(row = 0, column = 0)

    button2.grid(row = 0, column = 1)

    button3.grid(row = 0, column = 2)

    button4.grid(row = 1, column = 0)

    button5.grid(row = 1, column = 1)

    button6.grid(row = 1, column = 2)

 

    button7.grid(row = 0, column = 3)

    button8.grid(row = 1, column = 3)

     #���� ���콺 ��ư ���ε�

    frame1.pack(expand=True);

    window.mainloop()