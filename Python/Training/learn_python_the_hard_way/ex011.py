#!python

print "What is Your name?",
name = raw_input()
print "What old are you?",
age = raw_input()
print "How much tall you are?",
tall = raw_input()

print (age, type(age))

print "Your name is %s.\nYour age is %s.\nYou tall have %s.\n" % (
    name, age ,tall)

print "Your name is %r.\nYour age is %r.\nYou tall have %r.\n" % (name, age ,tall)
