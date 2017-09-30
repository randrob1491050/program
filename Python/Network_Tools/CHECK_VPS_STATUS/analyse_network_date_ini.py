#!/usr/bin/python
# DATE:   2017.02.17

__author__ = 'iBSD@siteop.me'

import os
import re
import ConfigParser
import subprocess

providers = ['ixupt', 'company', 'gfwpress']

def get_setting(s):
	config = ConfigParser.ConfigParser()
	config.read('hosts.ini')
	v1 = dict(config.items(s))
	return v1

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
		#print hostname
		for h in hostname.itervalues():
			print h , get_port_avail(h, '19764')
	elif x == 'company':
		hostname = get_setting(x)
		#print hostname
		for h in hostname.itervalues():
			print h , get_port_avail(h, '51515')
        elif x == 'gfwpress':
                hostname = get_setting(x)
                #print hostname
                for h in hostname.itervalues():
                        print h , get_port_avail(h, '10275')


#print get_setting('ixupt')
