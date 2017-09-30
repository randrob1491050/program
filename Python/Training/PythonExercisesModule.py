#!python3

'''
### Python3 library os
import os
import socket
print(os.uname()[1])
print(socket.gethostname())
print(os.getenv('PATH'))
print(os.getcwd())
print(os.getgid())
print(os.getuid())
print(os.getpid())
# How retrieve info under one dir
with os.scandir('/tmp') as it:
    for entry in it:
        if not entry.name.startswith('.') and entry.is_dir():
            print(entry.name)
# How using os.walk and print tricks
from os.path import join, getsize
for root, dirs, files in os.walk('/tmp'):
    print(root, "consumes", end=" ")
    print(sum(getsize(join(root, name)) for name in files), end=" ")
    print("bytes in", len(files), "non-directory files")
'''
'''
### Python3 library sys , locale
# Retrieve encoding info
import sys
import locale
#print("================>>>>>>>>>>")
#print(sys.version)
#print(sys.getfilesystemencoding(), sys.stdin.encoding, sys.stdout.encoding, locale.getpreferredencoding())
### Python3 library subprocess
# Execute System command with args
import subprocess
#           call method: only care whether it succeeds or not*, but blocking
#print("================>>>>>>>>>>")
#output_call = subprocess.call(['curl', '-s', '-4', 'ip.cn/8.8.8.8'])
#print(output_call)
#output_checkcall = subprocess.check_call(['curl', '-s', '-4', 'ip.cn/8.8.8.8'])
#print(output_checkcall)
#           getoutput method: is deprecated 
#print("================>>>>>>>>>>")
#output_getoutput = subprocess.getoutput('curl -s -4 ip.cn/8.8.8.8')
#print(output_getoutput)
#           check_output method: returns the output of the command execution, but blocking
#           But for more recent versions, it is no longer the recommended approach.
#print("================>>>>>>>>>>")
#output_bytes = subprocess.check_output(['curl', '-s', '-4', 'ip.cn/8.8.8.8'])
#output_text = output_bytes.decode('utf-8')
#print(output_text.strip())
#           run method: returns the output of the command execution
#           is recommended. It provides a very general, high-level API for the subprocess module
#           The return value is a bytes object, so if you want a proper string, you'll need to decode it. 
#           Assuming the called process returns a UTF-8-encoded string
#import re
#result = subprocess.run(['curl', '-s', '-4', 'ip.cn/8.8.8.8'], stdout=subprocess.PIPE)
#out = result.stdout.decode('utf-8')
#pattern = re.compile(r'\d.\d.\d.\d')
#ip = pattern.search(out)
#print(ip.group(0))
#result = subprocess.run("curl -s -4 ip.cn/8.8.8.8 | awk -F' ' '{print $1}'", shell=True, stdout=subprocess.PIPE)
#print(result.stdout.decode('utf-8'))
#           Popen method: returns the output of the command execution, but unblocking
#           Complex applications & legacy versions of Python (2.6 and below)
#print("================>>>>>>>>>>")
#p1 = subprocess.Popen(['ping', '-c 1', '114.114.114.114'], stdout=subprocess.PIPE)
#p2 = subprocess.Popen(['grep', 'packets'], stdin=p1.stdout, stdout=subprocess.PIPE)
#output_ping = p2.communicate()[0]
#print(output_ping.decode('utf-8'))
'''
'''
### Python3 library argparse
import argparse
parser = argparse.ArgumentParser(description='Self-checking library argparse under Python3')
parser.add_argument('integers', metavar='N', type=int, nargs='+', 
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const', 
                    const=sum, default=max, 
                    help='sum the integers (default: find the max)')
args = parser.parse_args(['1', '2', '3', '4'])
print(args.accumulate(args.integers))
print(args)
'''
'''
### Python3 library re
import re
# at the beginning of string
prog = re.compile(r'\w.*')
result_1 = prog.match('abcdefghijk123456789ABCDEFGHIJ')
print("result_1 match output:", result_1)
#           at the beginning of string
result_2 = re.match(r'\d{9}', 'abcdefghijk123456789ABCDEFGHIJ')
print("result_2 match output:", result_2)
#           scan through string and return match group
result_3 = re.search(r'\d{9}', 'abcdefghijk123456789ABCDEFGHIJ')
print("result_3 search output:", result_3[0])
print("result_3 search output:", result_3.group(0))
#           scan through string and return list object
result_4 = re.findall(r'\d{9}', 'abcdefghijk123456789ABCDEFGHIJ')
print("result_4 findall output:", result_4)
# scan through string and return iterator object
result_5 = re.finditer(r'\d{9}', 'abcdefghijk123456789ABCDEFGHIJ')
#           return match from iterator object 
for match in result_5:
    print("result_5 finditer output:", tuple(match.group()))
#for index, match in enumerate(result_5):
#    print("result_5 output:",index, match)
print()
result_split_1 = re.split('\W+', 'Words, words, words.')
print("result_split_1 output:", result_split_1)
result_split_2 = re.split('(\W+)', 'Words, words, words.')
print("result_split_2 output:", result_split_2)
result_split_3 = re.split('(\W+)\1', 'Words, words, words.')
print("result_split_3 output:", result_split_3)
print()
#           re.search sames re.match but re.findall just return list obj cann't using groups() functions
result_groups = re.search(r'(\d+)\.(\d+)', '24.1632')
print("result_groups output:", result_groups.groups())
print()
text = """Ross McFluff: 834.345.1254 155 Elm Street
Ronald Heathmore: 892.345.3428 436 Finley Avenue
Frank Burger: 925.541.7625 662 South Dogwood Way
Heather Albrecht: 548.326.4584 919 Park Place"""
entries = re.split('\n+', text)
print(entries)
print([re.split(":? ", entry, 4) for entry in entries])
'''
'''
### Python3 library json
import json
data_obj = {
    "English": {
        "car": ["small", "median", "big"],
        "color": ["white", "black", "red"],
    },
}
# Serialize obj to a JSON formatted str
s_dumps = json.dumps(data_obj, sort_keys=True, indent=4, ensure_ascii=False)
print(s_dumps)
# Load data from JSON formatted obj
r_loads = json.loads(s_dumps)
print(r_loads)

# Serialize obj to a JSON formatted file
with open("output.txt", "w", encoding="UTF-8") as f_dump:
    s_dump = json.dump(data_obj, f_dump, sort_keys=True, indent=4, ensure_ascii=False)
f_dump.close()

# Load data from JSON formatted file
with open("output.txt", "r", encoding="UTF-8") as f_load:
    r_load = json.load(f_load)
f_load.close()
print(r_load)
'''
'''
### Python3 library csv
import csv
# Read content from csv file
with open('egg.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        #print(', '.join(row)) 
        print(row)
csvfile.close()
# Write content to csv file
#with open('egg.csv', 'a', newline='') as csvfile:
#    myWriter = csv.writer(csvfile)
#    myWriter.writerow(['5', 'eee', 'lets make'])
#csvfile.close()
'''
'''
### Python3 library pprint
import pprint
stuff = ['spam', 'eggs', 'lumberjack', 'knights', 'ni']
stuff.insert(0, stuff[:])
print(stuff)
pprint.pprint(stuff)
pp = pprint.PrettyPrinter(indent=4)
pp.pprint(stuff)
'''
'''
import time
import datetime
print("### About library datetime ###")
#
print("Current datetime: ", datetime.datetime.now())
print("Obtain today: ", datetime.date.today())
print("Obtain tomorrow day", datetime.date.today() + datetime.timedelta(days=1))
print("Obtain three days before",
      datetime.date.today() - datetime.timedelta(days=3))
#           String format (datetime -> string)
print(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
#           Date format (string -> datetime)
print(datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S"))
#           datetime <=> date
print(datetime.datetime.now().date())
#           about attribute 'minute' of 'datetime.time' objects
# print(datetime.time)
# print(datetime.time().minute)
# print(datetime.time.minute)
#print('mintue       :', datetime.time(1, 2, 3).minute)
#           create a new datetime object, Because Python's datetime objects are immutable
#orig_end = datetime.now() + relativedelta.relativedelta(months=1)
#mod_end = orig_end.replace(hour=23, minute=59, second=59, microsecond=0)
print()
print("### About library time ###")
#           Timestamp
print("Currently timestamp: ", time.time())
#           Time tuple format
print("Current localtime: ", time.localtime())
print("Current timezone name: ", time.tzname)
print(time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.localtime()))
#year = time.strftime("%Y", time.localtime())
# print(year)
'''
