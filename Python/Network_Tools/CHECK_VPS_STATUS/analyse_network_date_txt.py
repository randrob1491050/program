#!/usr/bin/python
# DATE:   2017.02.17

__author__ = 'iBSD@siteop.me'

import os
import re
import subprocess

#hosts = ["aac3.ixupt.com", "aac1.ixupt.com"]
hosts = open("hosts_list", "r")

def get_ping_lost(s):
	child1 = subprocess.Popen("ping -c1 -W1 '%s'" % s, shell=True, stdout=subprocess.PIPE)
	child2 = subprocess.Popen(["grep", "time="], stdin=child1.stdout,stdout=subprocess.PIPE)
	out = child2.communicate()
	#print type(out[0].strip())
	if not out[0].strip() == '':
		collects = (out[0].strip()).split('=')
		return collects[3]
	else:
		return "packet loss"
		
def get_network_loss(s):
	output = subprocess.check_output("mtr -nrc 1 '%s' | tail -1" % s, shell=True)
	#print output.strip()
	collects = output.split()
	#print collects
	#print type(collects[2])
	return collects[2]

def get_port_avail(s):
	# return int
	status = subprocess.call(["nc", "-zw 1", s, "19764"])
	if status == 0:
		return "available"
	else:
		return "unavailable"	

for d in hosts:
	#print "{{{\t" + d.strip() + "\t}}}"
	print "HOSTNAME: %s" "\t" "LOSS: %s" "\t" "SERVICE: %s" "\t" "PING: %s"% ( d.strip(), get_network_loss(d.strip()), get_port_avail(d.strip()) , get_ping_lost(d.strip()) )

hosts.close()
