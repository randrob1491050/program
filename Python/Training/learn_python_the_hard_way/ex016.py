#!python

from sys import argv

script, filename = argv

print "We want to earse that %r." % filename
print "If yout don't do it,can hit Crtl+C stop"
print "Or enter continue it."

raw_input("?")

print "Opening that file"
txt = open(filename, "w")

#print "Truncating that file"
#txt.truncate()

print "Now you can input three line."

line1 = raw_input("Line1:")
line2 = raw_input("Line2:")
line3 = raw_input("Line3:")

print "i'm put above three line put in new file."
'''
txt.write(line1)
txt.write("\n")
txt.write(line2)
txt.write("\n")
txt.write(line3)
txt.write("\n")
'''
msg = "%s \n%s \n%s \n" % (line1, line2, line3)
txt.write(msg)

print "And Finally,we close it."
txt.close()

