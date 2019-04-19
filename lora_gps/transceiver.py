# 2019-04-19
# Version 0.1
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

import sys
import os
import time
from serial_rpi import write_to_file read_from_file distance_check

chooser = sys.argv[1]
os.chdir('/home/pi/lora_gps/transceiver/')
os.system('make')
rpi = serial_rpi()
start = time.time()
run = 1
while(time.time() - start) < 55:
    if((time.time() - start) < 25) and run == 1:
        if 'module1' in chooser:
            os.system('/home/pi/sender-reciever/lora/dragino_lora_app rec')
            rpi.read_from_file()
            rpi.distance_check()
            run = 0
            print("Recieving is done!\n\r")
        else 'module2' in chooser:
            rpi.write_to_file()
            os.system('/home/pi/sender-reciever/lora/dragino_lora_app sender')
            run = 0
    elif((time.time() - start) > 27) and run == 0:
        if 'module1' in chooser:
            rpi.write_to_file()
            os.system('/home/pi/sender-reciever/lora/dragino_lora_app sender')
            run = 1
        else 'module2' in chooser:
            os.system('/home/pi/sender-reciever/lora/dragino_lora_app rec')
            rpi.read_from_file()
            rpi.distance_check()
            run = 1
    time.sleep(1)


# Fixa detta under så det blir rätt
#
os.system('sudo rm /home/pi/sender-reciever/lora/dragino_lora_app')
os.system('sudo rm /home/pi/sender-reciever/lora/rpi-transceiver-main.o')
os.system('sudo rm /home/pi/sender-reciever/lora/serial_rpi.pyc')
os.system('sudo rm /home/pi/sender-reciever/lora/recCoordinates')
os.system('sudo rm /home/pi/lora_gps/lora/dragino_lora_app')
os.system('sudo rm /home/pi/lora_gps/data_processing/coordinates')
print("\n\rRun completed time it took: " + str(time.time() - start) + "\n\r")
