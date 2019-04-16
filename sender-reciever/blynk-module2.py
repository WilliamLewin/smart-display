# 2019-04-16
# Version 1.0.0

import blynklib
import sys
import math
from serial_rpi import serial_rpi

BLYNK_AUTH = sys.argv[1]
blynk = blynklib.Blynk(BLYNK_AUTH)

while True:
    blynk.run()
    rpi = serial_rpi()
    coordinates = rpi.filter_coordinates()
    if '' in coordinates[0] or coordinates[1]:
        lat = 0
        long = 0
        blynk.virtual_write(16,2,lat,long,"M2")
        blynk.virtual_write(22, lat)
        blynk.virtual_write(23, long)
    else:
        lat = float(coordinates[0])/100
        long = float(coordinates[1])/100
        blynk.virtual_write(16,2,lat,long,"M2")
        blynk.virtual_write(22, lat)
        blynk.virtual_write(23, long)
