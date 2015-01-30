# -*- encoding: UTF-8 -*-
import urllib, urllib2
import simplejson
import traceback
import sys
import re
reload(sys)
sys.setdefaultencoding('utf8')


class get_xinlang_ip():
    def __init__(self):
        pass
    def get_ip(self,ip_addr):
        try:
            ip = str.strip(ip_addr)
            urlfp = urllib.urlopen('http://int.dpool.sina.com.cn/iplookup/iplookup.php?format=json&ip=' + ip)
            ipdata = urlfp.read()
            urlfp.close()
            allinfo = simplejson.loads(ipdata)
	    if allinfo['ret']==1:
            	ip_dict = {}
                ip_dict['ip'] = ip
                ip_dict['city'] = allinfo["country"]+allinfo["province"] + allinfo["city"]
                ip_dict['isp'] = allinfo["isp"]
		print 'ip:',ip.encode('UTF-8')
		print 'city:',(allinfo["country"]+allinfo["province"] + allinfo["city"]).encode('UTF-8')
		print 'isp:',allinfo["isp"].encode('UTF-8')
                return ip_dict
        except:
	    traceback.print_exc(5)
            return False

ip_info_xl = get_xinlang_ip()
#ip_info_xl.get_ip('211.100.100.43')

