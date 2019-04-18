#!/bin/bash
time=$(date)
cd /home/pi/
sudo rm wifilog.log && sudo rm myjob.log && sudo rm blynk.log
echo $time >> wifilog.log
echo $time >> myjob.log
echo $time >> blynk.log
