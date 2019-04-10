# 2019-04-09
# Version 1.0.0
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

import os
os.chdir('/home/pi/sender-reciever/transmitter/c-code')
os.system('make')
os.system('python /home/pi/sender-reciever/transmitter/spawnSerialRPI.py')
os.system('/home/pi/sender-reciever/transmitter/c-code/dragino_lora_app sender')
os.system('rm /home/pi/sender-reciever/transmitter/c-code/dragino_lora_app')
os.system('rm /home/pi/sender-reciever/transmitter/c-code/rpi-transceiver-main.o')
os.system('rm /home/pi/sender-reciever/transmitter/coordinates')
os.system('rm /home/pi/sender-reciever/transmitter/serial_rpi.pyc')
