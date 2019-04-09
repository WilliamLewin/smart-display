# 2019-04-08
# Version 0.2.1
# Note: This file should be runned with python run_this.py
# after this file has been runned coordinates will be sent
# no cleaning up is needed program will do that for you.

import os
os.chdir('/home/pi/sender-python-c/c-code')
os.system('make')
os.system('python /home/pi/sender-python-c/python-code/spawnSerialRPI.py && /home/pi/sender-python-c/c-code/dragino_lora_app sender')
os.system('rm /home/pi/sender-python-c/c-code/dragino_lora_app')
os.system('rm /home/pi/sender-python-c/c-code/rpi-transceiver-main.o')
os.system('rm /home/pi/sender-python-c/python-code/coordinates')
os.system('rm /home/pi/sender-python-c/python-code/serial_rpi.pyc')
