# 2019-04-19
# Version 2.0.0
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

import sys
import os
import time
from serial_rpi import *
# coding=utf-8
chooser = sys.argv[1]
os.chdir('/home/pi/lora_gps/')
os.system('make')
rpi = serial_rpi()
start = time.time()
run = 1
print("LoRa work is getting started!\n\r")
while(time.time() - start) < 55:
    if((time.time() - start) < 25) and run == 1:
        if 'module1' in chooser:
            os.system('/home/pi/lora_gps/dragino_lora_app rec')
            rpi.read_from_file()
            rpi.distance_check()
            run = 0
            print("Recieving is done!\n\r")
        elif 'module2' in chooser:
            rpi.write_to_file()
            os.system('/home/pi/lora_gps/dragino_lora_app sender')
            run = 0
            print("Transmitting is done!\n\r")
        else:
            print("Something wrong!\n\r")
    elif((time.time() - start) > 27) and run == 0:
        if 'module1' in chooser:
            rpi.write_to_file()
            os.system('/home/pi/lora_gps/dragino_lora_app sender')
            run = 1
            print("Transmitting is done!\n\r")
        elif 'module2' in chooser:
            os.system('/home/pi/lora_gps/dragino_lora_app rec')
            rpi.read_from_file()
            rpi.distance_check()
            run = 1
            print("Recieving is done!\n\r")
        else:
            print("Something wrong!\n\r")
    else:
        print("Something really wrong!\n\r")
    time.sleep(1)

os.system('sudo /home/pi/lora_gps/remover.sh')
print("\n\rRun completed time it took: " + str(time.time() - start) + "\n\r")
