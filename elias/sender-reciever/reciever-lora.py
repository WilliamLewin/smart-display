# 2019-04-09
# Version 1.0.0
# Note: This file should be runned with python reciever-lora.py
# after this file has been runned coordinates will be recieved
# no cleaning up is needed program will do that for you.

import os
import time
os.chdir('/home/pi/sender-reciever/reciever/c-code')
os.system('make')
os.system('/home/pi/sender-reciever/reciever/c-code/dragino_lora_app rec')
os.system('python /home/pi/sender-reciever/reciever/spawnSerialRPI.py')
os.system('rm /home/pi/sender-reciever/reciever/c-code/dragino_lora_app')
os.system('rm /home/pi/sender-reciever/reciever/c-code/rpi-transceiver-main.o')
os.system('rm /home/pi/sender-reciever/reciever/serial_rpi.pyc')
os.system('rm /home/pi/sender-reciever/reciever/c-code/recCoordinates')
