#!/usr/bin/python

import subprocess

#host_list = ["aac3.ixupt.com", "aac1.ixupt.com"]
host_list = open("ixupt.com", "r")

def get_mtr(s):
	"""
	p1 = subprocess.Popen(["mtr", "-ncr 1", '%s' % s], stdout=subprocess.PIPE)
	p2 = subprocess.Popen(["tail", "-1"], stdin=p1.stdout, stdout=subprocess.PIPE)
	p1.stdout.close()  # Allow p1 to receive a SIGPIPE if p2 exits.
	output = p2.communicate()[0]
	print output
	"""
	output = subprocess.check_output("mtr -nrc 1 '%s' | tail -1" % s, shell=True)
	print output.strip()

def get_nc(s):
	status = subprocess.call(["nc", "-zvw 1", s, "19764"])

for host in host_list:
	print "{{{" + host.strip() + "}}}"
	get_mtr(host.strip())
	get_nc(host.strip())

host_list.close()
