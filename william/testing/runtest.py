#Currently non-operational due to first constraint
import time
import os
import subprocess

now = time.time()

#subprocess.Popen('python crontest.py', shell=True)
#Wait until 25s

while now < 58:
    #pass
    print("test")
    if now < 29:
        os.system('python crontest.py')
        #subprocess.Popen('python crontest2.py', shell=True)
    else:
        os.system('python crontest2.py')

#Wait until 50 sec
    end = time.time()
#doene
