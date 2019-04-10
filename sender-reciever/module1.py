import os
x = 1
y = 1
while y == 1:
    if x == 1:
        os.system('python /home/pi/sender-reciever/reciever-lora.py')
        x = 0
    if x == 0:
        os.system('python /home/pi/sender-reciever/transmit-lora.py')
        y = 0
