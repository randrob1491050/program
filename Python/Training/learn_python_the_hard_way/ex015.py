#!python

from sys import argv

#get scrip_name and file_name from argv
script, filename = argv
# open files to txt
txt = open(filename)
#display file_name
print "Here's your file %r:\n" % filename
#read txt
print txt.read()

txt.close()

print "Please input file name:"
promte = ">>"
filename = raw_input(promte)
content = open(filename)
print content.read()

content.close()


