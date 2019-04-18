# 2019-04-16
# Version 1.0.0

import blynklib
import sys
import math
import os
from lora.serial_rpi import serial_rpi
file = open('/home/pi/sender-reciever/key','r')
buffer = file.read()
key =[]
for i in range(0,len(buffer)):
    if '\n' not in buffer[i]:
        key.append(buffer[i])
key = ''.join(key)
BLYNK_AUTH = key
blynk = blynklib.Blynk(BLYNK_AUTH)
while True:
    blynk.run()
    rpi = serial_rpi()
    coordinates = rpi.filter_coordinates()
    if (coordinates[0]=='' or coordinates[1]==''):
        lat = 0
        long = 0
        blynk.virtual_write(16,2,lat,long,"M2")
        blynk.virtual_write(22, lat)
        blynk.virtual_write(23, long)
    else:
        lat = coordinates[0]
        long = coordinates[1]
        x1 = lat[0:2]
        x2 = lat[2:4]
        x3 = lat[5:7] + '.' + lat[7:9]
        lat = float(x1) + float(x2)/60 + float(x3)/3600
        y1 = long[0:3]
        y2 = long[3:5]
        y3 = long[6:8] + '.' + long[8:10]
        long = float(y1) + float(y2)/60 + float(y3)/3600
        blynk.virtual_write(16,2,lat,long,"M2")
        blynk.virtual_write(22, lat)
        blynk.virtual_write(23, long)
