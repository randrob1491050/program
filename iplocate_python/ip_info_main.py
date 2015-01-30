# -*- encoding: UTF-8 -*-
import traceback
import os,sys
from taobao_ip import ip_info_tb
from xinlang_ip import ip_info_xl
from iplocate import IPInfo
from ip_cidr import prostart
os.chdir(sys.path[0])
ip_str ='''
10.99.27.74
'''
if __name__=="__main__":
    try:
#        ip_addr = sys.argv[1]
        #ip_addr = "8.8.8.8"
        ip_info = ip_str.strip().split('\n')
        for ip_addr in ip_info:
            ip_addr = str(ip_addr)
            print '----------------taobao data-------------------------'
            tb_result =ip_info_tb.get_ip(ip_addr)
    	    print '----------------sina  data--------------------------'
            tb_result =ip_info_xl.get_ip(ip_addr)
    	    print '-----------------iplocate  data---------------------'
            IPInfo().getIPAddr(ip_addr)
            cidr_str ='whois -h whois.apnic.net %s |grep inetnum'%ip_addr
            f =os.popen(cidr_str)
            startIP =""
            endIP =""
            for i in f:
                ip_str =i.strip().replace('\t',' ')
                iplist = ip_str.strip().split(' ')
    	        ip_list = filter(lambda x: x.strip(), iplist)
                startIP = ip_list[1]
                endIP =  ip_list[3]
                prostart(startIP,endIP)
    except:
            traceback.print_exc(5)
            print '请正确输入您的Ip地址'




