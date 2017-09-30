#!python

from sys import argv
from os.path import exists

scripts, from_files, to_files = argv

print "we need to cp %r to %r" % (from_files, to_files)
print "that %s does opened" % (from_files)
src = open(from_files)
print "that %s does readed" % (from_files)
src_data = src.read()
print "that %s lens is: %d" % (from_files, len(src_data))

print "that file %s already exists" %  exists(to_files)
print "you can hit ctrl+c or"
print "enter continue."
raw_input(">>>")

print "create new file and write"
des = open(to_files, "w")
des.write(src_data)
print "write file finish"

print "Now close src and des files"
src.close()
des.close()
