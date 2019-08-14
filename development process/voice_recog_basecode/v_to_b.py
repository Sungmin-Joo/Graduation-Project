import speech_recognition as sr

import hbcvt

import os

from gtts import gTTS

 

#mp3_route = mpg321 homepidipsound

r = sr.Recognizer()

#os.system(mp3_route+음성입력전.mp3)

with sr.Microphone() as source

    print(say something)

    audio = r.listen(source)

    print(Time OVER)

 

#os.system(mp3_route+음성입력후.mp3)

 

string = r.recognize_google(audio,language='ko_KO')

data = hbcvt.h2b.text(string.replace( ,))

cnt=0

dot_data=[]

for i in data

    for j in i

        for z in j

            for x in z

                for a in x

                    if(type(a)==list)

                        cnt+=a.count(1) + a.count(0)

                        for b in a

                            dot_data.append(b)

 

print(string)                    

if(cnt72)

    #os.system(mp3_route+음성입력제한.mp3)

    print(cnt)

 

else

    print(text + string)

    print(cnt)

    tts = gTTS(text=입력된 단어는 + string +  입니다., lang='ko')

    tts.save(.sound음성결과임시.mp3)

    os.system(mpg321 .sound음성결과임시.mp3)

    print(dot_data)