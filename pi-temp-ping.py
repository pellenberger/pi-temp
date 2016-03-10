#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import subprocess
import time
import json
import requests
import sys

from conf import INTERFACE, FIREBASE_URL, DELAY_PING, configure_log

def get_ip_address(): 
	ip = ''
	try: 
		ifconfig = subprocess.Popen(['ifconfig', INTERFACE], stdout=subprocess.PIPE)
		output = subprocess.check_output(('grep', 'inet a'), stdin=ifconfig.stdout)
		ip = output.split()[1].split(':')[1]
	except:
		logging.error('Error when parsing ip address')
		pass		
	return ip

def get_current_time():
	return time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())) 

if __name__ == '__main__':

	configure_log(logging, 'pi-temp-ping.log')

	while True:		
		last_ping = json.dumps({'ip':get_ip_address(), 'datetime':get_current_time(), 'delay':DELAY_PING})

		try:
			requests.put(FIREBASE_URL + 'lastPing.json', last_ping)		
		except:
			logging.error('Error when executing firebase request')
			pass

		time.sleep(DELAY_PING)	



	
