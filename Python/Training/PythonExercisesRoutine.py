#!python3


# Basic Syntax
#
# 1, Write a program that asks the user for a number (integer only) and prints the sum of its digits
# number = input("Plz input a number(integar only): ")
# numList = []
# for i in str(number):
#    numList.append(int(i))
# print(sum(numList))

#
# 2, Write a program that takes a file name as command line argument,
# count how many times each word appears in the file and prints the word that appears the most
# (and its relevant count)
with open("input.txt", "r") as f:
    read_data = f.read()
    low_string = read_data.lower().replace(
        ' ', '').replace(',', '').replace('\n', '')
    print(low_string.split())
    myResult = {}
    for letter in low_string:
        myResult[letter] = low_string.count(letter)
    order_result = [(k, myResult[k])
                    for k in sorted(myResult, key=myResult.get, reverse=True)]
    print(order_result)

total = map(
    lambda x: sum([int(i) for i in x]),
    "123"
)
print(total)
