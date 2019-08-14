'''
import requests
import os


file_route='/home/pi/dip/download/'
def Find_dir(root):
    return os.listdir(root)

url='http://192.168.43.79:5000/download/version'
response = requests.get(url=url)
print(response.status_code)
A=response.json()
print(type(A))
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)
'''
import requests
import os
from gtts import gTTS


def set_ip(a):
    f=open('/home/pi/dip/setting/setip.txt','w')
    f.write(a)
    f.close()
    
def down_func(d_list,v_list,version_dir):
    f=open('/home/pi/dip/setting/setip.txt','r')
    ip=f.read()
    f.close()
      
    url_food='http://'+ip+'/download/food'
    url_place='http://'+ip+'/download/place'
    url_vehicle='http://'+ip+'/download/vehicle'
    url_list=[url_food,url_place,url_vehicle]
    
    url_version='http://'+ip+'/download/version'

    f=open(version_dir,'r')
    vs=f.read()
    f.close()
    
    response = requests.get(url=url_version)
    js=response.json()
    new_vs=js['version'][0]
    if(new_vs==vs):
        return 'newest'
    else:
        for i in range(3): 
            response = requests.get(url=url_list[i])
            #print(url_list[i])
            #print(d_list[i])
            #print(response)
            js=response.json()
            for key,val in js.items():
                f=open(d_list[i]+key,'w')
                f.writelines(val)
                f.close()
                user_v_list = os.listdir(v_list[i])
                if key.replace('txt','mp3') in user_v_list:
                   print('already exist mp3')
                else:
                    temp = key.replace('.txt','')
                    tts = gTTS(text=temp, lang='ko')
                    tts.save(v_list[i]+temp+".mp3")
                    #os.system("mpg321 " +v_list[i]+temp+".mp3")
        f=open('/home/pi/dip/setting/version.txt','w')
        f.write(new_vs)
        f.close()
        return 'complete'


if __name__ == '__main__':
    #set_ip('192.168.43.79:30000')
    #set_ip('114.204.75.31:30000')
    version_dir='/home/pi/dip/setting/version.txt' 

    d_food='/home/pi/dip/dot_data/food/'
    d_place='/home/pi/dip/dot_data/location/'
    d_vehicle='/home/pi/dip/dot_data/traffic/'
    d_list = [d_food, d_place, d_vehicle]
    
    v_food='/home/pi/dip/sound/food/'
    v_place='/home/pi/dip/sound/location/'
    v_vehicle='/home/pi/dip/sound/traffic/'
    v_list = [v_food, v_place, v_vehicle]
    
    print(down_func(d_list,v_list,version_dir))



'''
response = requests.get(url=url_food)
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)
response = requests.get(url=url_place)
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)


response = requests.get(url=url_vehicle)
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)


response = requests.get(url=url_version)
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)


A=response.json()
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)
'''
