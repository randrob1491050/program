#!python

def add(a, b):
    print "%d add %d" % (a, b)
    return a + b
def subtract(a, b):
    print "%d subtract %d" % (a, b)
    return a - b
def multiply(a, b):
    print "%d multiply %d" % (a, b)
    return a * b
def divide(a, b):
    print "%d divide %d" % (a, b)
    return a / b

age = add(11, 22)
height = subtract(22, 11)
weight = multiply(1, 2)
iq = divide(100, 10)

print "age is %d\nheight is %d\nweight is %d\niq is %d\n" % (age, height, weight, iq)

print "Here is a puzzle."

# 33+[11-(10/2*2)] = 33+1 = 34
what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
