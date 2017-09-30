#!/usr/bin/python
# DATE:   2017.02.17

__author__ = 'iBSD@siteop.me'

import os
import re
import re
import shlex
import json
import ConfigParser
import subprocess

providers = ['ixupt', 'company', 'gfwpress']

def get_setting(s):
	config = ConfigParser.ConfigParser()
	config.read('hosts.ini')
	#v1 = dict(config.items(s))
	#return v1
	v1 = config.items(s)
	#for name, value in config.items(s):
		#return '   %s = %s' % (name, value)
	#	return value
	return v1
	#for i in range(len(v1)):
	#	return i
	#	#return v1[i][i]
	#for value in v1.itervalues():
	#	return value
	#print config.get('ixupt', 'host01')

def get_port_avail(s, p):
	### return int
	#status = subprocess.call(["nc", "-zw 1", s, "19764"])
	status = subprocess.call(["nc", "-zw 1", s, p])
	if status == 0:
		return "available"
	else:
		return "unavailable"

for x in providers:
	if x == 'ixupt':
		hostname = get_setting(x)
		print hostname
		for name, value in hostname:
		#	print value
		#for h in hostname.itervalues():
			print value , get_port_avail(value, '19764')
	elif x == 'company':
		hostname = get_setting(x)
		print hostname
		for name, value in hostname:
		#for h in hostname.itervalues():
			print value , get_port_avail(value, '51515')
        elif x == 'gfwpress':
                hostname = get_setting(x)
		print hostname
		for name, value in hostname:
                #for h in hostname.itervalues():
                        print value , get_port_avail(value, '10275')

#print get_setting('ixupt')
#get_setting('ixupt')
