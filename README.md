# Smart Workplace

## This file contains instructions for both the modules.

Setup is needed following [LoRa/GPS hat wiki.](http://wiki.dragino.com/index.php?title=Lora/GPS_HAT)

On Raspberry pi SPI needs to be activated.

### For GPS and LoRa connection between two modules:
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
#@reboot python /home/pi/sender-reciever/startup-clean.py >> /home/pi/clean.log 2>&1
@reboot java -jar /home/pi/server-0.41.5-java8.jar -dataFolder /home/pi/Blynk &
*/1 * * * * python /home/pi/sender-reciever/lora/XXXX.py >> /home/pi/myjob.log 2>&1
*/1 * * * * sudo python /home/pi/sender-reciever/wifi/wifi_check.py >> /home/pi/wifilog.log 2>&1
*/1 * * * * /home/pi/sender-reciever/check-pid-XXXX.sh >> /home/pi/blynk.log 2>&1
```
Where XXXX.py is either module1.py or module2.py.
Where check-pid-XXXX.sh is either check-pid-module1.sh or check-pid-module2.sh.
The first line can be included but in current version it has been a problem with it creating a Read-Only file. So in this version this line is not included in cron jobs.

### For Easy SSH connection:
1. Run the command from below:
```sh
sudo raspi-config
```
2. Navigate to ```sh Advanced Options ``` using the arrow keys.
3. Then navigate to ```sh Hostname ```
4. In the new window, change the default input to desired name. Example is seen below.
```sh
smartworkplace-moduleX
```
Where X is the number of the module.

### Blynk Configuration:
1. Make an account on Blynk.com
2. Install Python library https://github.com/blynkkk/lib-python
3. Make an local server https://github.com/blynkkk/blynk-server and follow instructions for Raspberry-Pi. When sucessfully installed or runned the local server, exit the running program.
5. Use ```sh cd /home/pi/sender-reciever/ ```
6. Make a file called "key" either using ```sh nano key ``` and add the auth-key that was provided upon registration.
or use ```sh echo "XXXXXXXXXXXXXXXXXXX" >> key ```
6. In the app set out the widget that is needed with the correct virtual pins.
7. Run the following command when done ```sh sudo reboot ```
