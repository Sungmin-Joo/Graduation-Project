import speech_recognition as sr

import hbcvt

import os

from gtts import gTTS

 

#mp3_route = mpg321 homepidipsound

r = sr.Recognizer()

#os.system(mp3_route+�����Է���.mp3)

with sr.Microphone() as source

    print(say something)

    audio = r.listen(source)

    print(Time OVER)

 

#os.system(mp3_route+�����Է���.mp3)

 

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

    #os.system(mp3_route+�����Է�����.mp3)

    print(cnt)

 

else

    print(text + string)

    print(cnt)

    tts = gTTS(text=�Էµ� �ܾ�� + string +  �Դϴ�., lang='ko')

    tts.save(.sound��������ӽ�.mp3)

    os.system(mpg321 .sound��������ӽ�.mp3)

    print(dot_data)