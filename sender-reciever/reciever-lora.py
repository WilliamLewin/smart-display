# 2019-04-09
# Version 1.0.0
# Note: This file should be runned with python reciever-lora.py
# after this file has been runned coordinates will be recieved
# no cleaning up is needed program will do that for you.

from serial_rpi import *
import os
os.chdir('/home/pi/sender-reciever')
os.system('make')
os.system('/home/pi/sender-reciever/dragino_lora_app rec')
rpi = serial_rpi()
rpi.read_from_file()
rpi.distance_check()
os.system('rm /home/pi/sender-reciever/dragino_lora_app')
os.system('rm /home/pi/sender-reciever/rpi-transceiver-main.o')
os.system('rm /home/pi/sender-reciever/serial_rpi.pyc')
os.system('rm /home/pi/sender-reciever/recCoordinates')
