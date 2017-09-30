#!/bin/sh


> test_whois.txt
for i in `cat cnroute.txt`
do
	whois -h whois.cymru.com " -v $i" >> test_whois.txt
	sleep 300
done
