import os
import wifi

wifilist = []
cells = wifi.Cell.all('wlan0')
     
for cell in cells:
    #print(cell.encrypted)
    #print(cell.mode)
    if cell.encrypted:
        print(cell.encryption_type)
    else:
        print('no')
    cell = cell.ssid
    wifilist.append(cell)

print(wifilist)

