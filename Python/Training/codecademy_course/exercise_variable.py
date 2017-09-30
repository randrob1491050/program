a = True
b = not a

if b == False:
	print "BINGO"

if (a == b) == False:
	print "BINGO"
else:
	print "WRONG"

if (a != b) == True:
	print "BINGO"
else:
	print "WRONG"

if (a and b) == False:
	print "BINGO"
else:
	print "WRONG"

if (a or b) == True:
	print "BINGO"
else:
	print "WRONG"

if (1<2 and b==True) == False:
	print "BINGO"
else:
	print "WRONG"