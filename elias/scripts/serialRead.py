import serial
import time
import sys
import os
import re

print('\r\n')
print("Function for setting up and reading serial GPS data")
serial_gps = serial.Serial('/dev/ttyS0')
serial_gps.baudrate = 9600

end_time = 10
start_time = time.time()
stop = 0
while stop < end_time :
    stop_time = time.time()
    stop = stop_time - start_time

serial_read = serial_gps.inWaiting()
gpsdata = serial_gps.read(serial_read)
print("Done")
#fullstr = ''.join(gpsdata)

####################
# Function for filtering out GPS data
####################
print('\r\n')
print("Function for filtering out GPS data")
i = 0
datastr = []
dataBuffer = []
while i < len(gpsdata):
    if '\n' not in gpsdata[i]:
        datastr.append(gpsdata[i])
    else:
        if '$GPRMC' in ''.join(datastr):
            #print(''.join(datastr))
            dataBuffer.append(''.join(datastr))
            datastr = []
        else:
            datastr = []
    i = i + 1
print(dataBuffer)
print("\nDone")


################################################
# Function for filtering Longtitude and Latitude
################################################
print('\r\n')
print("Function for filtering longtitude and latitude")
print('\r\n')
latitude = 0
longtitude = 0
cleanedBuffer = []
for i in range(0,len(dataBuffer)):
    cleanedBuffer = dataBuffer[i].split(",")
    latitude = cleanedBuffer[3:4]
    longtitude = cleanedBuffer[5:6]

print(cleanedBuffer)
print(latitude)
print(longtitude)
print("\nDone")
