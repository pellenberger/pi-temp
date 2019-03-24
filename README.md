# pi-temp
## Setup the Raspberry Pi

Goal : having a Raspberry Pi configured to get temperature from a sensor, save it on a database and push it to a webservice.

### Basics

* Install Raspbian using NOOBS  
https://www.raspberrypi.org/help/noobs-setup/
* After install, when on desktop, use "Raspberry Pi Configuration" utility to change boot, auto login, localisation, etc.
* Clone this Github project (base for further actions and commands)
* Optional : configure static IP address on eth0 interface  
**Attention** : see file `/etc/network/interfaces` -> `/etc/dhcpcd.conf`  
http://www.modmypi.com/blog/tutorial-how-to-give-your-raspberry-pi-a-static-ip-address  

### Temperature sensor

Required material is : sensor DS18B20+, resistance of 4.7k ohm / 0.25W and some cables.  

* Connect the sensor to the RPi  
http://www.manuel-esteban.com/raspi-capteur-de-temperature-ds18b20/  
* Execute :  
`sudo modprobe w1-gpio`  
`sudo modprobe w1-therm`  
* If no devices in `ls /sys/bus/w1/devices` :  
http://raspberrypi.stackexchange.com/questions/26623/ds18b20-not-listed-in-sys-bus-w1-devices   
(perhaps execute the two `modprobe` commands one more time)
* Temperature can be found in file `/sys/bus/w1/devices/<sensor_id>/w1_slave`
* For further information about how GPIO is working :   
http://www.framboise314.fr/mesure-de-temperature-1-wire-ds18b20-avec-le-raspberry-pi/

### Database

* Install sqlite3 using `apt-get install sqlite3`
* Create database in project root : `sqlite3 pi-temp.db`
* In sqlite, import table *measure* : `.read measure.sql`
* Exit sqlite using `.exit`
* Useful :   
Several sqlite manipulations (dump, using with Python, etc.) : https://doc.ubuntu-fr.org/sqlite   
SQLite Documentation : http://www.sqlite.org/docs.html

### Python scripts

Supported version is 2.7.9

* The three scripts to be executed are :  
`ping.py`   
`measure.py`   
`push.py`   
* Add a cron job for each executable scripts to be executed at reboot  
https://www.raspberrypi.org/documentation/linux/usage/cron.md   
Example : `@reboot python /home/pi/pi-temp/pi-temp-ping.py &`   
**Attention** : change `PATH` in cron tab file : `PATH=/usr/bin:/bin:/sbin`   
In case of issues :   
http://askubuntu.com/questions/23009/reasons-why-crontab-does-not-work
* Customize configuration in `conf.py` (most important : **sensor id**)
