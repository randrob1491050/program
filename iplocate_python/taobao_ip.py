# -*- encoding: UTF-8 -*-
import urllib, urllib2  
import simplejson 
import traceback
import socket
import sys  
import re   
reload(sys)
sys.setdefaultencoding('utf8')
socket.setdefaulttimeout(20)


class get_taobao_ip():
    def __init__(self): 
        pass
    def get_ip(self,ip_addr):
        try:
            ip = str.strip(ip_addr)  
            #ptn = re.compile(r'(([12][0-9][0-9]|[1-9][0-9]|[1-9])\.){3,3}([12][0-9][0-9]|[1-9][0-9]|[1-9])')  
            #rel = ptn.match(ip)      
            urlfp = urllib.urlopen('http://ip.taobao.com/service/getIpInfo.php?ip=' + ip)  
            ipdata = urlfp.read()  
            urlfp.close()   
            allinfo = simplejson.loads(ipdata) 
            for oneinfo in allinfo:  
                if "code" == oneinfo:  
                    if 0 == allinfo[oneinfo]:  
                        #print "ip地址: " + allinfo["data"]["ip"]  
                        #print "ip: " + allinfo["data"]["ip"]  
                        #print "城市所在地: " + allinfo["data"]["country"],  
                        #print "city: " + allinfo["data"]["country"],  
                        #print allinfo["data"]["region"],  
                        #print allinfo["data"]["city"] 
                        #print "isp ："+"(" + allinfo["data"]["isp"] + ")"   
                        ip_dict = {}
                        ip_dict['ip'] = allinfo["data"]["ip"]
                        ip_dict['city'] = allinfo["data"]["country"]+allinfo["data"]["region"] + allinfo["data"]["city"]
                        ip_dict['isp'] = allinfo["data"]["isp"]
			print 'ip:',allinfo["data"]["ip"].encode('UTF-8') 
			print 'city:',(allinfo["data"]["country"]+allinfo["data"]["region"] + allinfo["data"]["city"]).encode('UTF-8')
			print 'isp:',allinfo["data"]["isp"].encode('UTF-8')
                        return ip_dict
        except:
	    error_str = "taobao api time out"
	    print error_str
            return error_str

ip_info_tb = get_taobao_ip()
#ip_info_tb.get_ip('114.80.88.211')
 
