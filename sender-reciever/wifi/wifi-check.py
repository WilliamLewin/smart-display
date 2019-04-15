# 2019-04-15
# Version 1.0.0

import os
import time

def getCurrentWifi():
    os.system('sudo iwconfig | grep wlan0 >> /home/pi/sender-reciever/wifi/currentwifi.txt')
    file = open('/home/pi/sender-reciever/wifi/currentwifi.txt', 'r')
    wifi = file.read()
    buffer = []
    for i in range(0,len(wifi)):
        if wifi[i] != '\n':
            buffer.append(wifi[i])
    cleanedBuffer = ''.join(buffer)
    cleanedBuffer = cleanedBuffer.replace(" ", "")
    trimmedWifi = cleanedBuffer[15:30]
    return trimmedWifi

def wifiScan():
    os.system("sudo iwlist wlan0 scan | grep ESSID | awk '{print substr($0, index($0,$1)) }' >> /home/pi/sender-reciever/wifi/wifi.txt")
    file = open('/home/pi/sender-reciever/wifi/wifi.txt','r')
    wifi = file.read()
    buffer = []
    for i in range(0,len(wifi)):
        if wifi[i] != '\n':
            buffer.append(wifi[i])
    buffer = ''.join(buffer)
    return buffer


trimmedWifi = getCurrentWifi()
buffer = wifiScan()
if 'CCGuest' in trimmedWifi:
    if 'SmartWorkplaceIphone' in buffer:
        print("Connecting")
        os.system('sudo /home/pi/sender-reciever/wifi/wifi-smartworkplace.sh')
    else:
        print("Not Available")
if 'SmartWorkplaceIphone' in trimmedWifi:
    print("Already Connected")
if 'off/any' in trimmedWifi:
    if 'SmartWorkplaceIphone' in buffer:
        print("Connecting")
        os.system('sudo /home/pi/sender-reciever/wifi/wifi-smartworkplace.sh')
    else:
        os.system('sudo /home/pi/sender-reciever/wifi/wifi-ccguest.sh')

os.system('rm /home/pi/sender-reciever/wifi/wifi.txt')
os.system('rm /home/pi/sender-reciever/wifi/currentwifi.txt')
