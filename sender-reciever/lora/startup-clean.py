# 2019-04-16
# Version 1.0.1

import os
from datetime import date
today = str(date.today())
echo = "echo " + today + " >> myjob.log"
os.chdir('/home/pi')
os.system('rm myjob.log')
os.system(echo)
