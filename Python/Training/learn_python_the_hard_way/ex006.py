#!python

x = "There are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

#Print 'There are 10 types of people.'
print x
#Print 'Those who know binary and those who don't.'
print y

#Print 'I said: There are 10 types of people.'
print "I said: '%s'." % x
print "I said: '%r'." % x
#Print 'I also said: Those who knoe binary and those who don't.'
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

#Print 'Isn't that joke so funny?! False'
print joke_evaluation % hilarious

w = "This is the left side of..."
e = "a string with a right side."

#Print 'This is the left side of... a string with a right side.'
print w + e
print w , e
