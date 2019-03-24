#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import time
import sqlite3
import json
import requests

from conf import DELAY_PUSH, FIREBASE_URL
from utils import configure_log, get_abs_path	

def get_unpushed_measures():
	measures = []
	try:
		conn = sqlite3.connect(get_abs_path() + '/pi-temp.db') 
		cursor = conn.execute('select id, timestamp, datetime, room, temp from measure where pushed="0"')
		measures = cursor.fetchall()
		conn.close()
	except:
		logging.error('Error when getting unpushed measures from database')
		pass
	return measures

def push_measure(body):
	status_code = 0
	try:
		response = requests.post(FIREBASE_URL + '/measures', body)	
		status_code = response.status_code
	except:
		logging.error('Error when executing firebase request')
		pass
	return status_code

def update_pushed_measure(id):
	try:
		conn = sqlite3.connect(get_abs_path() + '/pi-temp.db') 
		conn.execute('update measure set pushed=1 where id="%s"' % id)
		conn.commit()
		conn.close()
	except: 
		logging.error('Error when updating pushed measure in database')
		pass

def create_measure_document(timestamp, datetime, room, temp):
	return json.dumps({
		'fields': {
			'timestamp': {'integerValue': timestamp},
			'datetime': {'stringValue': datetime},
			'room': {'stringValue': room},
			'temp': {'doubleValue': temp},
		}
	})
	

if __name__ == '__main__':

	configure_log(logging, 'push.log')

	while True:		
		measures = get_unpushed_measures()	
	
		for measure in measures: 
			id = measure[0]
			timestamp = measure[1]
			datetime = measure[2]
			room = measure[3]
			temp = measure[4]
			body = create_measure_document(timestamp, datetime, room, temp)
			status_code = push_measure(body)
			if status_code == 200:
				update_pushed_measure(id)

		time.sleep(DELAY_PUSH)	



	
