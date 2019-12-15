#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import subprocess
import time
import json
import requests
import sys

from conf import INTERFACE, FIREBASE_URL, DELAY_PING, DELAY_MEASURE, DELAY_PUSH, ROOM
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

def create_ping_document():
	return json.dumps(
		{'fields': {
			'ip': {'stringValue': get_ip_address()},
			'datetime': {'stringValue': get_current_time()},
			'timestamp': {'integerValue': int(time.time())},
			'room': {'stringValue': ROOM},
			'delayPing': {'integerValue': DELAY_PING},
			'delayMeasure': {'integerValue': DELAY_MEASURE},
			'delayPush': {'integerValue': DELAY_PUSH},
			}
		})

if __name__ == '__main__':

	configure_log(logging, 'ping.log')

	while True:		
		ping = create_ping_document()

		try:
			requests.post(FIREBASE_URL + '/pings', ping)					
		except:
			logging.error('Error when executing firebase request')
			pass

		time.sleep(DELAY_PING)	



	
