# 2019-04-04
# Version: 0.1.1

from serial_rpi import *
rpi = serial_rpi()
x = rpi.filter_coordinates()
print(x[0])
print(x[1])
