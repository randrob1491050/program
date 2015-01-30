# -*- encoding: UTF-8 -*-
import os,sys

dict = {
         32:1,31:2,30:4,29:8,28:16,27:32,26:64,25:128,24:256,23:512,
         22:1024,21:2048,20:4096,19:8192,18:16384,17:32768,16:65536,15:131072,
         14:262144,13:524288,12:1048576,11:2097152,10:4194304,9:8388608,
         8:16777216,7:33554432,6:67108864,5:134217728,4:268435456,3:536870912,
         2:1073741824,1:2147483648,
        }
jishu = [
         1,2,4,8,16,32,64,128,256,512,
         1024,2048,4096,8192,16384,32768,65536,131072,
         262144,524288,1048576,2097152,4194304,8388608,
         16777216,33554432,67108864,134217728,268435456,536870912,
         1073741824,2147483648,
         ]
def prostart(startIP,endIP):
    stratip = ip_to_long(startIP)  #获得IP的整形值
    endip = ip_to_long(endIP)
    kob = getIPCidr(stratip,endip)
    print "ip地址cidr值：",kob


'''cidr计算'''
def getIPCidr(startip,endip):
    ipcidr = []
    if (startip&1)==1:
        ipstr = "%s/%s" % (long_to_ip(startip),32)
        ipcidr.append(ipstr)
        ipJiSuan(startip+1,endip)
        ipcidr.extend(ip_cidr)
        return ipcidr
    else:
        ipJiSuan(startip,endip)
        ipcidr.extend(ip_cidr)
        return ipcidr

ip_cidr = []
'''输入以0为初始位当前的IP值和结束值'''
def ipJiSuan(firstip,endip):

    weiYiWei = 0
    for i in jishu:
        firsttemp = firstip&i
        if firsttemp==i:
            for k,v in dict.items():
                if v==i:
                    weiYiWei = k
                    break
            break


    chazhi = endip - firstip+1 #相差的主机位

#    ipcidr = []

    if dict[weiYiWei]<=chazhi:
        '''当主机位小于差值时'''
        if dict[weiYiWei]<chazhi:
            list = wxc(firstip,weiYiWei)
            ip_cidr.append(list[0])
            ipJiSuan(list[1],endip)
        else:
            list = wxc(firstip,weiYiWei)
            ip_cidr.append(list[0])
            return ip_cidr
    else:
        '''当主机位大于差值时'''
        list = wdc(firstip,weiYiWei,chazhi)
        if list=='error':
            return ip_cidr
        else:
            ip_cidr.append(list[0])
            ipJiSuan(list[1],endip)


'''当主机位大于差值时'''
def wdc(firstip,weiYiWei,chazhi):
    if weiYiWei==32:
        return 'error'
    if dict[weiYiWei+1]>chazhi:
        return wdc(firstip,weiYiWei+1,chazhi)
    else:
        return wxc(firstip,weiYiWei+1)


'''当主机位小于差值时'''
def wxc(firstip,weiYiWei):
    ipstr = "%s/%s" % (long_to_ip(firstip),weiYiWei)
    nextip = firstip+dict[weiYiWei]
    list = [ipstr,nextip]
    return list

'''把IP转换成Long类型'''
def ip_to_long(info):
    iplist = helpSplit(info,1)
    temp = 0
    for i in iplist:
        temp = temp | int(i)
        temp = temp<<8
    return temp>>8

'''把Long类型转换成IP'''
def long_to_ip(info):
    ip_1 = (info>>24)&255
    ip_2 = (info>>16)&255
    ip_3 = (info>>8)&255
    ip_4 = info&255
    return "%s.%s.%s.%s" % (ip_1,ip_2,ip_3,ip_4)

'''listip to ip'''
def list_to_ip(ipList):
    return "%s.%s.%s.%s" % (ipList[0],ipList[1],ipList[2],ipList[3])#返回转换后的IP字符串


'''分割'''
def helpSplit(info,type):
    if not info:
        return None
    if type==1:
        iplist = info.split(u'.')
    if type==2:
        iplist = info.split(u'-')
    return iplist


'''
if __name__=="__main__":
    ip = raw_input(r'IP : ')
    ip = str.strip(ip)
    cidr_str ='whois -h whois.apnic.net %s |grep inetnum'%ip
    f =os.popen(cidr_str)
    startIP =""
    endIP =""
    for i in f:
        print i
        ip_str =i.split('\t')
        startIP =ip_str.split('-')[0].strip()
        endIP =  ip_str.split('-')[1].strip()

        prostart(startIP,endIP)
'''


