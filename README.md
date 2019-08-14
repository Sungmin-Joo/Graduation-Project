# Graduation_Project
Edu.Dot
This is the software source code for edu_dot team (the graduation project) of the Korea Polytechnic University.

The "dip" folder is located under "/home/pi/" in "Raspberry Pi".

The "Eud.dot_first_confirm" folder contains some of the code that was first reviewed.
I saved it for memory.

The "development process" folder contains the development process of the main source code.

Development Environment :
    server : 
        Window 10 + flask     
    client :
        Raspberry Pi
        
        

Libraries :
    Python built-in library 
    flask
        - Open download server
    wifi
        - Control Wi-Fi using Python
    gTTS
    speech-recognition
        - Using "Google text to speech" to implement voice recognition via a microphone in Python
    hbcvt
        - A library that converts Hangul into Braille
          ( https://github.com/hyonzin/hangul-braille-converter )
    Adafruit_PCA9685
    adafruit_servokit
        - Used for motor control

Developer :
    Joo Sung-Min :
        - Voice Recognition -> Braille Transformation
        - Deploying a Download Server
        - UI Designing for Visually Impaired
        - Overall software design	

Team Member :
    김민섭 :
        - Team leader
        - Collecting information about the visually impaired and Braille
        - The presentation of various examinations and competitions
    서형진 :
        - Design hardware
    임건영 :
        - Control motors
