# -*- coding: utf-8 -*-

import tkinter 

import time

import Smart_File

import wifi

import voice

import os

 

class Finder:

    def __init__(self, *args, **kwargs):

        self.server_name = kwargs['server_name']

        self.password = kwargs['password']

        self.interface_name = kwargs['interface']

        self.main_dict = {}

 

    def run(self):

        command = """sudo iwlist wlp2s0 scan | grep -ioE 'ssid:"(.*{}.*)'"""

        result = os.popen(command.format(self.server_name))

        result = list(result)

 

        if "Device or resource busy" in result:

            print("buzy")

            return None

        else:

            ssid_list = [item.lstrip('SSID:').strip('"\n') for item in result]

            print("Successfully get ssids {}".format(str(ssid_list)))

 

        for name in ssid_list:

            try:

                result = self.connection(name)

            except Exception as exp:

                print("Couldn't connect to name : {}. {}".format(name, exp))

            else:

                if result:

                    print("Successfully connected to {}".format(name))

 

    def connection(self, name):

        try:

            os.system("nmcli d wifi connect {} password {} iface {}".format(name,

       self.password,

       self.interface_name))

        except:

            raise

        else:

            return True

 

window=tkinter.Tk()

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

 

word_list = Smart_File.Find_dir_format("./dot_data/",".txt")

word_len = len(word_list)

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

    

    '''

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

        print("Ű���� �ش��ϴ� �������")

    '''

 

 

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

        os.system("mpg321 ./sound/"+sound+".mp3")

    else:

        if(time.time() - voice_flags.get(key,0) > minute):

            voice_flags[key] = time.time() 

            os.system("mpg321 ./sound/"+sound+".mp3") 

    

def Connect_wifi(event):

    global long_click_flag

    long_click_flag = time.time()

    print("�������̿��� ���� ���")

    voice_timmer("Wifi","wifi_toplevel",5)

            

def Connect_wifi_double():

    global line, text_pw, long_click_flag, text_ssid

    if(time.time() - long_click_flag < 2):

        return

    Wifi_list = []

    voice_timmer("Move","�̵��Ϸ�",1) 

    print("�̵� ���� ���")

    long_click_flag = time.time()

    wi = tkinter.Toplevel(bg = 'tan')

    wi.attributes("-fullscreen", True)

 

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

        voice_timmer("Connecnt_try","���ӽõ�",2)

        print(text_pw.get(), text_ssid.get())

        F = Finder(server_name=text_ssid.get(),

                   password=text_pw.get(),

                   interface='wlan0')

        F.run

        '''

        cell = wifi.Cell.all('wlan0')[0]

        scheme = wifi.Scheme.for_cell('wlan0', text_ssid.get(), cell, text_pw.get())

        scheme.save()

        scheme.activate()

        '''

        wi.destroy()

 

        

        

        

    wi.bind("<F11>", Close_double)

    #------------------------------------top--------------------------------

    frame_top = tkinter.Frame(wi,bg = 'tan')

 

    frame_back=tkinter.Frame(frame_top,bg = 'burlywood1')#back,id,pw input

    back = tkinter.Button(frame_back,text = "�ڷΰ���", overrelief="solid", height = 1,width=8,

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

    button_connect = tkinter.Button(frame_button, text = "����", overrelief="solid", height = 1,width=8,

                                    bg = 'burlywood1',command=Connect_double)

    button_connect.pack()

    

    frame_button.grid(row=0,column=2)#grid

    

    frame_top.pack(side = "top")

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

            voice_timmer("Miss","���ý���",5)

        

    def Search():

        wifilist = []

        cells = wifi.Cell.all('wlan0')

 

        for cell in cells:

            cell = str(cell)

            temp = cell.split('=')

            st = temp[1]

            wifilist.append(st[0:-1])

        return wifilist

    

    scrollbar = tkinter.Scrollbar(frame_wifi, command = scroll_voice,bg = 'tan')#����

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

 

    #---------------------------------right---------------------------------

    frame_keyboard=tkinter.Frame(wi, bg = 'tan')#keyboard

    Make_button(frame_keyboard)

    frame_keyboard.pack(side = "right")

    #-----------------------------------------------------------------------

 

def Word_education(event):

    global long_click_flag

    long_click_flag = time.time()

    voice_timmer("Word","�ܾ��н�",5)

    

def Word_education_double():

    #voice_timmer("demo","����",5)

    global word_list, word_index, word_double_flag, word_len, long_click_flag

 

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    

    word_index = 0

    Word = tkinter.Toplevel()

    Word.attributes("-fullscreen", True)

    

    def Close(event=None):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Close","back",3.5)

 

    def Close_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        Word.destroy()

        voice_timmer("Move","�̵��Ϸ�",1) 

        long_click_flag = time.time()

 

 

        

    Word.bind("<F11>", Close_double)

 

    def scroll_voice():

        voice_timmer("Scroll","��ũ��",5)#����

 

    def Next(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Next","����������",5)

     

    def Next_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        voice_timmer("Push","��ư����",1)

        

        if(word_index < word_len):

            print("���� ������ ����ϴµ� ������ ���Ƶΰڽ��ϴ�.")

        else:

            voice_timmer("Last","������������",5)

        long_click_flag = time.time()   

            

    def Sel_double(event=None):

        global word_double_flag, long_click_flag

        long_click_flag = time.time()

        word_double_flag = 1

        

        if(time.time() - long_click_flag < 2):

            return

        voice_timmer("Push","��ư����",1)

        

        

    def Map_wrd(x):

        global word_double_flag, long_click_flag

        if(word_double_flag):

            voice_timmer(x[0],x[0],2)

            word_double_flag = 0

        else:

            if(time.time() - long_click_flag < 3):

                return

            data = Smart_File.Read_file("./dot_data/",word_list[x[1]]).split('\n')

            print("-----------------------------------------------")

            print("�ܾ� : " + word_list[x[1]])

            print("���� �� : " + str(data[0]))

            print("Dot data : " + str(data[1]))

            voice_timmer("Select","�ܾ�ÿϷ�",5)

            #print(word_list[x[1]])

            sleep(2)

            long_click_flag = time.time()

 

    def make_button(index, frame):

        global wrd

        for r in range(0,4):

            for c in range(0,4):

                if(index < word_len):

                    wrd = lambda x = [str(word_list[index].replace(".txt","")), index]: Map_wrd(x)

                    word_button = tkinter.Button(frame,

                                        text = str(word_list[index].replace(".txt","")),

                                        overrelief="solid",

                                        height = 1,

                                        width=8,

                                        repeatdelay=100,

                                        repeatinterval=100,

                                        command=wrd)

                    word_button.bind("<Button-1>",Sel_double)

                    word_button.grid(row = r, column = c)

                    index = index + 1

                else:

                    break

        return index

                

    #----------------------------------------------------------------------

    frame_word = tkinter.Frame(Word)

    word_index = make_button(word_index, frame_word)

    frame_word.pack(anchor = 'c',padx = 30, pady = 30)

    #----------------------------------------------------------------------

    #----------------------------------------------------------------------

    frame_button = tkinter.Frame(Word)

    frame_button.pack(anchor = 'c',padx = 30, pady = 10)

    #-------------------------------------------------------------------

    frame_button_r = tkinter.Button(frame_button,

                                    text = "�ڷΰ���",

                                    overrelief="solid",

                                    height = 1,

                                    width=8,

                                    repeatdelay=100,

                                    repeatinterval=100,

                                    command=Close_double)

    frame_button_r.pack(side = "left",anchor = 'c',padx = 3, pady = 3)

    frame_button_r.bind("<Button-1>", Close)

    #-------------------------------------------------------------------

    frame_button_l = tkinter.Button(frame_button,

                                    text = "���� ������",

                                    overrelief="solid",

                                    height = 1,

                                    width=8,

                                    repeatdelay=100,

                                    repeatinterval=100,

                                    command=Next_double)

    frame_button_l.pack(side = "right",anchor = 'c',padx = 3, pady = 3)

    frame_button_l.bind("<Button-1>",Next)

    frame_button.pack(anchor = 'c',padx = 3, pady = 3)

    #----------------------------------------------------------------------

    

def Regist_word():

    voice_timmer("Regist","�ܾ���",5)

    #����� �ܾ�� ������Ʈ�ص� �� �������� ¥���Ѵ�.

    

def Regist_word_double(event):

    voice_timmer("Demo","����",5)

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

    voice_timmer("Update","������Ʈ",5)

 

def Update_double(event):

    #os.system("mpg321 ./sound/����.mp3")

    try:

        A = fff+123

        #�Ϻη� �ȵǴ� �ڵ� �������, ���ͳ��� ����ȵǰų� ������ ���� �������� ����Ǵºκ�

    except:

        voice_timmer("warning","�������",7)

        #pass

    '''

    Up = tkinter.Toplevel()

    def Check():

        pass      

    def Check_double(event):

        Up.destroy()

    Up.title("����")

    Up.geometry("400x240+200+120")

    frame_la = tkinter.Frame(Up)

    label=tkinter.Label(frame_la, text="������ �����ְų� �������̰� ����Ǿ����� �ʽ��ϴ�.")

    label.grid(row = 0 , column = 0, pady="3m")

    button_la=tkinter.Button(frame_la, text = "Ȯ��", overrelief="solid", height = 1,width=8, command=Check)

    button_la.bind("<Double-Button-1>", Check_double)

    button_la.grid(row = 1 , column = 0, pady="3m")

    frame_la.pack(padx = "3m",pady="15m")

    voice_timmer("warning","�������",7)

    '''

  

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

    free = tkinter.Toplevel(background = "tan")

    free.attributes("-fullscreen", True)

    def Close(event=None):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Close","back",3)

    def Close_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

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

        voice_timmer("Select","����Ϸ�",5) 

        

        for i in range(0,72):

            print(num[i].get(), end='')

        #�ӽ÷� ���� ����ϴ� �Լ���

          

    def Map_vos(x):

        global toggle_flag

        if(toggle_flag.get(str(x[0])+str(x[1]),0) == 0):

            toggle_flag[str(x[0])+str(x[1])] = 1

            os.system("mpg321 ./sound/"+str(x[0])+str(x[1])+"1.mp3")

        else:

            toggle_flag[str(x[0])+str(x[1])] = 0

            os.system("mpg321 ./sound/"+str(x[0])+str(x[1])+"2.mp3")

        

  

    def Button_in(frame,i,index):

        for r in range(6):

            vos = lambda x = [i,r+1] : Map_vos(x)

            if((r+1) % 2):

                c=0

            else:

                c=1

            tkinter.Checkbutton(frame,

                                variable=num[index],

                                bg = "tan",

                                padx = 1,

                                pady = 1,

                                command=vos,

                                width = 3,

                                height = 2).grid(row = (r//2), column = c)

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

    frame_up.pack(side = "top",anchor = 'c',padx = 3, pady = 3,fill="both")

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

    frame_button.pack(anchor = 'c',padx = 30, pady = 10)

    #-------------------------------------------------------------------

    frame_button_r = tkinter.Button(frame_button,

                                    text = "�ڷΰ���",

                                    overrelief="solid",

                                    height = 1,

                                    width=8,

                                    repeatdelay=100,

                                    repeatinterval=100,

                                    background = "tan",

                                    command=Close_double)

    frame_button_r.pack(side = "left",anchor = 'c',padx = 3, pady = 3)

    frame_button_r.bind("<Button-1>", Close)

    #-------------------------------------------------------------------

    frame_button_l = tkinter.Button(frame_button,

                                    text = "����",

                                    overrelief="solid",

                                    height = 1,

                                    width=8,

                                    command=Sel_double,

                                    repeatdelay=100,

                                    repeatinterval=100,

                                    background = "tan")

    frame_button_l.pack(side = "right",anchor = 'c',padx = 3, pady = 3)

    frame_button_l.bind("<Button-1>",Sel)

  

def jamo_edu(event):

    global long_click_flag

    long_click_flag = time.time()

    voice_timmer("Jamo","�ڸ��н�",3)

 

def jamo_edu_double():

    global long_click_flag

    if(time.time() - long_click_flag < 2):

        return

    voice_timmer("Move","�̵��Ϸ�",1) 

    long_click_flag = time.time()

    #���� �ʱ�ȭ �սô�.

    #voice_timmer("demo","����",5)

    #------------------------------------------------------------

    Jamo = tkinter.Toplevel(background = "tan")

    Jamo.attributes("-fullscreen", True)

    

    def Close(event=None):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Close","back",3)

    def Close_double(event = None):

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

        voice_timmer("Move","�̵��Ϸ�",1)

        Jamo.destroy()

 

    def Chosung(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Cho","�ʼ�",3)

 

    #------�ʼ� ��Ʈ------

    def Chosung_double():

        global long_click_flag

        if(time.time() - long_click_flag < 2):

            return

       

        voice_timmer("Move","�̵��Ϸ�",1) 

        Chosung = tkinter.Toplevel(background = "tan")

        Chosung.attributes("-fullscreen", True)

        char_list = ['��','��','��','��','��','��','��','��','��','��','��','��','��']

 

 

        #------�ڷΰ���� �ʱ� ȭ������ �κ�------

        def Close_top(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Close","back",3)

            

        def Close_top_double(event=None):

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

            voice_timmer("Move","�̵��Ϸ�",1) 

            Chosung.destroy()

 

        def Initialize(event):

            global long_click_flag

            long_click_flag = time.time()

            voice_timmer("Initial","�ʱ�ȭ��",3)

            

        def Initialize_double():

            global long_click_flag

            if(time.time() - long_click_flag < 2):

                return

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

    def Moum_double():

        pass

    

    def jongsung(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Jong","����",3)

    def jongsung_double():

        pass

    

    def simple_house(event):

        global long_click_flag

        long_click_flag = time.time()

        voice_timmer("Simple","����",3)

 

    def simple_house_double():

        pass

        

        

    Jamo.bind("<F11>", Close_double)

    #---------�ʼ� ���� ���� ���� -----------------

    frame_edu = tkinter.Frame(Jamo, background = "tan")

    frame_edu.pack(side = "top", anchor = 'c',padx = 3, pady = 3)

    button1 = tkinter.Button(frame_edu, text="�ʼ�",command = Chosung_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button1.bind("<Button-1>", Chosung)

    button1.grid(row = 0, column = 0)

 

    button2 = tkinter.Button(frame_edu, text="����",command = Moum_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button2.bind("<Button-1>", Moum)

    button2.grid(row = 0, column = 1)

 

    button3 = tkinter.Button(frame_edu, text="����",command = jongsung_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button3.bind("<Button-1>", jongsung)

    button3.grid(row = 0, column = 2)

 

    button4 = tkinter.Button(frame_edu, text="����",command = simple_house_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button4.bind("<Button-1>", simple_house)

    button4.grid(row = 0, column = 3)

 

    #�ڷΰ��� ��ư

    

    frame_sel_exit = tkinter.Frame(Jamo, background = "tan")

    frame_sel_exit.pack(side = "bottom", anchor = 'c',padx = 10, pady = 3)

    button5 = tkinter.Button(frame_sel_exit, text="�ڷΰ���",command = Close_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 3, width = 15,

                             background = 'tan1')

    button5.bind("<Button-1>", Close)

    button5.pack();

 

    #voice_timmer("demo","����",5)

 

def exit_(event):

    global long_click_flag

    long_click_flag = time.time() 

    voice_timmer("Exit","�������",3)

 

def exit_double():

    global long_click_flag

    if(time.time() - long_click_flag < 3):

        return

    voice_timmer("Exit_true","����������մϴ�",3)

    window.destroy()

    long_click_flag = time.time()

    #motor �� ������

    #os.~~~ exit

 

if __name__ == '__main__':

    window.title("Graduation Project")

    window.geometry("640x400+100+100")

    window.configure(background='tan')

 

    #���� ����� ���� �ʱ�ȭ �� ��������

    #window.resizable(False, False)

    #frame = Frame(window, width=600, height=300)

 

    def toggle_fullscreen(event=None):

        window.state = not window.state  # Just toggling the boolean

        window.attributes("-fullscreen", window.state)

        return "break"    

    window.bind("<F11>", toggle_fullscreen)

 

    frame1=tkinter.Frame(window,background="tan")

    button1 = tkinter.Button(frame1, text="�������� ����",command = Connect_wifi_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button1.bind("<Button-1>", Connect_wifi)

    button2 = tkinter.Button(frame1, text="�ܾ� �н�", command = Word_education_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = "burlywood1")

 

    button2.bind("<Button-1>", Word_education)

 

    button3 = tkinter.Button(frame1, text="����,���� �� ���� �н�", command = jamo_edu_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = 'tan1')

    button3.bind("<Button-1>", jamo_edu)

    

    button4 = tkinter.Button(frame1, text="������Ʈ", command = Update, height = 10, width = 18)

    button4.bind("<Double-Button-1>", Update_double)

    

    button5 = tkinter.Button(frame1, text="���� ���", command = Free_study_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = "burlywood1")

    button5.bind("<Button-1>", Free_study)

    

    button6 = tkinter.Button(frame1, text="�ܾ� ���", command = Regist_word, height = 10, width = 18)

    button6.bind("<Double-Button-1>", Regist_word_double)

    

    button7 = tkinter.Button(frame1, text="��� ����", command = exit_double,

                             repeatdelay=100,

                             repeatinterval=100,

                             height = 10, width = 18,

                             background = "burlywood1")

 

    button7.bind("<Button-1>", exit_)

 

    

    button1.grid(row = 0, column = 0)

    button2.grid(row = 0, column = 1)

    button3.grid(row = 0, column = 2)

    button4.grid(row = 1, column = 0)

    button5.grid(row = 1, column = 1)

    button6.grid(row = 1, column = 2)

 

    button7.grid(row = 0, column = 3)

     #���� ���콺 ��ư ���ε�

    frame1.pack();

    window.mainloop()