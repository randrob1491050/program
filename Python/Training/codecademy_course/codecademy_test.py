'''
squares = [i**2 for i in range(1,11)]
print filter(lambda x: x >=30 and x <=70 , squares)
'''

'''
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X" ,garbled)
print message
'''

'''
def denary2binary(number):
    binStr = ''
    if number < 0:  raise ValueError, "must be a positive integer"
    if number == 0: return '0'
    while number > 0:
        binStr = str(number % 2) + binStr
        print number
        number = number >> 1
        print number
    return "0b" + binStr

denary2binary(int(8))
'''

