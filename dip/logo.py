# -*- coding: utf-8 -*-
import tkinter
import time
import threading
import os
route = "/home/pi/dip/logo"
logo_name = 'Edu.DotLogo.00%d'%1
if __name__ == '__main__':
    global window, canvas
    
    pre = tkinter.Tk()
    pre.title("joo")
    pre.attributes("-fullscreen", True)
    pre.configure(background='tan', cursor='none')
    img1 = tkinter.PhotoImage(file='/home/pi/dip/logo/dot_img1.gif')
    arr = [tkinter.PhotoImage(file='/home/pi/dip/logo/Edu.DotLogo.%03d.gif'%(i+1)) for i in range(54)]

    def timer(a,t):
        global canvas
        flag = 1
        i=0
        def voice():
            os.system("mpg321 /home/pi/dip/sound/로고음성.mp3")    
        thread = threading.Thread(target=voice)
        thread.daemon = True 
        
        while(1):
            if(time.time() - t > 5):
                break
            elif((time.time() - t >1) and flag):
                thread.start()
                flag = 0
            elif(i<54):
                #canvas=tkinter.Canvas(pre,width = 800, height = 480)
                canvas.create_image(0, 0, anchor = tkinter.NW, image =arr[i])
                #canvas.pack()
                i+=1
                time.sleep(0.0025)
        a.destroy()
        del a
    
    
    canvas=tkinter.Canvas(pre,width = 800, height = 480,bg='white')
    canvas.create_image(0, 0, anchor = tkinter.NW, image =img1)
    canvas.pack()
    a = time.time()
    th = threading.Thread(target=timer, args=(pre,a))
    th.daemon = True 
    th.start()
    
    pre.mainloop()

