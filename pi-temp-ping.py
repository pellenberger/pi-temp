#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import subprocess
import time
import json
import requests

from conf import INTERFACE, FIREBASE_URL, configure_log

def get_ip_address(): 
	ifconfig = subprocess.Popen(['ifconfig', INTERFACE], stdout=subprocess.PIPE)
	output = subprocess.check_output(('grep', 'inet a'), stdin=ifconfig.stdout)
	return output.split()[1].split(':')[1]

def get_current_time():
	return time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())) 

if __name__ == '__main__':
	configure_log(logging, 'pi-temp-ping.log')
	last_ping = json.dumps({'ip':get_ip_address(), 'time':get_current_time(), 'delay':'fake'})
	response = requests.put(FIREBASE_URL + 'last-ping.json', last_ping)
	print response	



	
