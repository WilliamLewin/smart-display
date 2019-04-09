# 2019-04-09
# Version 0.2.1
# Note: This file should be runned with python reciever-lora.py
# after this file has been runned coordinates will be recieved
# no cleaning up is needed program will do that for you.

import os
os.chdir('/home/pi/reciever-python-c/c-code')
os.system('make')
os.system('/home/pi/reciever-python-c/c-code/dragino_lora_app rec')
os.system('python /home/pi/reciever-python-c/python-code/spawnSerialRPI.py')
os.system('rm /home/pi/reciever-python-c/c-code/dragino_lora_app')
os.system('rm /home/pi/reciever-python-c/c-code/rpi-transceiver-main.o')
os.system('rm /home/pi/reciever-pytjon-c/python-code/serial_rpi.pyc')
os.system('rm /home/pi/reciever-python-c/c-code/recCoordinates')
#os.system('rm /home/pi/reciever-python-c/python-code/coordinates')
#os.system('rm /home/pi/reciever-python-c/python-code/serial_rpi.pyc')
