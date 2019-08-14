# -*- coding: utf-8 -*-
from wireless import Wireless
import wifi
import os
import time

string = '''
    trl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
    update_config=1
    country=US
    '''
os.system("%s > /etc/wpa_supplicant/wpa_supplicant.conf" % string)

print(string)
'''


wireless = Wireless()
print(wireless.connect(ssid='useed', password='useed25255'))


print(wireless.current())
print(wireless.driver())
print(wireless.interfaces())

#print(wireless.interface())
#print(wireless.current())

os.system("dtoverlay=pi3-enable-wifi")
time.sleep(1)
wifilist = []
cells = wifi.Cell.all('wlan0')
for cell in cells:
    cell = str(cell)
    temp = cell.split('=')
    st = temp[1]
    wifilist.append(st[0:-1])
print(wifilist)


interface = 'wlan0'
name = 'useed'
password = 'useed2555'
os.system('iwconfig '+interface + ' essid ' +name + ' key ' + password)
'''
