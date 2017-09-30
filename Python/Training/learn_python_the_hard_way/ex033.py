#!python

i = 0
number = []

while i < 5:
    print "the top number is %d" % i
    i += 1
    number.append(i)
    print "Number Now:", number
    print "the bottom number is %d" % i

print "Now that numbers include:"

for num in number:
    print "%r" % num


