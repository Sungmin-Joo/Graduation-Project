from adafruit_servokit import ServoKit


####################### lim's code  ########################
def setup():
    return
    kit0 = ServoKit(address=0x40, channels=16)
    kit0.servo[0].set_pulse_width_range(480,2480)
    kit0.servo[1].set_pulse_width_range(450,2450)
    kit0.servo[2].set_pulse_width_range(400,2400)
    kit0.servo[3].set_pulse_width_range(400,2400)
    #===========================================
    kit0.servo[4].set_pulse_width_range(600,2600)
    kit0.servo[5].set_pulse_width_range(550,2550)
    kit0.servo[6].set_pulse_width_range(550,2550)
    kit0.servo[7].set_pulse_width_range(550,2550)
    #===========================================
    kit0.servo[8].set_pulse_width_range(600,2600)
    kit0.servo[9].set_pulse_width_range(450,2450)
    kit0.servo[10].set_pulse_width_range(590,2590)
    kit0.servo[11].set_pulse_width_range(400,2400)
    #=================================================== B - 0x40
    
    kit1 = ServoKit(address=0x41, channels=16)
    kit1.servo[0].set_pulse_width_range(550,2550)
    kit1.servo[1].set_pulse_width_range(450,2450)
    kit1.servo[2].set_pulse_width_range(560,2560)
    kit1.servo[3].set_pulse_width_range(400,2400)
    #===========================================
    kit1.servo[4].set_pulse_width_range(800,2800)
    kit1.servo[5].set_pulse_width_range(600,2600)
    kit1.servo[6].set_pulse_width_range(550,2550)
    kit1.servo[7].set_pulse_width_range(440,2440)
    #===========================================
    kit1.servo[8].set_pulse_width_range(600,2600)
    kit1.servo[9].set_pulse_width_range(600,2600)
    kit1.servo[10].set_pulse_width_range(550,2550)
    kit1.servo[11].set_pulse_width_range(400,2400)
    #=================================================== B - 0x41
    
    kit2 = ServoKit(address=0x42, channels=16)
    kit2.servo[0].set_pulse_width_range(600,2600)
    kit2.servo[1].set_pulse_width_range(550,2550)
    kit2.servo[2].set_pulse_width_range(600,2600)
    kit2.servo[3].set_pulse_width_range(400,2400)
    #===========================================
    kit2.servo[4].set_pulse_width_range(600,2600)
    kit2.servo[5].set_pulse_width_range(520,2520)
    kit2.servo[6].set_pulse_width_range(400,2400)
    kit2.servo[7].set_pulse_width_range(500,2500)
    #===========================================
    kit2.servo[8].set_pulse_width_range(650,2650)
    kit2.servo[9].set_pulse_width_range(500,2500)
    kit2.servo[10].set_pulse_width_range(400,2400)
    kit2.servo[11].set_pulse_width_range(430,2430)
    #=================================================== B-0x42
    
    kit3 = ServoKit(address=0x43, channels=16)
    kit3.servo[0].set_pulse_width_range(450,2450)
    kit3.servo[1].set_pulse_width_range(500,2500)
    kit3.servo[2].set_pulse_width_range(600,2600)
    kit3.servo[3].set_pulse_width_range(500,2500)
    #===========================================
    kit3.servo[4].set_pulse_width_range(450,2450)
    kit3.servo[5].set_pulse_width_range(440,2440)
    kit3.servo[6].set_pulse_width_range(500,2500)
    kit3.servo[7].set_pulse_width_range(400,2400)
    #===========================================
    kit3.servo[8].set_pulse_width_range(450,2450)
    kit3.servo[9].set_pulse_width_range(450,2450)
    kit3.servo[10].set_pulse_width_range(450,2450)
    kit3.servo[11].set_pulse_width_range(500,2500)
    #=================================================== B - 0x43
    
    kit4 = ServoKit(address=0x44, channels=16)
    kit4.servo[0].set_pulse_width_range(600,2600)
    kit4.servo[1].set_pulse_width_range(530,2530)
    kit4.servo[2].set_pulse_width_range(500,2500)
    kit4.servo[3].set_pulse_width_range(400,2400)
    #===========================================
    kit4.servo[4].set_pulse_width_range(450,2450)
    kit4.servo[5].set_pulse_width_range(450,2450)
    kit4.servo[6].set_pulse_width_range(600,2600)
    kit4.servo[7].set_pulse_width_range(450,2450)
    #===========================================
    kit4.servo[8].set_pulse_width_range(500,2500)
    kit4.servo[9].set_pulse_width_range(480,2480)
    kit4.servo[10].set_pulse_width_range(450,2450)
    kit4.servo[11].set_pulse_width_range(550,2550)
    #=================================================== B - 0x44
    
    kit5 = ServoKit(address=0x45, channels=16)
    kit5.servo[0].set_pulse_width_range(520,2520)
    kit5.servo[1].set_pulse_width_range(430,2430)
    kit5.servo[2].set_pulse_width_range(450,2450)
    kit5.servo[3].set_pulse_width_range(420,2420)
    #===========================================
    kit5.servo[4].set_pulse_width_range(450,2450)
    kit5.servo[5].set_pulse_width_range(450,2450)
    kit5.servo[6].set_pulse_width_range(500,2500)
    kit5.servo[7].set_pulse_width_range(550,2550)
    #===========================================
    kit5.servo[8].set_pulse_width_range(450,2450)
    kit5.servo[9].set_pulse_width_range(480,2480)
    kit5.servo[10].set_pulse_width_range(450,2450)
    kit5.servo[11].set_pulse_width_range(520,2520)
    #=================================================== B - 0x45
    
    KIT = [kit0, kit1, kit2, kit3, kit4, kit5]
    return KIT

def clear_all(KIT):
    return
    for j in KIT:
        for i in range(12):
            j.servo[i].angle = 90
        time.sleep(0.06)                    

def servo_up0(a,kit):
    return
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 135
            elif i==1:
                kit.servo[i].angle = 45
            elif i==2:
                kit.servo[i].angle = 145
            elif i==3:
                kit.servo[i].angle = 30
            elif i==4:
                kit.servo[i].angle = 140
            elif i==5:#39
                kit.servo[i].angle = 42
            elif i==6:
                kit.servo[i].angle = 140
            elif i==7:
                kit.servo[i].angle = 35
            elif i==8:#145
                kit.servo[i].angle = 135
            elif i==9:
                kit.servo[i].angle = 35
            elif i==10:
                kit.servo[i].angle = 150
            elif i==11:
                kit.servo[i].angle = 35


                
def servo_up1(a,kit):
    return
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 140
            elif i==1:
                kit.servo[i].angle = 45
            elif i==2:
                kit.servo[i].angle = 154
            elif i==3:
                kit.servo[i].angle = 32
            elif i==4:
                kit.servo[i].angle = 144
            elif i==5:
                kit.servo[i].angle = 32
            elif i==6:
                kit.servo[i].angle = 135
            elif i==7:
                kit.servo[i].angle = 40
            elif i==8:
                kit.servo[i].angle = 150
            elif i==9:
                kit.servo[i].angle = 30
            elif i==10:
                kit.servo[i].angle = 159
            elif i==11:
                kit.servo[i].angle = 38
                
def servo_up2(a,kit):
    return
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 150
            elif i==1:
                kit.servo[i].angle = 35
            elif i==2:
                kit.servo[i].angle = 125
            elif i==3:
                kit.servo[i].angle = 20
            elif i==4:
                kit.servo[i].angle = 145
            elif i==5:
                kit.servo[i].angle = 45
            elif i==6:
                kit.servo[i].angle = 150
            elif i==7:
                kit.servo[i].angle = 50
            elif i==8:
                kit.servo[i].angle = 130
            elif i==9:
                kit.servo[i].angle = 38
            elif i==10:
                kit.servo[i].angle = 155
            elif i==11:
                kit.servo[i].angle = 30
            
    
def servo_up3(a,kit):
    return
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 125
            elif i==1:
                kit.servo[i].angle = 45
            elif i==2:
                kit.servo[i].angle = 145
            elif i==3:
                kit.servo[i].angle = 40
            elif i==4:
                kit.servo[i].angle = 143
            elif i==5:
                kit.servo[i].angle = 45
            elif i==6:
                kit.servo[i].angle = 145
            elif i==7:
                kit.servo[i].angle = 32
            elif i==8:
                kit.servo[i].angle = 135
            elif i==9:
                kit.servo[i].angle = 40
            elif i==10:
                kit.servo[i].angle = 163
            elif i==11:
                kit.servo[i].angle = 25
                
def servo_up4(a,kit):
    return   
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 90
            elif i==1:
                kit.servo[i].angle = 45
            elif i==2:
                kit.servo[i].angle = 140
            elif i==3:
                kit.servo[i].angle = 35
            elif i==4:
                kit.servo[i].angle = 125
            elif i==5:
                kit.servo[i].angle = 40
            elif i==6:
                kit.servo[i].angle = 149
            elif i==7:
                kit.servo[i].angle = 30
            elif i==8:
                kit.servo[i].angle = 135
            elif i==9:
                kit.servo[i].angle = 50
            elif i==10:
                kit.servo[i].angle = 150
            elif i==11:
                kit.servo[i].angle = 30
                
def servo_up5(a,kit):
    return
    for i in range(12):
        if a[i] == 0:
            kit.servo[i].angle = 90
        elif a[i] == 1:
            if i==0:
                kit.servo[i].angle = 125
            elif i==1:
                kit.servo[i].angle = 35
            elif i==2:
                kit.servo[i].angle = 163
            elif i==3:
                kit.servo[i].angle = 22
            elif i==4:
                kit.servo[i].angle = 149
            elif i==5:
                kit.servo[i].angle = 30
            elif i==6:
                kit.servo[i].angle = 140
            elif i==7:
                kit.servo[i].angle = 59
            elif i==8:
                kit.servo[i].angle = 130
            elif i==9:
                kit.servo[i].angle = 50
            elif i==10:
                kit.servo[i].angle = 135
            elif i==11:
                kit.servo[i].angle = 43
                
def active(a,KIT):
    return
    servo_up0(a[0:12],KIT[0])
    time.sleep(0.06)
    servo_up1(a[12:24],KIT[1])
    time.sleep(0.06)
    servo_up2(a[24:36],KIT[5])
    time.sleep(0.06)
    servo_up3(a[36:48],KIT[3])
    time.sleep(0.06)
    servo_up4(a[48:60],KIT[4])
    time.sleep(0.06)
    servo_up5(a[60:72],KIT[2])
    time.sleep(0.06)

    
