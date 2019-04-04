import time
import serial
from serial_rpi import *

class serial_rpi:

    def capture_gps_data(self):
        gpsBuffer = []
        serial_gps = serial.Serial('/dev/ttyS0')
        serial_gps.baudrate = 9600
        end_time = 10   #run for 10 seconds
        stop_time = None #stop time variable
        start = time.time()
        while stop_time < end_time:
            stop = time.time()
            stop_time = stop - start
        serial_read = serial_gps.inWaiting()
        gpsBuffer = serial_gps.read(serial_read)
        return gpsBuffer

    def filter_gps_data(self):
        dataBuffer = []
        i = 0
        gpsBuffer = self.capture_gps_data()
        datastr = []
        while i < len(gpsBuffer):
            if '\r' not in gpsBuffer[i]:
                datastr.append(gpsBuffer[i])
            else:
                if '$GPRMC' in ''.join(datastr):
                    #print(''.join(datastr))
                    dataBuffer.append(''.join(datastr))
                    datastr = []
                else:
                    datastr = []
            i = i + 1
        return dataBuffer

    def filter_coordinates(self):
        longtitude = 0
        latitude = 0
        dataBuffer = self.filter_gps_data()
        cleanedBuffer = []
        for i in range(0,len(dataBuffer)):
            cleanedBuffer = dataBuffer[i].split(",")
            latitude = cleanedBuffer[3:4]
            longtitude = cleanedBuffer[5:6]
        coordinates = [latitude,longtitude]
        return coordinates
