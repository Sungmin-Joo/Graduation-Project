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

def down_func(durl,d_ddir,d_vdir)

def Find_dir(route):
    return os.listdir(route)
file_route='/home/pi/dip/download/'

ip_route='/home/pi/dip/setting/setip.txt' 
version_info='/home/pi/dip/setting/version.txt' 

url_food='http://192.168.43.79:5000/download/food'
url_place='http://192.168.43.79:5000/download/place'
url_vehicle='http://192.168.43.79:5000/download/vehicle'
url_version='http://192.168.43.79:5000/download/version'

down_food='/home/pi/dip/dot_data/food/'
down_place='/home/pi/dip/dot_data/food/'
down_vehicle='/home/pi/dip/dot_data/food/'

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

'''
A=response.json()
A=response.json()
for key,val in A.items():
    #f=open(file_route+key,'w')
    #f.writelines(val)
    #f.close()
    print(key , val)
'''
