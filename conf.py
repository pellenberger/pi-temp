#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys, os

INTERFACE='eth0'
FIREBASE_URL='https://pi-temp.firebaseio.com/'	

# All delays are in seconds
DELAY_PING=5

# Configure the logging module to write all messages to /log/<filename> with a specific text format
def configure_log(logging, filename): 
	logging.basicConfig(filename=get_abs_path() + '/log/' + filename, format='%(levelname)s:%(asctime)s *** %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)

def get_abs_path(): 
	pathname = os.path.dirname(sys.argv[0])
	return os.path.abspath(pathname)
	
