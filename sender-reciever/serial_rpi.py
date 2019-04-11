# 2019-04-09
# Version: 1.0.0

import time
import serial
import geopy.distance
import math

class serial_rpi:

    ###################################
    # This function captures GPS data
    # using serial port /dev/ttyS0
    # which the LoRa/GPS hat has gps
    # module connected on.
    #
    # Return: GPS data
    ###################################

    def capture_gps_data(self):
        gpsBuffer = []
        serial_gps = serial.Serial('/dev/ttyS0')
        serial_gps.baudrate = 9600
        end_time = 8                               #run for 10 seconds
        stop_time = None                            #stop time variable
        start = time.time()
        while stop_time < end_time:
            stop = time.time()
            stop_time = stop - start
        serial_read = serial_gps.inWaiting()
        gpsBuffer = serial_gps.read(serial_read)
        return gpsBuffer

    ###################################
    # This function filters out
    # gps data that is being transmit-
    # ted.
    #
    # Return: Filtered GPS data
    ###################################

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
                    dataBuffer.append(''.join(datastr))
                    datastr = []
                else:
                    datastr = []
            i = i + 1
        return dataBuffer

    ###################################
    # This function gives latitude
    # and longtitude
    #
    # Return: Latitude and longtitude
    ###################################
    def filter_coordinates(self):
        longtitude = 0
        latitude = 0
        dataBuffer = self.filter_gps_data()
        cleanedBuffer = []
        for i in range(0,len(dataBuffer)):
            cleanedBuffer = dataBuffer[i].split(",")
            latitude = cleanedBuffer[3]
            longtitude = cleanedBuffer[5]
        coordinates = [latitude,longtitude]
        return coordinates

    ###################################
    # This function writes latitude
    # and longtitude to a file called
    # coordinates
    # Return: None
    ###################################

    def write_to_file(self):
        coordinates = self.filter_coordinates()
        file = open("/home/pi/sender-reciever/coordinates","w")
        file.write(str(coordinates[0]))
        file.write('\n\r')
        file.write(str(coordinates[1]))
        file.close()


    def read_from_file(self):
        file = open('/home/pi/sender-reciever/recCoordinates','r')
        coordinates = file.read()
        buffer = []
        for i in range(0,len(coordinates)):
            if coordinates[i] != '\n':
                buffer.append(coordinates[i])
        cleanedBuffer = ''.join(buffer)
        latitude = cleanedBuffer[0:9]
        longtitude = cleanedBuffer[9:20]
        latLong = [latitude,longtitude]
        return latLong

    def calculate_dist_gps(self):
        latLong = self.filter_coordinates()
        latitude1 = float(latLong[0])/100
        longtitude1 = float(latLong[1])/100
        latLong = self.read_from_file()
        latitude2 = float(latLong[0])/100
        longtitude2 = float(latLong[1])/100
        cord1 = (latitude1,longtitude1)
        cord2 = (latitude2,longtitude2)
        distance = geopy.distance.vincenty(cord1, cord2).m
        return distance

    ###################################
    # This function returns an error
    # message based on the distance
    #
    # Return: None
    ###################################
    def distance_check(self):
        distance_to_sender = self.calculate_dist_gps()
        print(distance_to_sender)
        if distance_to_sender < 5:
            print("TURN AROUND")
            print("Distance is to low")
            print(distance_to_sender)
