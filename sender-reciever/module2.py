# 2019-04-15
# Version 1.0.0

import os
import time

start = time.time()
run = 1
while (time.time() - start) < 57:
    if ((time.time() - start) < 25) and run == 1:
        os.system('python /home/pi/sender-reciever/transmit-lora.py')
        run = 0
    if((time.time() - start) > 27) and run == 0:
        os.system('python /home/pi/sender-reciever/reciever-lora.py')
        run = 1
    time.sleep(1)

print("\n\rRun completed!\n\r")
print(time.time() - start)
