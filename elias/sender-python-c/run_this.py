import os
os.system('gcc c-code/rpi-transceiver-main.c -o foo')
os.system('python python-code/spawnSerialRPI.py | ./foo')
os.system('rm foo')
