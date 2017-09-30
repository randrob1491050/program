print "Welcome to the English to Pig Latin translator!"

original = raw_input("Enter some word?")

if len(original) != 0 and original.isalpha():
    print original
else:
    print "empty"