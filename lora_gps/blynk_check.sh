#!/bin/sh
if ps -ef | grep -v grep | grep blynk_module.py ; then
  exit 0
else
  python /home/pi/lora_gps/blynk_module.py &
  exit 0
fi
