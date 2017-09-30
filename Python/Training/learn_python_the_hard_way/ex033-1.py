#!python

numbers = []

def myloop(nums, increment):
    i = 0
    while i < nums:
        print "the top number is: %d" % i
        i += increment
        numbers.append(i)
        print "Now Numbers: " , numbers
        print "the bottom number is: %d" % i

def display_numbers(x):
    for y in x:
        print "That numbers include: %r" % y


user_input_number = int(raw_input("input number 1 to 10>>> "))
user_input_increment = int(raw_input("input number that you want to increment>>>"))

myloop(user_input_number, user_input_increment)

display_numbers(numbers)
