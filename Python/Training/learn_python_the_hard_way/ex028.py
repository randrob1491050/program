#!python


print "True and True"
print "\t result: True"

print "False and True"
print "\t result: False"

print "1 == 1 and 2 == 1"
print "\t result: False"

print '"test" == "test"'


print "1 == 1 or 2 != 1"
print "\t result: True"

print "True and 1 == 1"
print "\t result: True"

print '"False and 0 != 0"'
print "\t result: False"

print '"True or 1 == 1"'
print "\t result: True"

print '"test" == "testing"'
print "\t result: False"

print '1 != 0 and 2 == 1'
print "\t result: False"

print '"test" != "testing"'
print "\t result: True"

print '"test" == 1'
print "\t result: False"

print 'not (True and False)'
print "\t result: True"

print 'not (1 == 1 and 0 != 1)'
print "\t result: False"

print 'not (10 == 1 or 1000 == 1000)'
print "\t result: False"

print 'not (1 != 10 or 3 == 4)'
print "\t result: False"

print 'not ("testing" == "testing" and "Zed" == "Cool Guy")'
print "\t result: True"

print '1 == 1 and (not ("testing" == 1 or 1 == 0))'
print "\t result: True"

print '"chunky" == "bacon" and (not (3 == 4 or 3 == 3))'
print "\t result: False"

print '3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))'
print "\t result: False"

