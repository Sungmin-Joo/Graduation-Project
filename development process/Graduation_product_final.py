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
import dot_convert as dc
import tkinter.font
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

#키보드 문자를 위한 배열 설정.
little_array = ['`','1','2','3','4','5','6','7','8','9','0','-','=',
                'q','w','e','r','t','y','u','i','o','p','[' ,']',
                'a','s','d','f','g','h','j','k','l',';',
                'z','x','c','v','b','n','m',',','.','/','Space','Shift','Erase']
big_array = ['~','!','@','#','$','%','^','&','*','(',')','_','+',
             'Q','W','E','R','T','Y','U','I','O','P','{','}',
             'A','S','D','F','G','H','J','K','L',':',
             'Z','X','C','V','B','N','M','<','>','?','Space','Shift','Erase']

#보드의 볼륨 초기값을 설정
os.system('sudo amixer cset numid=1 88%')

# ------------------------- 프로젝트에 필요한 경로 설정. -------------------------
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

Manual_route_voice = "/home/pi/dip/sound/manual/"
Manual_route_data = "/home/pi/dip/dot_data/manual/"
word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")
word_manual_len = len(word_manual_list)

version_dir='/home/pi/dip/setting/version.txt'

mp3_route = "mpg321 /home/pi/dip/sound/"
mp3_route_regit = "/home/pi/dip/sound/"

#-----------------------------------------------------------------------------------------


#----------------------------- 단어 표기를 위한 변수 및 배열 선언 ---------------------------
d_list=[Food_root_data, Location_root_data, Traffic_route_data]
v_list=[Food_root_voice, Location_root_voice, Traffic_route_voice]


agree=['응','어','네','넵','그렇습니다','그래','엉','넹','으응','맞아요','예스']
r = sr.Recognizer()

simple_k_list = [
    ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ','된소리'],
    ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅔ','ㅚ','ㅘ','ㅝ','ㅢ','ㅖ','ㅟ','ㅒ','ㅙ','ㅞ'],
    ['ㄱ','ㄴ','ㄷ','ㄹ','ㅁ','ㅂ','ㅅ','ㅇ','ㅈ','ㅊ','ㅋ','ㅌ','ㅍ','ㅎ'],
    ['가','나','다','마','바','사','자','카','타','파','하','것','ㅆ받침','억','언','얼','연','열','영','옥','온','옹','운','울','은','을','인'],
    ['그래서','그러나','그러면','그러므로','그런데','그리고']
    ]
simple_d_list = [
    [[0,1,0,0,0,0], [1,1,0,0,0,0], [0,1,1,0,0,0], [0,0,0,1,0,0], [1,0,0,1,0,0], [0,1,0,1,0,0], [0,0,0,0,0,1],
     [0,1,0,0,0,1], [0,0,0,1,0,1], [1,1,1,0,0,0], [1,0,1,1,0,0], [1,1,0,1,0,0], [0,1,1,1,0,0], [0,0,0,0,0,1]],
    [[1,0,1,0,0,1], [0,1,0,1,1,0], [0,1,1,0,1,0], [1,0,0,1,0,1], [1,0,0,0,1,1], [0,1,0,0,1,1], [1,1,0,0,1,0],
     [1,1,0,0,0,1], [0,1,1,0,0,1], [1,0,0,1,1,0], [1,0,1,1,1,0], [1,1,0,1,1,0], [1,1,0,1,1,1], [1,0,1,0,1,1],
     [1,1,1,0,1,0], [0,1,1,1,0,1], [0,1,0,0,1,0], [1,1,0,0,1,0,1,0,1,1,1,0], [0,1,0,1,1,0,1,0,1,1,1,0],
     [1,0,1,0,1,1,1,0,1,1,1,0], [1,1,1,0,1,0,1,0,1,1,1,0]],
    [[1,0,0,0,0,0], [0,0,1,1,0,0], [0,0,0,1,1,0], [0,0,1,0,0,0], [0,0,1,0,0,1], [1,0,1,0,0,0], [0,0,0,0,1,0],
     [0,0,1,1,1,1], [1,0,0,0,1,0], [0,0,1,0,1,0], [0,0,1,1,1,0], [0,0,1,0,1,1], [0,0,1,1,0,1], [0,0,0,1,1,1]],
    [[1,1,1,0,0,1], [1,1,0,0,0,0], [0,1,1,0,0,0], [1,0,0,1,0,0], [0,1,0,1,0,0], [1,0,1,0,1,0], [0,1,0,0,0,1],
     [1,1,1,0,0,0], [1,0,1,1,0,0], [1,1,0,1,0,0], [0,1,1,1,0,0], [0,1,0,1,0,1,0,1,1,0,1,0],[0,1,0,0,1,0],
     [1,1,0,1,0,1], [0,1,1,1,1,1], [0,1,1,1,1,0], [1,0,0,0,0,1], [1,0,1,1,0,1], [1,1,1,1,0,1], [1,1,0,0,1,1],
     [1,0,1,1,1,1], [1,1,1,1,1,1], [1,1,1,1,0,0], [1,1,1,0,1,1], [1,0,0,1,1,1], [0,1,1,0,1,1], [1,1,1,1,1,0]],
    [[1,0,0,0,0,0,0,1,1,0,1,0], [1,0,0,0,0,0,1,1,0,0,0,0], [1,0,0,0,0,0,0,0,1,1,0,0], [1,0,0,0,0,0,0,0,1,0,0,1],
     [1,0,0,0,0,0,1,1,0,1,1,0], [1,0,0,0,0,0,1,0,0,0,1,1]]
    ]
t_x = [2,3,2,3,2]
t_y = [7,7,7,9,3]
#-----------------------------------------------------------------------------------------


####################### call lim's code  ########################
kit_list = srv.setup()
srv.clear_all(kit_list)
#################################################################


# 단어학습 파트에서 각 파트별로 단어를 표기하기 위한 함수 정의
def word_sheet(root_data,root_sound,word_list,word_len,parent):
    global word_index
    Func_top = tkinter.Toplevel(background = "tan", cursor='none')
    Func_top.geometry("800x480")
    Func_top.attributes("-fullscreen", True)
    word_index = 0

    def Map_wrd(x):
        voice_timmer_root(root_sound,x[0],x[0],2)
        data = Smart_File.Read_file(root_data,word_list[x[1]]).split('\n')
        #디버깅을 위한 출력
        #print("-----------------------------------------------")
        #print("단어 : " + word_list[x[1]])
        #print("글자 수 : " + data[0])
        #print("Dot data : " + data[1])

        #72개의 모터에 넘겨줄 데이터 정의
        d_list = []
        for i in data[1]:
            d_list.append(int(i))
        [d_list.append(0) for i in range(72-len(d_list))]
        print(d_list) #확인
        #모터 구동
        srv.active(d_list,kit_list)

    #각 단어에 해당하는 버튼을 만들어주는 함수
    def make_button(index):
        global Func_frame
        color_flag=1
        if(index != 0):
            Func_frame.destroy()
        Func_frame = tkinter.Frame(Func_top,background = "tan")
        Func_frame.pack(side = "top", anchor = 'c',expand=True)
        #모든 단어는 3행 7열로 배열
        for r in range(3):
            for c in range(7):
                if(color_flag):
                    color_= '#222b3f'
                    fg_color = 'tan'
                    color_flag=0
                else:
                    color_= 'burlywood1'
                    fg_color = 'black'
                    color_flag=1
                if ((r==0 or r==1 or r==2) and (c==0 or c==6)):
                    w=13
                else:
                    w=12
                if(index < word_len):
                    #람다 함수로 각 버튼별로 같은 이름의 다른 동작을 하는 함수를 맵핑
                    wrd = lambda x = [str(word_list[index].replace(".txt","")), index]: Map_wrd(x)
                    word_button = tkinter.Button(Func_frame,
                                        text = str(word_list[index].replace(".txt","")),
                                        overrelief="solid", fg = fg_color,
                                        height = 7,
                                        width=w,
                                        bg=color_,
                                        command=wrd)
                    word_button.grid(row = r, column = c)
                    index = index + 1
                else:
                    word_button = tkinter.Button(Func_frame,
                                        text = '',
                                        overrelief="solid",
                                        height = 7,
                                        bg=color_,
                                        width=w)
                    word_button.grid(row = r, column = c)
        return index

    # ------- 단어 갯수가 21개를 초과하면 다음 단어 페이지로 이동 --------
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
        srv.clear_all(kit_list)
        long_click_flag = time.time()
    # ----------------------------------------------------------------

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
        srv.clear_all(kit_list)
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
        voice_timmer("Move","이동완료",1)
        srv.clear_all(kit_list)
        Func_top.destroy()
        parent.destroy()

    Func_top.bind("<F11>", Close_top_double)
    frame_sel_exit = tkinter.Frame(Func_top, background = "burlywood1")
    frame_sel_exit.pack(side = "bottom", anchor = 'c',expand=True)
    button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 34,
                             background = 'burlywood1')
    button1.bind("<Button-1>", Close_top)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 34,
                             background = 'burlywood1')
    button2.bind("<Button-1>", Initialize)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_sel_exit, text="다음 페이지",command = Next_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             height = 3, width = 34,
                             background = 'burlywood1')
    button3.bind("<Button-1>", Next)
    button3.grid(row = 0, column = 2)
    #--------------------------------------------------------------------------------------------

#키보드 각 버튼에 대한 동작 정의해주는 함수
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

#키보드 버튼을 만드는 함수
def Make_button(Frame):
    temp_row = 0
    temp_col = 0
    for i in range(0,48):
        #람다 함수로 각 버튼별로 같은 이름의 다른 동작을 하는 함수를 맵핑
        key_func = lambda x = i : Mapping(x)
        if little_array[i] in ['`','q','Erase','Space','Shift','=',']','-']:
            ssize=8
        else:
            ssize=5
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

#시스템에 관한 음성 안내를 출력하기위한 함수
def voice_timmer(key, sound, minute):
    global voice_voice_flags
    if(voice_flags.get(key,0) == 0):
        voice_flags[key] = time.time()
        os.system(mp3_route+sound+".mp3")
    else:
    #첫 클릭 후 minute 초 만큼 입력 무시, 음성 동시 출력 방지
        if(time.time() - voice_flags.get(key,0) > minute):
            voice_flags[key] = time.time() 
            os.system(mp3_route+sound+".mp3")

#각 단어 별로 경로를 지정해서 음성 안내를 출력하기위한 함수
def voice_timmer_root(root, key, sound, minute):
    global voice_voice_flags
    if(voice_flags.get(key,0) == 0):
        voice_flags[key] = time.time()
        os.system("mpg321 "+root+sound+".mp3")
    else:
        #첫 클릭 후 minute 초 만큼 입력 무시, 음성 동시 출력 방지
        if(time.time() - voice_flags.get(key,0) > minute):
            voice_flags[key] = time.time()
            os.system("mpg321 "+root+sound+".mp3")

#-------------------- 설정 탭 top level 관련 함수 -------------------------
def Connect_wifi(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Wifi","설정",2)

def Connect_wifi_double():
    global line, text_pw, long_click_flag, text_ssid, text_ip, wifi_flag, Wifi_list, first_flag
    if(time.time() - long_click_flag < 2):
        return
    #음성출력때문에 알고리즘이 밀리는것을 방지하는 flag
    #아래는 관리자인지 확인하는 음성인식 부분 코드이지만 데모때는 생략.
    '''
    if wifi_flag == 0:
        wifi_flag = 1
        os.system(mp3_route+"보호자전용.mp3")
        time.sleep(0.3)
        os.system(mp3_route+"보호자전용1.mp3")
        time.sleep(0.3)
        os.system(mp3_route+"보호자전용2.mp3")

        with sr.Microphone() as source:
            audio = r.listen(source)
        wifi_flag=0
        try:
            string = r.recognize_google(audio,language='ko_KO')
            string=string.replace(" ","")
            print(string)
            if "관리자" in string:
                os.system(mp3_route+"보호자전용3.mp3")
            else:
                os.system(mp3_route+"보호자전용4.mp3")
                return
        except:
            os.system(mp3_route+"보호자전용4.mp3")
            wifi_flag=0
            return
    else:
        return
        '''
    Wifi_list = []
    os.system(mp3_route+"보호자전용3.mp3")
    #voice_timmer("Move","이동완료",2)
    f=open('/home/pi/dip/setting/setip.txt','r')
    ip=f.read()
    f.close()
    long_click_flag = time.time()
    wi = tkinter.Toplevel(bg = '#222b3f', cursor='none')
    wi.geometry("800x480")
    wi.attributes("-fullscreen", True)

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

    # 와이파이 연결을 위한 설정을 도와주는 함수
    # wpa_supplicant.conf 자체를 변경하기 때문에 재부팅 후 적용
    def Connect_double():
        global text_pw, text_ssid
        #voice_timmer("Connecnt_try","접속시도",2)
        if(text_ssid.get() == ''):
            #voice_timmer("Connecnt_warnning","접속실패",2)
            mb.showinfo('warning','WiFi_ID를 확인해주세요',parent=wi)
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

            #voice_timmer("Connecnt_good","접속성공",2)
            mb.showinfo('complete','재부팅 후 적용됩니다.',parent=wi)
            wi.destroy()

    def Set_ip():
        dm.set_ip(text_ip.get())
        #voice_timmer("Setip","변경",2)
        mb.showinfo('complete','적용 완료',parent=wi)

    wi.bind("<F11>", Close_double)
    #-----------------------------------------------------------------------
    top_grid_frame=tkinter.Frame(wi,bg = '#222b3f')
    frame_top = tkinter.Frame(top_grid_frame,bg = '#222b3f')

    frame_up_scale = tkinter.Frame(frame_top,bg = '#222b3f')

    frame_idpw=tkinter.Frame(frame_up_scale,bg = '#222b3f')
    frame_ip=tkinter.Frame(frame_idpw,bg = '#222b3f')
    label_ip = tkinter.Label(frame_ip, text="IP : ",width = 10, anchor='e',bg = '#222b3f',fg='tan')
    label_ip.pack(side ="left")
    text_ip = tkinter.Entry(frame_ip,width = 30)
    text_ip.insert(tkinter.END,ip)
    text_ip.pack(side = "right")
    frame_ip.pack(pady=7)

    frame_id=tkinter.Frame(frame_idpw,bg = '#222b3f')
    label_ssid = tkinter.Label(frame_id, text="WiFi_ID : ",width = 10, anchor='e',bg = '#222b3f',fg='tan')
    label_ssid.pack(side ="left")
    text_ssid = tkinter.Entry(frame_id,width = 30)
    text_ssid.pack(side = "right")
    frame_id.pack()

    frame_pw=tkinter.Frame(frame_idpw,bg = '#222b3f')
    label_pw = tkinter.Label(frame_pw, text="Password : ",width = 10, anchor='e',bg = '#222b3f',fg='tan')
    label_pw.pack(side ="left")
    text_pw = tkinter.Entry(frame_pw,width = 30)
    text_pw.pack(side = "right")
    frame_pw.pack()
    frame_idpw.grid(row=0,column=0)

    frame_button = tkinter.Frame(frame_up_scale,bg = '#222b3f')
    button_connect = tkinter.Button(frame_button, text = "변경", overrelief="solid", height = 1,width=8,
                                    bg = 'burlywood1',command=Set_ip)
    button_connect.pack(pady=4)
    button_connect = tkinter.Button(frame_button, text = "접속", overrelief="solid", height = 2,width=8,
                                    bg = 'burlywood1',command=Connect_double)
    button_connect.pack()
    frame_button.grid(row=0,column=1)
    frame_up_scale.pack()

    ################################### volume ###################################
    scale_val=tkinter.IntVar()
    volume_val = [0,65,70,75,80,84,88,90,92,94,96,98,99,100]
    def volume_check(self):
        os.system('sudo amixer cset numid=1 {0}%'.format(volume_val[int(scale_val.get())]))
        #print('sudo amixer cset numid=1 {0}%'.format(volume_val[int(scale_val.get())]))

    first_flag = 1
    def Set_vol():
        global first_flag
        x = wi.winfo_x()
        y = wi.winfo_y()
        wi_vol = tkinter.Toplevel(master=wi,bg = 'tan', cursor='none',relief='ridge',padx=2,pady=2,bd=5)
        wi_vol.title('Volume')
        scale=tkinter.Scale(wi_vol,variable=scale_val,command=volume_check, orient="horizontal",
                        showvalue=False, to=13, length=250, bg='burlywood1', relief = 'ridge',
                        troughcolor = 'tan')
        scale.pack()
        wi_vol.geometry("+%d+%d" % (x + 200, y + 150))
        if first_flag:
            first_flag = 0
            scale.set(6)

    volume_button=tkinter.Button(wi, text = "음량조절", overrelief="solid",
                                   height = 1,width=8, command=Set_vol,
                                   bg = 'burlywood1')
    volume_button.place(x=400,y=176)
    ######################### volume end #################################

    ######################################## word delete ##################################

    def Del_word():
        global first_flag, word_manual_list
        wi_del = tkinter.Toplevel(master=wi,bg = 'tan', cursor='none',relief='ridge',padx=2,pady=2,bd=5)
        wi_del.title('Delete')

        frame_del = tkinter.Frame(wi_del,bg = 'tan')
        word_scrollbar = tkinter.Scrollbar(frame_del,bg = 'tan')
        word_scrollbar.pack(side="right", fill="y")
        word_listbox=tkinter.Listbox(frame_del, yscrollcommand = scrollbar.set,height=7)
        word_listbox.pack(side="left")
        word_scrollbar["command"]=word_listbox.yview

        line = 1
        word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")
        for name in word_manual_list:
           word_listbox.insert(line, name.replace('.txt',''))
           line = line + 1
        frame_del.pack()

        def do_del():
            global word_manual_list, word_manual_len, line
            try:
                item = word_listbox.curselection()
                index = item[0]
                os.system('sudo rm '+ Manual_route_data + word_manual_list[index])
                os.system('sudo rm '+ Manual_route_voice + word_manual_list[index].replace('txt','mp3'))

                word_manual_list = Smart_File.Find_dir_format(Manual_route_data,".txt")
                word_manual_len = len(word_manual_list)
                for i in range(1,line+1):
                    word_listbox.delete(0)

                line = 1
                for name in word_manual_list:
                   word_listbox.insert(line, name)
                   line = line + 1
            except:
                mb.showinfo('error','단어를 선택해주세요.',parent=wi)

        del_button = tkinter.Button(wi_del, text = "삭제", overrelief="solid",
                                   height = 1,width=18, command=do_del,
                                   bg = 'burlywood1')
        del_button.pack()
        wi_del.geometry("+%d+%d" % (300,150))

    delete_button=tkinter.Button(wi, text = "단어삭제", overrelief="solid",
                                   height = 1,width=8, command=Del_word,
                                   bg = 'burlywood1')
    delete_button.place(x=485,y=176)
    ################################ word delete end ###################################
    #------------------------------ back button --------------------------------
    back = tkinter.Button(wi,text = "뒤로가기", overrelief="solid", height = 3,width=200,
                          repeatdelay=100,bg = 'burlywood1',
                          repeatinterval=100,command=Close_double)
    back.bind("<Button-1>", Close)
    back.pack(side = "bottom")

    frame_keyboard=tkinter.Frame(wi, bg = 'tan')#keyboard
    Make_button(frame_keyboard)
    frame_keyboard.pack(side = "bottom")
    frame_top.pack(side = "right")

    #----------------------------------wifi list---------------------------------
    frame_left = tkinter.Frame(top_grid_frame,bg = '#222b3f')
    frame_wifi = tkinter.Frame(frame_left,bg = '#222b3f')#wifi list

    def Ins_double():
        try:
            item = listbox.curselection()
            index = item[0]
            text_ssid.delete(0,30)
            text_ssid.insert(0,Wifi_list[index])

        except:
            #voice_timmer("Miss","선택실패",5)
            mb.showinfo('error','와이파이를 선택해주세요.',parent=wi)

    def Search():
        global Wifi_list
        Wifi_list = []
        cells = wifi.Cell.all('wlan0')

        for cell in cells:
            Wifi_list.append(cell.ssid)

    scrollbar = tkinter.Scrollbar(frame_wifi,bg = '#222b3f')
    scrollbar.pack(side="right", fill="y")
    listbox=tkinter.Listbox(frame_wifi, yscrollcommand = scrollbar.set,height=7)
    line = 1

    for name in Wifi_list:
       listbox.insert(line, name)
       line = line + 1

    def Retry_double():
        global line, Wifi_list
        for i in range(1,line+1):
            listbox.delete(0)

        Search()
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

    button_retry = tkinter.Button(frame_id_insert, text = "검색", overrelief="solid",
                                  height = 1,width=8, command=Retry_double,
                                  bg = 'burlywood1')
    button_retry.pack(side="right") 

    frame_id_insert.pack()
    frame_under_list.grid(row = 1, column = 0)#grid
    frame_left.pack(side = "left")
    #------------------------------- wifi list end -------------------------------
    top_grid_frame.pack(pady=40) #맨위에 여백
#-------------------------- 와이파이 관련 함수 끝-------------------------------

#------------------------ 단어 학습 top level에 관한 함수 ----------------------
def Word_education(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Word","단어학습",2)

def Word_education_double():
    global long_click_flag, font_1
    if(time.time() - long_click_flag < 2.5):
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
    frame_edu.pack(side = "top", anchor = 'c',expand=True)

    button1 = tkinter.Button(frame_edu, text="교통수단",command = Traffic_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 22, width = 25, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button1.bind("<Button-1>", Traffic)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_edu, text="음식",command = Food_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 22, width = 24, highlightcolor='#222b3f',activebackground='burlywood1',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = 'burlywood1')
    button2.bind("<Button-1>", Food)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_edu, text="장소",command = Location_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 22, width = 24, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button3.bind("<Button-1>", Location)
    button3.grid(row = 0, column = 2)

    button4 = tkinter.Button(frame_edu, text="사용자 지정",command = User_word_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 22, width = 25, highlightcolor='#222b3f',activebackground='burlywood1',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = 'burlywood1')
    button4.bind("<Button-1>", User_word)
    button4.grid(row = 0, column = 3)

    #뒤로가기 버튼
    frame_sel_exit = tkinter.Frame(Jamo, background = "burlywood1")
    frame_sel_exit.pack(side = "bottom", anchor = 'c')
    button5 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100, highlightbackground = '#ffffff',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 5, width = 215, highlightcolor='#ffffff',activebackground='#ffffff',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = '#ffffff')
    button5.bind("<Button-1>", Close)
    button5.pack()
#------------------------ 단어 학습 top level에 관한 함수 끝 ----------------------

#------------------------ 자율 학습 top level에 관한 함수 ----------------------
def Free_study(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Free","수동모드", 3)

def Free_study_double():
    global long_click_flag
    if(time.time() - long_click_flag < 2):
        return
    voice_timmer("Move","이동완료",1) 
    long_click_flag = time.time()
    #모터 초기화 합시다.
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
        voice_timmer("Move","이동완료",1)
        srv.clear_all(kit_list)
        free.destroy()
    free.bind("<F11>", Close_double)

    num = []
    for i in range(0,72):
        num.append(tkinter.IntVar())
    #################### 수동모드에서 설정한 값을 모터에 넘기는 함수 #######################
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
            #print(num[i].get(), end='')
        srv.active(d_list,kit_list)
    #################### 수동모드에서 설정한 값을 모터에 넘기는 함수 끝 #######################

    ############## 각 칸에 이름은 같지만 동작이 다른 함수를 맵핑 ########################
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
                                width = 5,
                                height = 3).grid(row = (r//2), column = c)
            index += 1
        i += 1
        return i, index
    ############## 각 칸에 이름은 같지만 동작이 다른 함수를 맵핑 끝 #####################

    ####################################################################
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
    frame_button.pack(anchor = 'c',expand=True)
    #-------------------------------------------------------------------
    frame_button_r = tkinter.Button(frame_button,
                                    text = "뒤로가기",
                                    overrelief="solid",
                                    height = 4,
                                    width=53,
                                    repeatdelay=100,
                                    repeatinterval=100,
                                    background = "burlywood1",
                                    command=Close_double)
    frame_button_r.pack(side = "left",anchor = 'c',expand=True)
    frame_button_r.bind("<Button-1>", Close)
    #-------------------------------------------------------------------
    frame_button_l = tkinter.Button(frame_button,
                                    text = "적용",
                                    overrelief="solid",
                                    height = 4,
                                    width=53,
                                    command=Sel_double,
                                    repeatdelay=100,
                                    repeatinterval=100,
                                    background = "burlywood1")
    frame_button_l.pack(side = "right",anchor = 'c',expand=True)
    frame_button_l.bind("<Button-1>",Sel)

#------------------------ 자음모음 및 약자 학습 top level에 관한 함수 ----------------------
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
    #------------------------------------------------------------
    Jamo = tkinter.Toplevel(background = "tan", cursor='none')
    Jamo.geometry("800x480")
    Jamo.attributes("-fullscreen", True)

    def Close(event=None):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Close","back",2)
    def Close_double(event = None):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1)
        Jamo.destroy()
    Jamo.bind("<F11>", Close_double)

    #자음, 모음, 약자에 관한 버튼을 만들어주는 함수
    def Simple_word_maker(simple_list, simple_var, parent,j):
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        voice_timmer("Move","이동완료",1) 
        Sung = tkinter.Toplevel(background = "tan",cursor='none')
        Sung.geometry("800x480")
        Sung.attributes("-fullscreen", True)
        Sung_frame = tkinter.Frame(Sung,background = "tan")
        Sung_frame.pack(side = "top", anchor = 'c',expand=True)
        sung_index = 0

        def Map_act(x):
            voice_timmer("Simple_"+str(x), simple_list[x], 1.7)
            d_list = []
            print(simple_var[x])
            for i in simple_var[x]:
                d_list.append(int(i))
            [d_list.append(0) for i in range(72-len(d_list))]
            #print(d_list) #확인
            srv.active(d_list,kit_list)
        if j == 0 or j == 2:
            w=15
            h=11
        elif j == 1:
            w=15
            h=7
        elif j == 3:
            w=11
            h=7
        else:
            w=37
            h=11
        for x in range(t_x[j]):
            for y in range(t_y[j]):
                if j == 3:
                    if sung_index>26:
                        break
                act = lambda x = sung_index : Map_act(x)
                if(sung_index%2):
                    color_= 'tan1'
                else:
                    color_= 'burlywood1'
                tkinter.Button(Sung_frame,text = simple_list[sung_index],
                                bg = color_,
                                padx = 1,
                                pady = 1,
                                height = h,
                                width = w,
                                command = act).grid(row = (x), column = y)
                sung_index += 1

        #------뒤로가기랑 초기 화면으로 부분------
        def Close_top(event):
            global long_click_flag
            long_click_flag = time.time()
            voice_timmer("Close","back",3)

        def Close_top_double(event=None):
            global long_click_flag
            if(time.time() - long_click_flag < 2):
                return
            voice_timmer("Move","이동완료",1)
            srv.clear_all(kit_list)
            Sung.destroy()
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
            voice_timmer("Move","이동완료",1)
            srv.clear_all(kit_list)
            Sung.destroy()
            parent.destroy()

        Sung.bind("<F11>", Close_top_double)

        frame_sel_exit = tkinter.Frame(Sung, background = "tan")
        frame_sel_exit.pack(side = "bottom", anchor = 'c')
        button1 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_top_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 55,
                                 background = 'tan1')
        button1.bind("<Button-1>", Close_top)
        button1.pack(side = "left");

        button2 = tkinter.Button(frame_sel_exit, text="초기 화면으로",command = Initialize_double,
                                 repeatdelay=100,
                                 repeatinterval=100,
                                 height = 3, width = 55,
                                 background = 'tan1')
        button2.bind("<Button-1>", Initialize)
        button2.pack(side = "right");
    #------초성 파트------
    def Chosung(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Cho","초성",3)

    def Chosung_double():
        Simple_word_maker(simple_k_list[0],simple_d_list[0],Jamo,0)

    #------모음 파트------
    def Moum(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Moum","모음",3)

    def Moum_double():
        Simple_word_maker(simple_k_list[1],simple_d_list[1],Jamo,1)

    #------종성 파트------
    def jongsung(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Jong","종성",3)

    def jongsung_double():
        Simple_word_maker(simple_k_list[2],simple_d_list[2],Jamo,2)

    #------1종 약자 파트------
    def simple_h1(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Simple","1종약자",3)

    def simple_h1_double():
        Simple_word_maker(simple_k_list[3],simple_d_list[3],Jamo,3)

    #------2종 약자 파트------
    def simple_h2(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("Simple","2종약자",3)

    def simple_h2_double():
        Simple_word_maker(simple_k_list[4],simple_d_list[4],Jamo,4)

    Jamo.bind("<F11>", Close_double)
    #---------초성 모음 종성 약자 -----------------
    frame_edu = tkinter.Frame(Jamo, background = "tan")
    frame_edu.pack(side = "top", anchor = 'c',expand=True)
    button1 = tkinter.Button(frame_edu, text="초성",command = Chosung_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 22, width = 19,
                             background = 'burlywood1')
    button1.bind("<Button-1>", Chosung)
    button1.grid(row = 0, column = 0)

    button2 = tkinter.Button(frame_edu, text="모음",command = Moum_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 22, width = 19,
                             background = 'tan1')
    button2.bind("<Button-1>", Moum)
    button2.grid(row = 0, column = 1)

    button3 = tkinter.Button(frame_edu, text="종성",command = jongsung_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 22, width = 19,
                             background = 'burlywood1')
    button3.bind("<Button-1>", jongsung)
    button3.grid(row = 0, column = 2)

    button4 = tkinter.Button(frame_edu, text="1종 약자",command = simple_h1_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 22, width = 19,
                             background = 'tan1')
    button4.bind("<Button-1>", simple_h1)
    button4.grid(row = 0, column = 3)

    button5 = tkinter.Button(frame_edu, text="2종 약자",command = simple_h2_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 22, width = 19,
                             background = 'burlywood1')
    button5.bind("<Button-1>", simple_h2)
    button5.grid(row = 0, column = 4)

    #뒤로가기 버튼
    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")
    frame_sel_exit.pack(side = "bottom", anchor = 'c')
    button5 = tkinter.Button(frame_sel_exit, text="뒤로가기",command = Close_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 3, width = 120,
                             background = 'tan3')
    button5.bind("<Button-1>", Close)
    button5.pack();
#------------------------ 자음모음 및 약자 학습 top level에 관한 함수 끝 ----------------------

#------------------------ 단어 등록 top level에 관한 함수 ----------------------
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

    #저장 여부를 마이크에 대고 말하면 이식하는 함수. ex) 네, 그래
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
                    print(data)
                    for _ in dc.convert_dot(data):
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

    #마이크에 단어를 입력받고 점자로 변환해주는 함수
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
            #보드에서 표현 가능한 단어인지 확인
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
                print(cnt, '<- 점자수')

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
#------------------------ 단어등록 학습 top level에 관한 함수 끝 ----------------------

#------------------------ 종료 관련 top level에 관한 함수 ----------------------
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
    srv.clear_all(kit_list)
    long_click_flag = time.time()
#------------------------ 종료 관련 top level에 관한 함수 끝 ----------------------

#------------------------ 퀴즈 관련 top level에 관한 함수 ----------------------
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
        srv.clear_all(kit_list)
        Quiz.destroy()
    Quiz.bind("<F11>", Close_double)

    #사용자 단어를 제외한 세 파트의 단어 중 한개를 랜덤으로 선택하여 퀴즈를 만드는 함수
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
        srv.active(d_list,kit_list)
        return r_k_data.replace('.txt',''), d_list, q_v_route

    now_data_k, now_data_b, now_voice_route = make_quize()

    #다음 퀴즈에 관한 함수
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
        button_answer.configure(text="정답 말하기\n(%s)"%now_data_k)

    # 마이크에 정답을 말하면 값을 읽어오는 함수
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
            if now_data_k.replace(' ','') in string.replace(' ',''):
                os.system(mp3_route+"문제정답.mp3")
                now_data_k, now_data_b, now_voice_route = make_quize()
                button_answer.configure(text="정답 말하기\n(%s)"%now_data_k)
            else:
                os.system(mp3_route+"문제오답.mp3")
        except:
            os.system(mp3_route+"단어분석실패.mp3")

    #정답을 확인하는 함수
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
                             height = 13, width = 53,
                             background = 'burlywood1')
    button_back.bind("<Button-1>", Close)

    button_answer = tkinter.Button(frame_sel_exit, text="정답 말하기\n(%s)"%now_data_k,command = answer_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 13, width = 53,
                             background = 'tan1')
    button_answer.bind("<Button-1>", answer)

    button_confirm = tkinter.Button(frame_sel_exit, text="정답 확인",command = confirm_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 13, width = 53,
                             background = 'tan1')
    button_confirm.bind("<Button-1>", confirm)

    button_next_q = tkinter.Button(frame_sel_exit, text="다음 문제",command = next_q_double,
                             repeatdelay=100,
                             repeatinterval=100,
                             relief = 'solid',
                             height = 13, width = 53,
                             background = 'burlywood1')
    button_next_q.bind("<Button-1>", next_q)
    button_back.grid(row=1,column=0);
    button_next_q.grid(row=0,column=1);
    button_confirm.grid(row=1,column=1);
    button_answer.grid(row=0,column=0);
#------------------------ 퀴즈 관련 top level에 관한 함수 끝 ----------------------

#------------------------ 업데이트 관련 top level에 관한 함수 ----------------------
def Update(event):
    global long_click_flag
    long_click_flag = time.time()
    voice_timmer("Update","업데이트",3)

def Update_double():
    global long_click_flag,word_food_list,word_food_len,word_location_list,word_location_len\
           ,word_trf_list,word_trf_len,d_list,v_list
    if(time.time() - long_click_flag < 2):
        return
    voice_timmer("Move","업데이트시작",4)
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
            os.system(mp3_route+"업데이트완료.mp3")
        else:
            os.system(mp3_route+"최신버전.mp3")
    except:
        voice_timmer("warning","서버경고",7)
#------------------------ 업데이트 관련 top level에 관한 함수 끝 ----------------------

if __name__ == '__main__':
    global window, font_1
    #로고 음악 출력 -> edu_dot_main.py를 통해 졸업작품을 실행하면 로고 송이 나오게 함
    #os.system("python3 ~/dip/logo.py")
    window=tkinter.Tk()
    window.title("Graduation Project")
    window.geometry("800x480")

    window.configure(background='#222b3f', cursor='none')
    window.attributes("-fullscreen", True)

    font_1=tkinter.font.Font(family="맑은 고딕", size=9,weight='bold')

    #혹시 모를 상황을 대비해 F11에 전체화면 토글 함수를 맵핑
    def toggle_fullscreen(event=None):
        window.state = not window.state  # Just toggling the boolean
        window.attributes("-fullscreen", window.state)
        return "break"    
    window.bind("<F11>", toggle_fullscreen)

    frame1=tkinter.Frame(window,background="#222b3f")
    button1 = tkinter.Button(frame1, text="설정",command = Connect_wifi_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 13, width = 25, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button1.bind("<Button-1>", Connect_wifi)

    button2 = tkinter.Button(frame1, text="단어 학습",command = Word_education_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 13, width = 24, highlightcolor='#222b3f',activebackground='#ffffff',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = '#ffffff')
    button2.bind("<Button-1>", Word_education)

    button3 = tkinter.Button(frame1, text="자음,모음 및 약자 학습", command = jamo_edu_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 13, width = 24, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button3.bind("<Button-1>", jamo_edu)

    button4 = tkinter.Button(frame1, text="업데이트", command = Update_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 13, width = 25, highlightcolor='#222b3f',activebackground='#ffffff',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = '#ffffff')
    button4.bind("<Button-1>", Update)

    button5 = tkinter.Button(frame1, text="수동 모드", command = Free_study_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 13, width = 24, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button5.bind("<Button-1>", Free_study)

    button6 = tkinter.Button(frame1, text="단어 등록",command = Regist_word_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 13, width = 24, highlightcolor='#222b3f',activebackground='#ffffff',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = '#ffffff')
    button6.bind("<Button-1>", Regist_word)

    button7 = tkinter.Button(frame1, text="사용 종료", command = exit_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#c8a780', highlightthickness=1,
                             height = 13, width = 25, highlightcolor='#222b3f',activebackground='#222b3f',
                             relief = 'solid',activeforeground='#c8a780',font = font_1,
                             background = '#222b3f')
    button7.bind("<Button-1>", exit_)

    button8 = tkinter.Button(frame1, text="문제풀기", command = quiz_double,
                             repeatdelay=100, highlightbackground = '#c8a780',
                             repeatinterval=100, fg = '#222b3f', highlightthickness=1,
                             height = 13, width = 25, highlightcolor='#222b3f',activebackground='#ffffff',
                             relief = 'solid',activeforeground='#222b3f',font = font_1,
                             background = '#ffffff')

    button8.bind("<Button-1>", quiz)

    button1.grid(row = 0, column = 0)
    button2.grid(row = 0, column = 1)
    button3.grid(row = 0, column = 2)
    button4.grid(row = 1, column = 0)
    button5.grid(row = 1, column = 1)
    button6.grid(row = 1, column = 2)

    button8.grid(row = 0, column = 3)
    button7.grid(row = 1, column = 3)
     #왼쪽 마우스 버튼 바인딩
    frame1.pack(expand=True);
    window.mainloop()

