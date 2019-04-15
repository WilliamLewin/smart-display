# 2019-04-09
# Version 1.0.0
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

from serial_rpi import *
import os
os.chdir('/home/pi/sender-reciever')
os.system('make')
rpi = serial_rpi()
rpi.write_to_file()
os.system('/home/pi/sender-reciever/dragino_lora_app sender')
os.system('rm /home/pi/sender-reciever/dragino_lora_app')
os.system('rm /home/pi/sender-reciever/rpi-transceiver-main.o')
os.system('rm /home/pi/sender-reciever/coordinates')
os.system('rm /home/pi/sender-reciever/serial_rpi.pyc')
print("Transmitting is done!")
