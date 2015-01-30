# -*- encoding: UTF-8 -*-
import os,sys
import time
class GetCpuUage():
    def __init__(self,file_dir):
        self.file_dir = file_dir
    
    def read_cpu_usage(self,ip_num):
	#commad ='''ssh root@%s  cat /proc/stat | grep 'cpu ' | awk '{print $2" "$3" "$4" "$5" "$6" "$7" "$8}''''%ip_num
	commad = "ssh root@%s cat /proc/stat |grep 'cpu '"%ip_num
        cpustr = os.popen(commad)
	for item in cpustr:
            return item.strip().split('  ')[1].split(' ')
    
    def get_cpu_usage(self):
        ip_list = self.get_ip_num()
        for item in ip_list:
            cpustr= self.read_cpu_usage(item)
	    usni1 = long(cpustr[0])+long(cpustr[1])+long(cpustr[2])+long(cpustr[4])+long(cpustr[5])+long(cpustr[6])+long(cpustr[3])  
    	    #usn1  = long(cpustr[0])+long(cpustr[1])+long(cpustr[2]) 
	    usn1 = long(cpustr[3])
            sleep = 1  
            time.sleep(sleep)  

            cpustr = self.read_cpu_usage(item)  
            if not cpustr:  
                return 0  
	    usni2 = long(cpustr[0])+long(cpustr[1])+long(cpustr[2])+long(cpustr[4])+long(cpustr[5])+long(cpustr[6])+long(cpustr[3])  
    	    #usn2  = long(cpustr[0])+long(cpustr[1])+long(cpustr[2]) 
	    usn2 = long(cpustr[3])
            #usni2=long(cpustr[1])+long(cpustr[2])+float(cpustr[3])+long(cpustr[5])+long(cpustr[6])+long(cpustr[7])+long(cpustr[4])  
	    #usn2 = long(cpustr[4])
            #usn2  = long(cpustr[1])+long(cpustr[2])+long(cpustr[3])
            ###usn2=long(cpustr[1])+long(cpustr[2])+long(cpustr[3])  
	    #cpuper = (usn2-usn1)/(usni2-usni1)  
            cpuper = round(1-float(usn2-usn1)/(usni2-usni1),4)
            print '%scpu使用率 : %s'%(item,cpuper*100)
                            
    def get_ip_num(self):
        f = open(self.file_dir,'r')
	ip_list =[]
	for item in f:
	    ip_list.append(item.strip())
       	return ip_list 
    

if __name__ == '__main__':
    file_dir = sys.argv[1]
    GetCpuUage(file_dir).get_cpu_usage()
