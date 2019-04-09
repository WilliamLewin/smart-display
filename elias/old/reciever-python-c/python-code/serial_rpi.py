# 2019-04-08
# Version: 0.2.1

import time
import serial

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
        end_time = 10                               #run for 10 seconds
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
        file = open("/home/pi/sender-python-c/python-code/coordinates","w")
        file.write(str(coordinates[0]))
        file.write('\n\r')
        file.write(str(coordinates[1]))
        file.close()


    def read_from_file(self):
        file = open('/home/pi/reciever-python-c/c-code/recCoordinates','r')
        coordinates = file.read()
        buffer = []
        for i in range(0,len(coordinates)):
            if coordinates[i] != '\n':
                buffer.append(coordinates[i])
        cleanedBuffer = ''.join(buffer)
        latitude = cleanedBuffer[0:9]
        longtitude = cleanedBuffer[9:18]
        print(latitude)
        print(longtitude)
