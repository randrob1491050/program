#!python

from sys import argv

script, filename = argv

print "Open file: %r." % filename
txt = open(filename)

print "Display file content:"
print txt.read()

print "Now close that file"
txt.close()


