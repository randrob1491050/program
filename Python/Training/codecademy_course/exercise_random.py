#!python

from random import randint

num = randint(1,100)
print "pls input you guess number"

result = False;

while result == False:
	answer = input()

	if answer<num:
		print "is too small"
	if answer>num:
		print "is too big"
	if answer==num:
		print "BINGO"
		result = True