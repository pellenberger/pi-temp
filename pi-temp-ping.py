#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import subprocess
import time
import json
import requests
import sys

from conf import INTERFACE, FIREBASE_URL, DELAY_PING, DELAY_MEASURE, DELAY_PUSH
from utils import configure_log, get_current_time

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

if __name__ == '__main__':

	configure_log(logging, 'pi-temp-ping.log')

	while True:		
		last_ping = json.dumps({'ip':get_ip_address(), 'datetime':get_current_time(), 'delayPing':DELAY_PING, 'delayMeasure':DELAY_MEASURE, 'delayPush':DELAY_PUSH})

		try:
			requests.put(FIREBASE_URL + 'lastPing.json', last_ping)					
		except:
			logging.error('Error when executing firebase request')
			pass

		time.sleep(DELAY_PING)	



	
