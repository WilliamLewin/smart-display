# 2019-04-15
# Version 1.0.0

import os
from datetime import date
today = str(date.today())
echo = "echo " + today + " >> myjob.log"
os.chdir('/home/pi')
os.system('rm myjob.log')
os.system(echo)
