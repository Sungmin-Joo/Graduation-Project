# -*- coding: utf-8 -*-
from gtts import gTTS

import os
def make_voice(string):  
    tts = gTTS(text=string, lang='ko')
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")
    os.remove("temp.mp3")

def make_voice_en(string):  
    tts = gTTS(text=string, lang='en')
    tts.save("temp.mp3")
    os.system("mpg321 temp.mp3")
    os.remove("temp.mp3")
    
if __name__ == '__main__':
    
    tts = gTTS(text="설정", lang='ko')
    tts.save("./sound/설정.mp3")
    os.system("mpg321 ./sound/설정.mp3")
    '''
    texxt = ['아','야','어','여','오','요','우','유','으','이','애','에','외','와',
                    '워','의','예','위','얘','왜','웨']
    name = ['ㅏ','ㅑ','ㅓ','ㅕ','ㅗ','ㅛ','ㅜ','ㅠ','ㅡ','ㅣ','ㅐ','ㅔ','ㅚ','ㅘ',
                    'ㅝ','ㅢ','ㅖ','ㅟ','ㅒ','ㅙ','ㅞ']
    
    for i in ['남자화장실','백화점','여자화장실','은행','집']:
        tts = gTTS(text=i, lang='ko')
        tts.save("./sound/location/"+i+".mp3")
        os.system("mpg321 ./sound/location/"+i+".mp3")
    #os.remove("./sound/다음.mp3")
    '''
    
    '''
    for r in range(12):
        for j in range(6):
            if r == 0:
                tts = gTTS(text="첫 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 1:
                tts = gTTS(text="두 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 2:
                tts = gTTS(text="세 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 3:
                tts = gTTS(text="네 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 4:
                tts = gTTS(text="다섯 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 5:
                tts = gTTS(text="여섯 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 6:
                tts = gTTS(text="일곱  번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 7:
                tts = gTTS(text="여덟 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 8:
                tts = gTTS(text="아홉 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 9:
                tts = gTTS(text="열 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 10:
                tts = gTTS(text="열 한 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")
            elif r == 11:
                tts = gTTS(text="열 두 번째, 점자," + str(j+1)+", 번, 점 해제", lang='ko')
                tts.save("./sound/"+str(r+1)+str(j+1)+str(2)+".mp3")    
    
    
    for z in range(1,5):       
        for r in range(0,3):
                for c in range(0,6):
                    if(z == 1):
                        tts = gTTS(text="좌측 상단 구역," + str(r)+", 행"+str(c)+", 열 선택", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 2):
                        tts = gTTS(text="우측 상단 구역," + str(r)+", 행"+str(c)+", 열 선택", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 3):
                        tts = gTTS(text="좌측 하단 구역," + str(r)+", 행"+str(c)+", 열 선택", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 4):
                        tts = gTTS(text="우측 하단 구역," + str(r)+", 행"+str(c)+", 열 선택", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
    for z in range(5,9):       
        for r in range(0,3):
                for c in range(0,6):
                    if(z == 5):
                        tts = gTTS(text="좌측 상단 구역," + str(r)+", 행"+str(c)+", 열 해제", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 6):
                        tts = gTTS(text="우측 상단 구역," + str(r)+", 행"+str(c)+", 열 해제", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 7):
                        tts = gTTS(text="좌측 하단 구역," + str(r)+", 행"+str(c)+", 열 해제", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
                    elif(z == 8):
                        tts = gTTS(text="우측 하단 구역," + str(r)+", 행"+str(c)+", 열 해제", lang='ko')
                        tts.save("./sound/"+str(z)+str(r)+str(c)+".mp3")
                        #os.system("mpg321 ./sound/"+str(z)+str(r)+str(c)+".mp3")
    '''
else:
    print("module call")

