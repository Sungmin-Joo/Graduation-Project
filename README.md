# Edu_Dot - Graduation_Project  
Edu.Dot//201903~  

## o About Edu.Dot - Braille Board for the Blind  
![앞](https://user-images.githubusercontent.com/46941349/66121952-697ecf80-e619-11e9-8e81-43db89196b4a.JPG)  
![뒤JPG](https://user-images.githubusercontent.com/46941349/66121965-73083780-e619-11e9-938d-66d0bbe28431.JPG)  


## o Getting Started

We have implemented educational kits for people who are blind using various open sources and libraries.  
To run main code without hardware, I2C-related functions of the main code shall be annotated.  


This is the software source code for edu_dot team (the graduation project) of the Korea Polytechnic University.  
The "dip" folder is located under "/home/pi/" in "Raspberry Pi".  
The "Eud.dot_first_confirm" folder contains some of the code that was first reviewed.(I thought it was a memory.)  
The "development process" folder contains the development process of the main source code.  
The "demo" folder contains videos and pictures that actually work

## o Awards and Honors
* 2019 창의적 사업계획서 경진대회       - 우수상  
* 2019 산학협동 산업기술대전      - 산업장관상  
* 2019 임베디드 경진대회        - 우수상  
* 2019 산학협동 성과발표회      - 산업장관상  

* [Link](https://github.com/Sungmin-Joo/Graduation_Project/tree/master/Awards_and_Honors)


## o Prerequisites

Development Environment :


    server :  
        Window 10 + flask in Python     
    client :  
        Raspberry Pi with Python  
        
        

Libraries :


    * Python built-in library   
    * flask  
        - Open download server  
    * wifi  
        - Control Wi-Fi using Python  
    * gTTS  
    * speech-recognition  
        - Using "Google text to speech" to implement voice recognition via a microphone in Python  
    * hbcvt  
        - A library that converts Hangul into Braille  
          ( https://github.com/hyonzin/hangul-braille-converter )  
    * Adafruit_PCA9685  
    * adafruit_servokit  
        - Used for motor control  


## o How to use

Braille learning can be done by manipulating the UI for the blind.  
Once pressed, a voice message is heard for that button, and another long push is used to perform the function of that button.


### example algorithm

The following code implements touch (jesture) for the blind.

```
    def exmaple(event):
        global long_click_flag
        long_click_flag = time.time()
        voice_timmer("exmaple","exmaple",3)

    def exmaple_double():
        global long_click_flag
        if(time.time() - long_click_flag < 2):
            return
        long_click_flag = time.time()
        
    ------------------    skip    ------------------    
    
    button1 = tkinter.Button(frame1, text="exmaple",
                             command = exmaple_double,
                             repeatdelay=100,
                             repeatinterval=100)
    button1.bind("<Button-1>", exmaple)
         
```  
  
  
## o Videos and Pictures

You can see it by visiting the [demo](https://github.com/Sungmin-Joo/Graduation-Project/tree/master/demo) folder.


## o S/W development process:  
 * 06/05/2019 : Complete GUI design and gesture  
 * 07/17/2019 : Complete first planned Edu.Dot
 * 08/21/2019 : Complete recognize korean and convert braille, quize  
 
 
 
## o Developer :  

    주성민(Joo Sung-Min) :  
        - Voice Recognition -> Braille Transformation  
        - Deploying a Download Server  
        - UI Designing for Visually Impaired  
        - Overall software design  
    E-mail : 
        big-joo_dev@naver.com   
    Phone   :  
        010-2770-4367  
    Univesity :  
        Korea Polytechnic University  
  
        
## o Built With

* [김민섭](https://github.com/miseop25) - Team leader, collecting information about the visually impaired and Braille.  
* [서형진] - Design hardware.  
* [임건영] - Control motors.  


