import time

start = time.time()
run = 1
while (time.time() - start) < 58:
    if ((time.time() - start) < 25) and run == 1:
        #time.sleep(22)
        run = 0
    if((time.time() - start) > 27) and run == 0:
        #time.sleep(10)
        run = 1
    time.sleep(1)
