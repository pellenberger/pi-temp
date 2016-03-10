#!/usr/bin/python2.7
#-*- coding: utf-8 -*-

import sys
import os
import time

# Configure the logging module to write all messages to ./log/<filename> with a specific text format
def configure_log(logging, filename): 
	logging.basicConfig(filename=get_abs_path() + '/log/' + filename, format='%(levelname)s:%(asctime)s %(message)s', datefmt='%d-%m-%Y %H:%M:%S', level=logging.DEBUG)

# Return absolute path of the folder containing the executed script
def get_abs_path(): 
	pathname = os.path.dirname(sys.argv[0])
	return os.path.abspath(pathname)

def get_current_time():
	return time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(time.time())) 
