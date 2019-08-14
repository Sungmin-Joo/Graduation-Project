# -*- coding: utf-8 -*-
f=open("/home/pi/dip/dot_data/manual/사과.txt",'w')
f.write(str(30)+'\n')
for i in [1,1,1,0,0]:
    f.write(str(i))


f.close()
