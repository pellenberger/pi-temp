#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import logging
import time
import sqlite3

from conf import DELAY_MEASURE, SENSOR_ID, ROOM
from utils import configure_log, get_current_time, get_abs_path

def get_temp():
	path = '/sys/bus/w1/devices/' + SENSOR_ID + '/w1_slave'
	temp = ''
	try:
		temp_file = open(path, 'r')
		data = temp_file.read()
		data = data.split('\n')[1].split('=')[1]
		temp = float(data) / 1000
		temp_file.close()
	except:
		logging.error('Error when getting temperature from file')
		pass
	return temp

def save_db(temp):
	timestamp = int(time.time())
	datetime = get_current_time()
	pushed = 0	
	query = 'insert into measure values (null, %s, "%s", "%s", %s, %s)' % (timestamp, datetime, ROOM, pushed, temp)	
	try: 
		conn = sqlite3.connect(get_abs_path() + '/pi-temp.db')
		conn.execute(query)	
		conn.commit()
		conn.close()
	except:
		logging.error('Error when saving measure in database')
		pass	

if __name__ == '__main__':

	configure_log(logging, 'pi-temp-measure.log')

	while True:		
		temp = get_temp()
		
		if temp != '':
			save_db(temp)				

		time.sleep(DELAY_MEASURE)	



	
