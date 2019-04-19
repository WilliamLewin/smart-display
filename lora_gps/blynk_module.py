import blynklib
import sys
import math
import os
from data_processing.serial_rpi import serial_rpi
module = sys.argv[1]
file = open('/home/pi/lora_gps/key','r')
buffer = file.read()
key = []
for i in range(0,len(buffer)):
    if '\n' not in buffer[i]:
        key.append(buffer[i])
key = ''.join(key)
BLYNK_AUTH = key
blynk = blynklib.Blynk(BLYNK_AUTH)
rpi = serial_rpi()
while True:
    blynk.run()
    coordinates = rpi.filter_coordinates()
    if (coordinates[0]=='' or coordinates[1]==''):
        lat = 0
        long = 0
        if module == 'module1':
            blynk.virtual_write(16,1,lat,long,"M1")
            blynk.virtual_write(20, lat)
            blynk.virtual_write(21, long)
        else module == 'module2':
            blynk.virtual_write(16,2,lat,long,"M2")
            blynk.virtual_write(22, lat)
            blynk.virtual_write(23, long)
    else:
        lat = coordinates[0]
        long = coordinates[1]
        x1 = lat[0:2]
        x2 = lat[2:9]
        lat = float(x1) + float(x2)/60
        y1 = long[0:3]
        y2 = long[3:10]
        long = float(y1) + float(y2)/60
        if module == 'module1':
            blynk.virtual_write(16,1,lat,long,"M1")
            blynk.virtual_write(20, lat)
            blynk.virtual_write(21, long)
        else module == 'module2':
            blynk.virtual_write(16,2,lat,long,"M2")
            blynk.virtual_write(22, lat)
            blynk.virtual_write(23, long)
