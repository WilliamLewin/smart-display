# Smart Workplace

## This file contains instructions for both the modules.

Setup is needed following [LoRa/GPS hat wiki.](http://wiki.dragino.com/index.php?title=Lora/GPS_HAT)

On Raspberry pi SPI needs to be activated.

For GPS and LoRa connection between two modules:
1. Get the latest update from Smart Workplace on GitHub.
2. Unzip folder "sender-reciever" in /home/pi.
3. Edit crontab "crontab -e".
4. Cd to "wifi" folder inside "sender-reciever" folder.
6. Use "chmod +x wifi-ccguest.sh" and "chmod +x wifi-ccguest.sh".
7. Make two files called wifi1 and wifi2 in /etc/wpa_supplicant/
8. Wifi1 should contain the hotspot connection, for example look below.
```sh
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=INSERTCOUNTRYCODE

network={
	ssid="HOTSPOTNAME"
	psk="HOTSPOTSECRET"
	key_mgmt=WPA-PSK
}
```
9. Do the same with wifi2, this should have the original WiFi connection when first installed the Raspberry.
10. Add the lines from under in "crontab -e":
```sh
@reboot python /home/pi/startup-clean.py
*/1 * * * * python /home/pi/sender-reciever/XXXX.py >> /home/pi/myjob.log 2>&1
*/1 * * * * sudo python /home/pi/sender-reciever/wifi/wifi-check.py
```
Where XXXX.py is either module1.py or module2.py.

Easy SSH connection:
1. raspi-config
2. Advanced Options
3. Hostname
4. Change to "smartworkplace-moduleX" where X is the number on the module.
