#!python3

__author__ = 'iBSD@siteop.me'

'''
ABOUT CHECK PROCESS with commands and system modules
from os import system
from commands import getoutput

def check_agent():
    VALUE = getoutput("ps aux | grep falcon-agen | grep -v grep")
    if VALUE != '':
        print "falcon-agent already is exits"
    else:
        system("/usr/local/app/agent/control start &")

check_agent()
'''

'''
ABOUT TIME FORMAT OUTPUT
'''
#import time
#t = str(int(time.time() * 1000))
#print(t)

'''
ABOUT COMMAND OUTPUT
'''
#import subprocess
#subproccess.call(['tesseract', infile, outfile])

''' 
ABOUT JSON LIBRARY 
'''
#import json
#json_key = json.load(open('.json'))
#print(json_key['client_email'])
#print(json_key['private_key'].encode())

''' 
ABOUT STRING ENCODE 
'''
#print(r.content.decode('utf-8'))
#print(r.text.encode('ISO-8859-1').decode(requests.utils.get_encodings_from_content(r.text)[0]))

''' 
ABOUT REQUEST LIBRARY 
'''
#post_data = {'message': '111111', 'addsubmit': 'true'}
#r = s.post(url2, post_data)
#r = requests.get(URL, auth=(USERNAME, '123456'))
#r = requests.get(URL)
#print(r.status_code, r.encoding, r.headers, r.text.encode("GBK",'ignore'))

''' 
ABOUT FILE OPERATION 
'''
#import glob, os
#for infile in glob.glob("*.jpg"):
#    file, ext = os.path.splitext(infile)

''' 
ABOUT TUPLE LIST DICTIONARY 
'''
#s = "-"
#seq = ("a", "b", "c")
#a = 'aaa'
#b = 'bbb'
#c = 'ccc'
#seq = [(a, b, c)] 
#seq1 = (a, b, c)
#seq2 = [a, b, c]
#print(type(seq))
#print(type(seq1))
#print(type(seq2))
#print("-".join([a, b, c]))

