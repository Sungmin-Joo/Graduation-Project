# Edu_dot - Graduation_Project

Braille Board for the Blind



## Getting Started

We have implemented educational kits for people who are blind using various open sources and libraries.  
To run main code without hardware, I2C-related functions of the main code shall be annotated.  


This is the software source code for edu_dot team (the graduation project) of the Korea Polytechnic University.  
The "dip" folder is located under "/home/pi/" in "Raspberry Pi".  
The "Eud.dot_first_confirm" folder contains some of the code that was first reviewed.(I thought it was a memory.)  
The "development process" folder contains the development process of the main source code.  
The "demo" folder contains videos and pictures that actually work

### Awards and Honors
* 2019 창의적 사업계획서 경진대회 - 우수상


* [Link](https://github.com/Sungmin-Joo/Graduation_Project/tree/master/Awards_and_Honors)


### Prerequisites

Development Environment :


    server :  
        Window 10 + flask     
    client :  
        Raspberry Pi  
        
        

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


## How to use

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
### Videos and Pictures

You can see it by visiting the demo folder.


## Developer :  

    주성민(Joo Sung-Min) :  
        - Voice Recognition -> Braille Transformation  
        - Deploying a Download Server  
        - UI Designing for Visually Impaired  
        - Overall software design	  
        
## Built With

* [김민섭](https://github.com/miseop25) - Team leader, collecting information about the visually impaired and Braille.  
* [서형진] - Design hardware.  
* [임건영] - Control motors.  


# Graduation_Project
## Edu.Dot

