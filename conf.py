#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

INTERFACE='eth0'
FIREBASE_URL='https://pi-temp.firebaseio.com/'	

# Configure the logging module to write all messages to /log/<filename> with a specific text format
def configure_log(logging, filename): 
	logging.basicConfig(filename='log/' + filename, format='%(levelname)s:%(asctime)s *** %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)
