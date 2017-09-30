#!python

print 'Guess what I think?'
num = 10
bingo = False

while bingo == False: 
	answer = input()

	if answer<num:
		print '%d too samll' % answer
	if answer>num:
		print '%d too big' % answer
 	if answer==num:
		print 'BINGO,%d is the right answer' % answer	
		bingo = True
