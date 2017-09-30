#!python

print "we needs you to input something into which windows."
print "we have 1# and 2# windows,you can choose that numbers."

windows = raw_input(">>>> ")

if windows == "1":
    print "good,you into the 1 window"
    print "welcome to 1 window,there does offer some food.you can pick something"
    print "we have apple,orange,banbale"

    food = raw_input("pls input number 1 or 2 to pick something: ")

    if food == "1":
        print "you was choose pick apple"
    elif food == "2":
        print "you was choose pick orange"
    else:
        print "nothing"

elif windows =="2":
    print "bad,you into the 2 window"
    print "welcome to 2 window,there does offer some bad.you need skip it"
    print "you can choose between number 1 to 10,now begin."

    skips = int(raw_input(">>>>>> "))

    if skips == 2 or skips == 10:
        print "bingo"
    elif int(skips) >= 11:
        print "do not over number 1 to 10"
    else:
        print "you do not choose right number,pls play again"

else:
    print "no,you can't into any window"
