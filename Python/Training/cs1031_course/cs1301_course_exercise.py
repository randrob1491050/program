#!python3

### about data type conversion
my_boolen = True
boolen_as_integer = int(my_boolen)
my_integer = "5.1"
integer_as_boolen = bool(my_integer)

print(boolen_as_integer)
print(integer_as_boolen)

### about input usage
myInt = input("Pls input interger: ")
print(int(myInt) * int(myInt))

#### getting reserved word in python
import keyword
print(keyword.kwlist)

### About list in python
mystery_int_1 = 15
mystery_int_2 = 5

def factors(n):
    myList = []
    for i in range(1, n+1):
        if n % i == 0:
            myList.append(i)
    return myList

myResult1 = factors(mystery_int_1)
myResult2 = factors(mystery_int_2)

print(myResult1)
print(myResult2)

if mystery_int_1 in myResult2 or mystery_int_2 in myResult1:
    print("Factors!")

### About four usage about functions print
team_1 = "Georgia Tech"
team_1_score = 29
team_2 = "Georgia"
team_2_score = 28

if team_1_score > team_2_score:
    winner = team_1
    loser = team_2
    margin = team_1_score - team_2_score
    print("%s beat %s by %s" % (winner, loser, margin))
    print(winner, "beat", loser, "by", margin)
    print(winner + " beat " + loser + " by " + str(margin))
    print("{0} beat {1} by {2}".format(winner, loser, str(margin))) 
elif team_2_score > team_1_score:
    winner = team_2
    loser = team_1
    margin = team_2_score - team_1_score
    print("%s beat %s by %s" % (winner, loser, margin))
else:
    print("%s played %s and it was a tie" % (team_1, team_2))


#Imagine you're choosing between the following restaurants:
#
# - Barrelhouse: Closes at 11:00PM
# - Taco Bell: Closes at 2:00AM
# - Cookout: Closes at 3:00AM
# - Waffle House: Never closes. Ever.
#
#Assume that this list is also a priority list: if Barrelhouse
#is open, you choose Barrelhouse. If not, you choose Taco Bell
#if it's open. If not, you choose Cookout if it's open. If
#not, you choose Waffle House.
#
#However, there are two wrinkles:
#
# - We're using 12-hour time.
# - hour will always represent a time from 10PM to 5AM.
#
#That means that if hour is 10, 11, or 12, it's PM; if hour
#is 1, 2, 3, 4, or 5, it's AM. This will make your reasoning
#a little more complex. You may assume that all four
#restaurants open later than 6AM, though, so you don't have
#to worry about opening time, just closing time.
#
#Add some code below that will print what restaurant you'll
#go to based on the current values of hour and minute.

hour = 12
minute = 45

PM=[10,11,12]
AM =[1,2,3,4,5]
if hour in PM:
    if hour >5 and hour <11:
        print("Barrelhouse")
    else:
        print("Taco Bell")
if hour in AM:
    if hour >=1 and hour <2 :
        print("Taco Bell")
    elif hour <3:
        print("Cookout")
    else:
        print("Waffle House")


#Atlanta is full of great coffee places. Unfortunately, great
#coffee is usually expensive. The variables above will
#contain a balance and a cafe name. Below are the prices of
#a cup of coffee at each of three locations:
#
# - Octane: $6
# - Galloway: $5
# - Starbucks: $4
# - Revelator: $3
# - Dunkin: $2
#
#Add some code above that will print one of the following
#two messages depending on whether the value of balance is
#high enough to buy a cup of coffee at the given cafe.
#
# - If it is sufficient, print "With [balance] dollars, I
#   can buy coffee at [cafe]"
# - If it is not sufficient, print "With [balance] dollars,
#   I cannot buy coffee at [cafe]"

cafe = "Starbucks"
balance = 4.5

can_afford = True

if cafe == "Octane" and balance < 6:
    can_afford = False
if cafe == "Galloway" and balance < 5:
    can_afford = False
if cafe == "Starbucks" and balance < 4:
    can_afford = False
if cafe == "Revelator" and balance < 3:
    can_afford = False
if cafe == "Dunkin" and balance < 2:
    can_afford = False

if can_afford:
    print("With", balance, "dollars, I can buy coffee at", cafe)
else:
    print("With", balance, "dollars, I cannot buy coffee at", cafe)


### About For Loops
mystery_string = "CS1301"
## a for loop
for count in range(0, len(mystery_string)):
    print(count, mystery_string[count])
## a for-echo loop
myCount = 0
for letter in mystery_string:
    print(myCount, letter)
    myCount += 1

### About While loops
mystery_value = 87
while not mystery_value >100:
    mystery_value += 9
    print(mystery_value)


#For example, if mystery_int is 5, this could print:
#
#1	2	3	4	5
#2	4	6	8	10
#3	6	9	12	15
#4	8	12	16	20
#5	10	15	20	25

mystery_int = 3

# One way
myRow = []
for i in range(1, mystery_int+1):
    myRow.append(i)
#print(myRow)

for j in range(1,mystery_int+1):
    #print(j)
    myString = ""
    for n in myRow:
        n *= j
        myString += str(n) + "\t"
    print(myString)

# Another Way
for i in range(1, mystery_int + 1):
    row_string = ""
    for j in range(1, mystery_int + 1):
        product = i * j
        row_string += str(product) + "\t"
    print(row_string)


#For example, if the string was "Lucy", then the output would be:
#L
#Lu
#Luc
#Lucy

mystery_string = "Lucy"

current_words = ""
for runs in range(0, len(mystery_string)):
    current_words += mystery_string[runs]
    print(current_words, end="")
    print("")

#Use a loop to find the sum of all numbers between 0 and
#mystery_int, including bounds (meaning that if
#mystery_int = 7, you add 0 + 1 + 2 + 3 + 4 + 5 + 6 + 7).

mystery_int = -5
## for loop
if mystery_int >= 0:
    total = 0
    for i in range(0, mystery_int+1):
        total += i
    print(total)
else:
    total = 0
    for i in range(0, mystery_int-1, -1):
        total += i
    print(total)

## while loop
current_sum = 0
if mystery_int > 0:
    while mystery_int > 0:
        current_sum += mystery_int
        mystery_int -= 1
else:
    while mystery_int < 0:
        current_sum += mystery_int
        mystery_int += 1
print(current_sum)

### About Count-Down
mystery_int = 46

## one way
counter = 3
print(mystery_int)
while mystery_int >0:
    mystery_int -= counter
    if mystery_int <0:
            break
    print(mystery_int)

## another way
while mystery_int >= 0:
    print(mystery_int)
    mystery_int -= 3


#Add some code below that will count and print how many
#times the character sequence "cat" appears in mystery_string.
#For example, for the string above, it would print 2.

mystery_string = "my cat your cat"
#mystery_string = "catcatcattf"
#mystery_string = "cacacat cacacat"

# One way
sum = 0
current_word = ""
length = len(mystery_string)
for i in range(length):
    if mystery_string[i] == 'c':
        if mystery_string[i+1] == 'a':
            if mystery_string[i+2] == 't':
                current_word += 'cat'
                sum += 1
print(sum)
print(current_word)

## Another ways
count = 0
current_search_letter = "c"

for letter in mystery_string:
    if letter == "c" and current_search_letter == "c":
        current_search_letter = "a"
    elif letter == "a" and current_search_letter == "a":
        current_search_letter = "t"
    elif letter == "t" and current_search_letter == "t":
        count += 1
        current_search_letter = "c"
    else:
        current_search_letter = "c"
print(count)

### Time and Date
from datetime import date
def get_todays_date ():
    myDate = date.today()
    myYear = myDate.year
    myMonth = myDate.month
    myDay = myDate.day
    return (str(myYear) + '/' + str(myMonth) + '/' + str(myDay))
print(get_todays_date())


### how to reverse strings
def reverse(a_string):
    rev = ""
    for i in range(len(a_string)-1, -1, -1):
        rev = rev + a_string[i]
    return rev
rev = reverse("This string should be reversed!")
print(rev)


### Multiple try-catch conditions
mystery_value = 0
#mystery_value = 1
#mystery_value = "cat"

try:
    myresult_1 = mystery_value / mystery_value
    print(myresult_1)
except:
    try:
        myresult_2 = mystery_value / ( mystery_value + 5)
        print(myresult_2)
    except:
        myresult_3 = mystery_value * 5
        print(myresult_3)

### About parameter default values 
def find_pressure(n, T, V, R=0.082057):
    try:
        myResult = (n * R * T) / V
        return myResult
    except ZeroDivisionError:
        return ("Volume must be greater than 0")

test_n = 10
test_T = 298
test_V = 5
test_R = 62.364 #Torr!
print("Result:", find_pressure(test_n, test_T, test_V, R = test_R))


### how count multiple consecutive spaces to one
## one way: rebuild string with split and join, remove multiple consecutive spaces
def word_count(my_string):
    try:
        num = 0
        newString = ' '.join(my_string.split())
        #print(newString)
        for i in newString:
           if i == " ":
                num += 1
    except:
        return ("Not a string")
    else:
        return (num+1)

## Other way: using True and False conditions
def word_count(my_string):
    try:
        word_count = 1
        previous_was_space = False
        for letter in my_string:
            if letter == " " and not previous_was_space:
                word_count += 1
            if letter == " ":
                previous_was_space = True
            else:
                previous_was_space = False
        return word_count
    except TypeError:
        return "Not a string"

## Another way: using index method
def word_count(my_string):
    try:
        word_count = 1
        for i in range(1, len(my_string)):
		if my_string[i] == " ":
            if not my_string[i - 1] == " ":
                word_count += 1
    except:
        return "Not a string"

## Another way: using replace method
def word_count(my_string):
    try:
        while "  " in my_string:
            my_string = my_string.replace("  ", " ")
        word_count = 1
        for letter in my_string:
            if letter == " ":
                word_count += 1
        return word_count
    except TypeError:
        return "Not a string"

print("Word Count:", word_count("Four words are here!"))
print("Word Count:", word_count("Hi   David"))
print("Word Count:", word_count(5))
print("Word Count:", word_count(5.1))
print("Word Count:", word_count(True))


def average_word_length(my_string):
    try:
        punctuation = ['.', ',', '!', '?']
        newString = ""
        for p in punctuation:
            while p in my_string:
                my_string = my_string.replace(p, "")
        newString =  my_string.replace(" ", "")
        if not newString:
            return("No words")
    except TypeError:
        return("Not a string")
    else:
        letter_count = 0
        for i in my_string:
            if not i == " ":
                letter_count += 1

        word_count = 1
        for i in range(1, len(my_string)):
            if my_string[i] == " ":
                if not my_string[i - 1] == " ":
                    word_count += 1
        myResult = letter_count / word_count
        return(myResult)
        
print(average_word_length("Hi"))
print(average_word_length("Hi, Lucy"))
print(average_word_length("   What   big spaces  you    have!"))
print(average_word_length(True))
print(average_word_length("?!?!?! ... !"))


### how modify output with for-loop
def steps(numbers):
    current_word = ""
    for i in range(1, numbers+1):
        current_word += "\t" * (i-1) + str(i) * 3 + "\n"
    return(current_word)
print(steps(6))

### string index usage
def string_finder(target_string, search_string):
    length_target_string = len(target_string)
    #print(length_target_string)
    length_search_string = len(search_string)
    #print(length_search_string)
    postions = target_string.find(search_string)
    #print(postions)
    if postions >= 0:
        if search_string == target_string[postions:length_search_string]:
            return("Beginning")
        if search_string == target_string[postions:]:
            return("End")
        else:
            return("Middle")
    else:
        return("Not Found")
print(string_finder("Georgia Tech", "Georgia"))
print(string_finder("Georgia Tech", "gia"))
print(string_finder("Georgia Tech", "Tech"))
print(string_finder("Georgia Tech", "Idaho"))


### string replace operations with split and join
def replace_all(target_string, find_string, replace_string):
    newString = target_string.split(find_string)
    newString = replace_string.join(newString)
    return(newString)
target = "In case I don't see ya, good afternoon, good evening, and good night!"
find = "good"
replace = "bad"
print(replace_all(target, find, replace))


### string operations with index under unregular
def in_parentheses(inString):
    try:
        return inString[inString.index("(") + 1:inString.index(")")]
    except ValueError:
        return ""
print(in_parentheses("iAawc)Je(qT"))
print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(in_parentheses("David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."))
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))


### string operations with slice under regular
def find_color(inString):
    newString = inString[4:-1]
    return(newString)
print(find_color("rgb(0, 0, 0)"))
print(find_color("rgb(0,0,0)"))
print(find_color("rgb(125, 50, 75)"))
print(find_color("rgb(125, 17, 125)"))
print(find_color("rgb(217, 217, 217)"))


### multiple try-except usage
def input_type(inString):
    if inString == "True" or inString == "False":
        return("boolean")
    try:
        int(inString)
        return("integer")
    except:
        try:
            float(inString)
            return("float")
        except:
            return("string")
print(input_type(""))
print(input_type("False"))
print(input_type("7.432621"))
print(input_type("2788"))


### List operations
import math
a_list = [19, 7, 71.34260578068043, 82, 92.16621472300301, 48, 46.11832778043146]
def modify_list(inList):
    inList.sort()
    inList.reverse()
    #print(inList)
    del inList[-3:]
    #print(inList)
    for item in inList:
        if item == 7:
            inList.remove(7)
    inList[0] = inList[0] * 2
    inList[2] = inList[2] * 2
    return(inList)
print(modify_list(a_list))


### About booleans estimate
#The function should perform as follows:
#
# - If use_and is True, the function should return True if
#   every item in the list is True (simulating the and
#   operator).
# - If use_and is False, the function should return True if
#   any item in the list is True (simulating the or
#   operator).
def one_dimensional_booleans(bool_list, use_and):
    if not use_and:
        return True in bool_list
    else:
        return not False in bool_list
print(one_dimensional_booleans([True, True, True], True))
print(one_dimensional_booleans([True, False, True], True))
print(one_dimensional_booleans([True, False, True], False))
print(one_dimensional_booleans([False, False, False], False))
print(one_dimensional_booleans([True, False], False))


## multiple function
def one_dimensional_booleans(bool_list, use_and):
    if not use_and:
        return True in bool_list
    else:
        return not False in bool_list
def two_dimensional_booleans(aLol, aBool):
    newBool = []
    for list_plot in aLol:
        newBool.append((one_dimensional_booleans(list_plot, aBool)))
    return(newBool)
bool_superlist = [[True, True, True], [True, False, True], [False, False, False]]
print(two_dimensional_booleans(bool_superlist, True))
print(two_dimensional_booleans(bool_superlist, False))


### about some list mothed
def sort_artists(inList):
    artist_name = []
    artist_album = []
    for artList in inList:
        #print(artList)
        artist_name.append(artList[0])
        artist_album.append(artList[1])
    artist_name.sort()
    artist_album.sort()
    artist_album.reverse()
    return(artist_name, artist_album)        
artists = [("The Beatles", 270.8), ("Elvis Presley", 211.5), ("Michael Jackson", 183.9)]
print(sort_artists(artists))


### print the items in myList in reverse order
myList = [1, 2, 3, 4, 5]
i = len(myList) - 1
while i >= 0:
    print(myList[i])
    i -= 1
## Another way
for i in range(len(myList) - 1, -1, -1):
    print(myList[i])


### About List and Conditions
#For example:
#  lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]) -> True
#  lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]) -> False
def lucky_sevens(inList):
    for num in range(len(inList)):
        try:
            if inList[num] == 7 and inList[num+1] == 7 and inList[num+2] == 7:
                return(True)
        except:
            return(False)
    return(False)
print(lucky_sevens([4, 7, 8, 2, 7, 7, 7, 3, 4]))
print(lucky_sevens([4, 7, 7, 2, 8, 3, 7, 4, 3]))

## Another way , try it with a for-each loop
def lucky_sevens(a_list):
    consecutive_7s = 0
    for num in a_list:
        if num == 7:
            consecutive_7s += 1
        else:
            consecutive_7s = 0
        if consecutive_7s == 3:
            return True
    return False

## Another way , try it with map() functions
def lucky_sevens(a_list):
    #map() takes two arguments: a function and a list. It returns
    #a new list created by applying that function to each item in
    #that list:
    a_list_as_strings = map(str, a_list)
    a_list_as_one_string = "".join(a_list_as_strings)
    return "777" in a_list_as_one_string

    #All of which could becompressed down to one line:
    #return "777" in "".join(map(str, a_list))


### About List and Tuple
#The function should return the movie from the list that
#had the most sales. Return only the movie name, not the
#full tuple.
def find_max_sales(inList):
    movie_score = []
    for items in inList:
        movie_score.append(items[1])
    movie_score.sort()
    high_score = movie_score.pop()
    for items in inList:
        (movie_name, movie_score) = items
        if movie_score == high_score:
            return(movie_name)
movie_list = [("Finding Dory", 486), ("Captain America: Civil War", 408), ("Deadpool", 363), ("Zootopia", 341), ("Rogue One", 529), ("The Secret Life of Pets", 368), ("Batman v Superman", 330), ("Sing", 268), ("Suicide Squad", 325), ("The Jungle Book", 364)]
print(find_max_sales(movie_list))

## Another way
def find_max_sales(movie_list):
    #To start, we want to keep track of the movie with
    #the highest sales so far (so we can return it), and
    #what its sales were (so we can compare it). Let's
    #create these:
    current_max_movie = ""
    current_max_sales = -1
    #Note that we initially set current_max_sales to -1.
    #That's one way to guarantee that the first movie
    #we look at becomes our maximum: we know its sales
    #are going to be more than -1.
    #
    #Now, let's go through each movie in the list:
    for movie_tuple in movie_list:
        #And check if its sales are higher than our
        #current max:
        if movie_tuple[1] > current_max_sales:
            current_max_sales = movie_tuple[1]
	    current_max_movie = movie_tuple[0]
    return current_max_movie

## Another way , more clever
def find_max_sales(movie_list):
    current_max_tuple = movie_list[0]
    for movie_tuple in movie_list:
        if movie_tuple[1] > current_max_tuple[1]:
            current_max_tuple = movie_tuple
    return current_max_tuple[0]


### About using index and list instead of strings.split
def string_splitter(inString):
    newList = []
    char = ""
    for i in range(0,len(inString)):
        if i == len(inString)-1:
            char  += inString[i]
            newList.append(char)
        elif inString[i] == " ":
            newList.append(char)
            char = ""    
        else:
            char += inString[i]
    return(newList)
print(string_splitter("He llo wo rld"))
print(string_splitter("Hello"))

## Another ways , more clever
def string_splitter(a_string):
    words = []
    while " " in a_string:
        index = a_string.find(" ")
        words.append(a_string[:index])
        a_string = a_string[index + 1:]
    words.append(a_string)
    return words
print(string_splitter("Hello, world"))


### About input-output file operations
def find_coffee(inFilename):
    with open(inFilename, "r") as f:
        read_data = f.read()
        if "coffee" in read_data:
            return(True)
        else:
            return(False)
        read_data.close()
print(find_coffee("coffeeful.txt"))

### About input-output file operations
## With-As Usage - how save tuple into file
movieList = [('Rogue One', 530, 2017), ('Finding Dory', 486, 2017), ('Captain America: Civil War', 408, 2017)]
def save_info(inList):
    with open("Output.txt", "w") as f:
        for item in inList:
            print(item, file=f)
    f.close()
save_info(movieList)
## Tradition Usage - how save tuple into file
outputFile = open("movies.txt", "w")
for movie in movieList:
    print(movie, file = outputFile)
outputFile.close()
## Tradition Usage - how load tuple from file
import ast
movieList = []
inputFile = open("movies.txt", "r")
for line in inputFile:
    lineAsTuple = ast.literal_eval(line)
    movieList.append(lineAsTuple)
inputFile.close()

### About input-output file operations
def logChanges(newValue):
    logFile = open("WriteFileOutput.txt", "a")
    print("New temperature setting:", newValue, file = logFile)
    logFile.close()
logChanges(12)

### About input-output file operations
def saveList(myList, myFilename):
    outputFile = open(myFilename, "w")
    for item in myList:
        print(item, file=outputFile)
    outputFile.close()
def loadList(myFilename):
    newList = []
    inputFile = open(myFilename, "r")
    for line in inputFile:
        newList.append(line.strip())
    return newList
    inputFile.close()
test_list = ["123", "234", "345"]
saveList(test_list, "WriteFileOutput.txt")
print(loadList("WriteFileOutput.txt"))

### About input-opout with readlines()
def angry_file_finder(filename):
    with open(filename, "r") as f:
        for line in f.readlines():
            print(line)
            if not "!" in line:
                f.close()
                return(False)
        f.close()
        return(True)
print(angry_file_finder("input.txt"))


### About input-output file operations - Coding Problem 4.4.6
def sort_films(inFile, outFile):
    with open(inFile, "r") as f:
        current_all_list = []
        current_grade_list = []
        for line in f.readlines():
            line = line.strip().split("\t")      #remove Line break - one way
            #line = line.split("\t")             #remove Line break - another way
            #line = [x.strip() for x in line]    
            inTuple = (line[0], line[1])
            current_all_list.append(inTuple)
            current_grade_list.append(line[1])
        current_grade_list.sort()
        current_grade_list.reverse()
        #return(current_all_list, current_grade_list)
    with open(outFile, "w") as f1:
        for grade in current_grade_list:
            for movieline in current_all_list:
                if movieline[1] == str(grade):
                    print(movieline[0], "\t", movieline[1], file=f1)
    f.close()
    f1.close()

sort_films("input.txt", "output.txt")
print("Done!")


### About dictionary
### punctuation marks in the string will be 
### periods句号,commas逗号,question marks问号, exclamation points感叹号, and apostrophes撇号.
def word_lengths(inString):
    myString = inString.replace(".", "")
    myString = myString.replace(",", "")
    myString = myString.replace("?", "")
    myString = myString.replace("!", "")
    myString = myString.replace("'", "")
    myString = myString.lower()
    myString_split = myString.split(" ")
    myDict = {}
    for word in myString_split:
        myDict[word] = len(word)
    return(myDict)
print(word_lengths("Joe made the sugar cookies, Susan decorated them."))

### About dictionary - addition values with list data structure type
def length_words(inString):
    mark_list = ".,?!'"
    for mark in mark_list:
        myString = inString.replace(mark, "")
    myString = myString.lower()
    myString_split = myString.split(’ ‘)
    myResult_dict = {}
    for word in myString_split:
        if len(word) not in myResult_dict.keys():
            myResult_dict[len(word)] = []
        word_list = myResult_dict[len(word)]
        word_list.append(word)
    return(myResult_dict)
print(length_words("I ate a bowl of cereal out of a dog bowl today."))

### About how iterate key on dictionary 
def modify_dict(name_dict):
    #The hint in the original instructions tells you that
    #we can't iterate through the dictionary and delete
    #items from it at the same time. Why not? When
    #iterating, Python keeps a pointer to the current item.
    #When you delete an item, every item slides back one
    #spot -- so the pointer is now pointing to what *was*
    #the next item. Then, when it gets the next item, it
    #skips what was actually the next item.
    #
    #So instead, we want to first make a list of all the
    #keys we want to delete. First, we initialize an
    #empty list:
    del_list = []
    #Then we iterate through the keys:
    for key in name_dict:
        if key != key.capitalize():
            del_list.append(key)
    #Once that's done, del_list has a list of all the
    #keys in name_dict to delete. Now we want to iterate
    #through the keys we stored into del_list. Note that
    #this is okay because we're iterating through del_list
    #and deleting from name_dict, *not* iterating through
    #name_dict:
    for key in del_list:
        del name_dict[key]
    return name_dict
my_dict = {'Joshua':'Diaddigo', 'joyner':'David', 'Elliott':'jackie', 'murrell':'marguerite'}
print(modify_dict(my_dict))

### About how write Classes functions within Python and learn Conctructors,getters,setters, method type 
#To summarize (and give a to-do list):
# - Create getters and setters for each variable.
# - Print a log statement when the getters and setters
#   are called.
# - Check the type of the new value inside the setters,
#   and print an error if it's the wrong type.
# - Modify the constructor body to use the getters and/or
#   setters instead of assigning values directly.
#Hint 3: Remember to put self before any instance variables
#or methods you're trying to access. For example, to access
#the method setTitle from within the constructor, you would
#need to write self.setTitle().
class TodoItem:
    def __init__(self, title, description, completed=False):
        self.title = self.setTitle(title)
        self.description = self.setDescription(description)
        self.completed = self.setCompleted(completed)
    def getTitle(self):                                     # TYPE: a Method
        print("title accessed")
        return(self.title)
    def getDescription(self):                               # TYPE: a Method
        print("description accessed")
        return(self.description)
    def getCompleted(self):
        print("completed accessed")
        return(self.completed)
    def setTitle(self, newTitle):
        print("title changed")
        if type(newTitle) == str:
            self.title = newTitle
            return(self.title)
        else:
            print("invalid value")
            self.title = None
            return(self.title)
    def setDescription(self, newDescription):
        print("description changed")
        if type(newDescription) == str:
            self.description = newDescription
            return(self.description)
        else:
            print("invalid value")
            self.description = None
            return(self.description)
    def setCompleted(self, newCompleted):
        print("completed changed")
        if type(newCompleted) is bool:
            self.completed = newCompleted
            return(self.completed)
        else:
            print("invalid value")
            self.completed = None
            return(self.completed)

### About relationship between classes and instances
### Classes can also have references to other instances of themselves 
class Person:
    def __init__(self, name, age, father=None, mother=None):        # TYPE: init method
        self.name = name                                            # TYPE: a attributes (instance variables)
        self.age = age                                              # TYPE: a attributes (instance variables)
        self.father = father                                        # TYPE: a attributes (instance variables)
        self.mother = mother                                        # TYPE: a attributes (instance variables)
george_p_mother = Person("Mrs. Burdell", 53)                        # TYPE: a new instances of this class
george_p_father = Person("Mr. Burdell", 53)
george_p = Person("George P. Burdell", 25, father=george_p_father, mother=george_p_mother)
print(george_p.name)
print(george_p.mother.name)
print(george_p.father.name)


### About use Recursion and use While-loop or for-loop or other way without Recursion
## Recursio function
def countDown(start):
    if start <= 0:
        print(start)
    else:
        print(start)
        countDown(start - 1)
print(countDown(5))
## While-loop function
def countDown2(start):
    print(start)
    while start > 0:
        start = start - 1
        print(start)
print(countDown2(5))

### About Recursion usage Factorial and Exponentiation
###it should return the product of that number times every number between itself and 1
#  4! = 4! = 4 * 3!, 3! = 3 * 2!, 2! = 2 * 1
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
print("5! is", factorial(5))
print("10! is", factorial(10))

###It should return the mathematical answer to base^expo
#  2^4 = 2 * 2^3, 2^3 = 2 * 2^2, 2^2 = 2 * 2^1, 2^1 = 2 * 2^0
def exponentCalc(base, expo):
    if expo == 0:
        return 1
    else:
        return base * exponentCalc(base, expo - 1)
print(exponentCalc(5, 3))

### calculate the nth triangular number  - n + (n -1) + (n - 2)
def tri(n):
    if n == 1:
        return 1
    else:
        return n + tri(n-1)
print("5 is", tri(5))

### About Sorting Algorithms - bubbleSort
def bubbleSort(lst):
    #Set swapOccurred to True to guarantee the loop runs once
    swapOccurred = True
    #Run the loop as long as a swap occurred the previous time
    while swapOccurred:
        #Start off assuming a swap did not occur
        swapOccurred = False
        #For every item in the list except the last one...
        for i in range(len(lst)-1):
            #If the item should swap with the next item...
            if lst[i] > lst[i + 1]:
                #Then, swap them! But these lines aren't
                #quite right: fix this code
                temp = lst[i]
                lst[i] = lst[i + 1]
                lst[i + 1] = temp
                #One more line is needed here; add it!
                swapOccurred = True
    return lst
print(bubbleSort([5, 3, 1, 2, 4]))

### About Sorting Algorithms - selectionSort
def selectionSort(aList):
    #For each index in the list...
    for i in range(len(aList)):
        #Assume first that current item is already correct...
        minIndex = i
        #For each index from i to the end...
        for j in range(i + 1, len(aList)):
            #Complete the reasoning of this conditional to
            #complete the algorithm! Remember, the goal is
            #to find the lowest item in the list between
            #index i and the end of the list, and store its
            #index in the variable minIndex.
            #
            #Write your code here!
            if aList[j] <= aList[minIndex]:
                minIndex = j
        #Save the current minimum value since we're about
        #to delete it
        minValue = aList[minIndex]
        #Delete the minimum value from its current index
        del aList[minIndex]
        #Insert the minimum value at its new index
        aList.insert(i, minValue)
    #Return the resultant list
    return aList
#The code below will test your fix. It is not used for
#grading, so feel free to modify it. As written, it should
#print a sorted list.
#print(selectionSort([5, 3, 1, 2, 4]))
print(selectionSort([6, 4, 78, 54, 44, 4, 56, 5, 12, 16, 3, 3, 2, 1]))

### About Sorting Algorithms - InsertionSort
def insertionSort(alist):
   for index in range(1,len(alist)):
    currentvalue = alist[index]
    position = index
    while position>0 and alist[position-1]>currentvalue:
        alist[position]=alist[position-1]
        position = position-1
    alist[position]=currentvalue
alist = [3, 2, 5, 6, 4, 1]
insertionSort(alist)
print(alist)

### About Sorting Algorithms - mergeSort
def mergesort(lst):
    #Then, what does it do? mergesort should recursively
    #run mergesort on the left and right sides of lst until
    #it's given a list only one item. So, if lst has only
    #one item, we should just return that one-item list.
    if len(lst) <= 1:
        return lst
    #Otherwise, we should call mergesort separately on the
    #left and right sides. Since each successive call to
    #mergesort sends half as many items, we're guaranteed
    #to eventually send it a list with only one item, at
    #which point we'll stop calling mergesort again.
    else:
        #Floor division on the length of the list will
        #find us the index of the middle value.
        midpoint = len(lst) // 2
        #lst[:midpoint] will get the left side of the
        #list based on list slicing syntax. So, we want
        #to sort the left side of the list alone and
        #assign the result to the new smaller list left.
        left = mergesort(lst[:midpoint])
        #And same for the right side.
        right = mergesort(lst[midpoint:])
        #So, left and right now hold sorted lists of
        #each half of the original list. They might
        #each have only one item, or they could each
        #have several items.
        #Now we want to compare the first items in each
        #list one-by-one, adding the smaller to our new
        #result list until one list is completely empty.
        newlist = []
        while len(left) and len(right) > 0:
            #If the first number in left is lower, add
            #it to the new list and remove it from left
            if left[0] < right[0]:
                newlist.append(left[0])
                del left[0]
            #Otherwise, add the first number from right
            #to the new list and remove it from right
            else:
                newlist.append(right[0])
                del right[0]
        #When the while loop above is done, it means
        #one of the two lists is empty. Because both
        #lists were sorted, we can now add the remainder
        #of each list to the new list. The empty list
        #will have no items to add, and the non-empty
        #list will add its items in order.
        newlist.extend(left)
        newlist.extend(right)
        #newlist is now the sorted version of lst! So,
        #we can return it. If this was a recursive call
        #to mergesort, then this sends a sorted half-
        #list up the ladder. If this was the original
        #call, then this is the final sorted list.
        return newlist
#Let's try it out!
print(mergesort([2, 5, 3, 8, 6, 9, 1, 4, 7]))


### About Search Algorithms - linear Search only for unsorted data
def linear(inList, inString):
    for idx_num in range(len(inList)):
        if inString == inList[idx_num]:
            return(idx_num)
    return(False)
print(linear(["bob", "fred"], "fred"))
print(linear([1, 5, 4, 3, 6, 7], 7))


### About Search Algorithms - Binary Search only for sorted data
#Let's implement a binary search using a loop! 
def binary_search(searchList, searchTerm):
    #First, the list must be sorted.
    searchList.sort()
    #Now, each iteration of the loop, we want to narrow
    #down the part of the list to look at. So, we need to
    #keep track of the range we've narrowed down to so
    #far. Initially, that will be the entire list, from
    #the first index to the last.
    min = 0
    max = len(searchList) - 1
    #Now, we want to loop as long as our range has any
    #numbers left to investigate. As long as there is
    #more than one number between minimum and maximum,
    #we're not done searching.
    while min <= max:
        #We want to check the middle item of the
        #current range, which is the average of the
        #current minimum and maximum index. For
        #example, if min was 5 and max was 15, our
        #middle number would be at index 5. We'll
        #use floor division because indices must be
        #integers.
        currentMiddle = (min + max) // 2
        #If the term in the middle is the term we're
        #looking for, we're done!
        if searchList[currentMiddle] == searchTerm:
            return True
        #If not, we want to check if the term we're
        #looking for should come earlier or later.

        #If the term we're looking for is less than
        #the current middle, then search the first
        #half of the list:
        elif searchTerm < searchList[currentMiddle]:
            max = currentMiddle - 1

        #If the term we're looking for is greater
        #than the current middle, search the second
        #half of the list:
        else:
            min = currentMiddle + 1

        #Each iteration of the loop, one of three
        #things happens: the term is found, max
        #shrinks, or min grows. Eventually, either
        #the term will be found, or min will be
        #equal to max.

    #If the search term was found, this line will
    #never be reached because the return statement
    #will end the function. So, if we get this
    #far, then the search term was not found, and
    #we can return False.
    return False

#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))


### About Search Algorithms - Binary Search only for sorted data
#Let's implement a binary search using recursion! 
def binary_search(searchList, searchTerm):
    searchList.sort()
    #With each recursive call to binary_search, the size
    #of the list will be cut in half, rounding down. If
    #the search term is not found, then eventually an
    #empty list will be passed into binary_search. So,
    #if searchList is empty, we know that the search
    #term was not found, and we can return False. This
    #is the base case for the recursive binary_search.
    if len(searchList) == 0:
        return False
    #If there are still items in the list, then we want
    #to find if searchTerm is greater than, less than,
    #or equal to the middle term in the list. For that,
    #we need the index of the middle term.
    middle = len(searchList) // 2

    #First, the easy case: if it's the middle term, we
    #found it! Return True.
    if searchList[middle] == searchTerm:
        return True

    #If the search term is less than the middle term,
    #then repeat the search on the left half of the
    #list.
    elif searchTerm < searchList[middle]:
        return binary_search(searchList[:middle], searchTerm)

    #If the search term is greater than the middle
    #term, then repeat the search on the right half
    #of the list.
    else:
        return binary_search(searchList[middle + 1:], searchTerm)

    #As long as there are items to be searched, binary_search
    #will keep getting called on smaller and smaller lists,
    #until eventually the item is found or the list of possible
    #places it could be found is empty.

#Let's try it out!
intlist = [12, 64, 23, 3, 57, 19, 1, 17, 51, 62]
print("23 is in intlist:", binary_search(intlist, 23))
print("50 is in intlist:", binary_search(intlist, 50))

#Want to see something else interesting? Because of
#the way Python handles types, this exact same
#function works for any sortable data type. Check
#it out with strings:
strlist = ["David", "Joshua", "Marguerite", "Jackie"]
print("David is in strlist:", binary_search(strlist, "David"))
print("Lucy is in strlist:", binary_search(strlist, "Lucy"))

#Or with dates!
from datetime import date
datelist = [date(1885, 10, 13), date(2014, 11, 29), date(2016, 11, 26)]
print("10/13/1885 is in datelist:", binary_search(datelist, date(1885, 10, 13)))
print("11/28/2015 is in datelist:", binary_search(datelist, date(2015, 11, 28)))

### for-loop version instead of len()
def strLength(myStr):
    n = 0 
    for l in myStr:
        if l == None:
            return(False)
        else:
            n += 1
    return(n)
print(strLength("15 characters"))

### recursive version instead of len()
def strLength(myStr):
    if myStr == '':
        return(0)
    else:
        return(1 + strLength(myStr[1:]))
print(strLength("15 characters"))


def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
print("fib(5) is", fib(5))
print("fib(10) is", fib(10))

def fib3(n):
    if n == 1 or n == 2 or n == 3: 
        return 1
    else:
        return fib3(n - 1) + fib3(n - 2) + fib3(n - 3)
print(fib3(7))


from datetime import date
def binary_year_search(searchList, searchTerm):
    searchList.sort()
    if len(searchList) == 0:
        return False
    middle = len(searchList) // 2
    myDate = searchList[middle]
    #print(myDate.year)
    if myDate.year == searchTerm:
        return True
    elif searchTerm < myDate.year:
        return binary_year_search(searchList[:middle], searchTerm)
    else:
        return binary_year_search(searchList[middle + 1:], searchTerm)

#The lines below will test your code. If it's working
#correctly, they will print True, then False.
listOfDates = [date(2016, 11, 26), date(2014, 11, 29), 
               date(2008, 11, 29), date(2000, 11, 25), 
               date(1999, 11, 27), date(1998, 11, 28), 
               date(1990, 12, 1), date(1989, 12, 2), 
               date(1985, 11, 30)]

print(binary_year_search(listOfDates, 2016))
print(binary_year_search(listOfDates, 2007))



### Class and Function with three instance variables
class Person:
    def __init__(self, name, age, GTID):
        self.set_name(name)
        self.set_age(age)
        self.set_GTID(GTID)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_GTID(self, GTID):
        self.GTID = GTID

    def get_name(self):
        return self.name

    def get_age(self):
       return self.age

    def get_GTID(self):
        return self.GTID

def same_person(person1, person2):
    if person1.get_GTID() == person2.get_GTID():
        return(True)
    else:
        return(False)

person1 = Person("David", 30, 901234567)
person2 = Person("D. Joyner", 29, 901234567)
person3 = Person("David", 30, 903987654)
print(same_person(person1, person2))
print(same_person(person1, person3))


### Instances as Arguments
class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label
class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
def get_song_string(song):
    mystring = '"' + song.name +'"'+ " - " + song.artist.name +  " (" + str(song.year) + ")"
    return mystring
newArtist = Artist("Taylor Swift", "Big Machine Records, LLC")
newSong = Song("You Belong With Me", "Fearless", 2008, newArtist)
print(get_song_string(newSong))


### Instance Assignments
class Artist:
    def __init__(self, name, label):
        self.name = name
        self.label = label
class Song:
    def __init__(self, name, album, year, artist):
        self.name = name
        self.album = album
        self.year = year
        self.artist = artist
song1 = Song("You Belong With Me", "Fearless", 2008, Artist("Taylor Swift", "Big Machine Records, LLC"))
song2 = Song("All Too Well", "Red", 2012, song1.artist)
song3 = Song("Up We Go", "Midnight Machines", 2016, Artist("LIGHTS", "Warner Bros. Records Inc."))
print(song3.name)
print(song3.album)
print(song3.year)
print(song3.artist.name)
print(song3.artist.label)


class FibSeq:
    def __init__(self):
        self.back1 = 1
        self.back2 = 0
    def next_number(self):
        total = self.back1 + self.back2
        self.back2 = self.back1
        self.back1 = total
        return(total)
newFib = FibSeq()
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())
print(newFib.next_number())


class Number:
    def __init__(self, value, even):
        self.value = value
        self.even = even
number_instance = Number(101, False)
print(number_instance.value)
print(number_instance.even)


def french2eng(sentence):
    inString = sentence.lower()
    inList = inString.split()
    #return(inList)
    for index_num in range(len(inList)):
        if inList[index_num] in french_dict:
            inList[index_num] = french_dict[inList[index_num]]
    inList = ' '.join(inList)
    return(inList)    

french_dict = {"me": "moi", "hello": "bonjour", 
               "goodbye": "au revoir", "cat": "chat", 
               "dog": "chien", "and": "et"}
print(french2eng("Hello it's me"))


def course_info(inTuple):
    #return len(inTuple)
    tmpList = []
    sum = 0
    for item in inTuple:
        tmpList.append(item[0])
        sum += item[1]
    #return(tmpList)
    tmpInt = sum / len(inTuple)
    ourDict = {"students":tmpList, "avg_age":tmpInt}
    return(ourDict)
student_list = [('Maria', 18), ('Ashtyn', 25), ('Marco', 23), ('Jesse', 23), ('Marco', 25), ('Lucy', 21), ('David', 20), ('Taryn', 21), ('Haylee', 24), ('David', 18)]
print(course_info(student_list))



### about how split output
def reader(filename):
    with open(filename, "r") as f:
        line_list = []
        main_dict = {}
        sub_dict = {}
        #for line in f:                            # Single LIST TYPE, OUTPUT: ['3', 'exam_1', '95', '100', '0.5\n']
        #    line = line.split(" ")
        #    number, name, grade, total, weight = line
        #    return(number, name, grade, total, float(weight))
        #    return(line)
        #    print(line)
        for line in f:
            line = line.strip().split(" ")       # Single LIST TYPE, OUTPUT: ['1', 'assignment_1', '85', '100', '0.25']
            #return(line)
            sub_dict = {"number": int(line[0]), "grade": int(line[2]), "total": int(line[3]), "weight": float(line[4])}
            main_dict[str(line[1])] = sub_dict
        #for line in f:                           # Multiple OUTPUT: ['1 assignment_1 85 100 0.25\n', '2 test_1 90 100 0.25\n', '3 exam_1 95 100 0.5']
        #    line_list.append(line)
        #for line in f.readlines():               # Multiple OUTPUT: [['1 assignment_1 85 100 0.25'], ['2 test_1 90 100 0.25'], ['3 exam_1 95 100 0.5']]
        #    line = line.strip().split("\t")      # remove Line break - one way
        #    #line = line.split("\t")             # remove Line break - another way
        #    #line = [x.strip() for x in line] 
        #    line_list.append(line)
    return(main_dict)
    f.close()

print(reader("input.txt"))


'''
cat input.txt
1 assignment_1 85 100 0.25
2 test_1 90 100 0.25
3 exam_1 95 100 0.5
'''

### about one dict value transfrom to key, and key as same - Coding Problem 4.5.6
'''
create a separate function to handle transforming movie-performers dictionaries into aperformer-performances dictionary.
'''
###Onther way - more clever
def movies_to_performers(orig_dict, new_dict):
    for performance, performers in orig_dict.items():
        for performer in performers:
            if performer not in new_dict:
                new_dict[performer] = []
            new_dict[performer].append(performance)
            
def stars(movies, tvshows):
    new_dict = {}
    movies_to_performers(movies, new_dict)
    movies_to_performers(tvshows, new_dict)
    
    for performer, performances in new_dict.items():
        performances.sort()
    return new_dict

### My way 
'''
#The function stars should return a new dictionary. The keys
#of the new dictionary should be the performers' names, and
#the values for each key should be the list of shows and
#movies in which that performer has appeared. Sort the shows
#and movies alphabetically.
'''
def stars(movies, tvshows):
    movies.update(tvshows)     
    appearedIn = {}
    for (title, actorList) in movies.items():
        #print(type(title))                          # STR TYPE , OUTPUT:  DICT KEY
        #print(type(actorList))                      # LIST TYPE , OUTPUT: DICT VAULES 
        for actorName in actorList:
            if actorName in appearedIn and title not in appearedIn[actorName]:
                appearedIn[actorName].append(title)
            else:
                appearedIn[actorName] = [title]
                #print(type(appearedIn[actorName]))   # LIST TYPE , OUTPUT: DICT VAULES 
        '''
        ### Other way - fisrt if-not ,then else
        for actorName in actorList:
            if actorName not in appearedIn:
                appearedIn[actorName] = [title]
            else:
                appearedIn[actorName].append(title)
        '''
    for (myk, myv) in appearedIn.items():
        myv.sort()
    return(appearedIn)
        
movies = {"How to Be Single": ["Alison Brie", "Dakota Johnson",
                               "Rebel Wilson"],
          "The Lego Movie": ["Will Arnett", "Elizabeth Banks",
                             "Alison Brie", "Will Ferrell"]}
tvshows = {"Community": ["Alison Brie", "Joel McHale",
                         "Danny Pudi", "Yvette Brown",
                         "Donald Glover"],
           "30 Rock": ["Tina Fey", "Tracy Morgan", "Jack McBrayer",
                       "Alec Baldwin", "Elizabeth Banks"],
           "Arrested Development": ["Jason Bateman", "Will Arnett",
                                    "Portia de Rossi"]}
print(stars(movies, tvshows))



#Copy your Burrito class from the last exercise. Below,
#We've given you three additional classes named "Meat",  
#"Rice" and "Beans." We've gone ahead and built getters
#and setters in these classes to check if the incoming
#values are valid, so you'll be able to remove those
#from your original code.
#
#First, edit the constructor of your Burrito class.
#Instead of calling setters to set the values of the
#attributes self.meat, self.rice, and self.beans, it
#should instead create new instances of Meat, Rice, and
#Beans. The arguments to these new instances should be
#the same as the arguments you were sending to the
#setters previously (e.g. self.rice = Rice("brown")
#instead of set_rice("brown")).
#
#Second, modify your getters and setters from your
#original code so that they still return the same value
#as before. get_rice(), for example, should still
#return "brown" for brown rice, False for no rice, etc.
#instead of returning the instance of Rice.
#
#Third, make sure that your get_cost function still
#works when you're done changing your code.
#
#Hint: When you're done, creating a new instance of
#Burrito with Burrito("pork", True, "brown", "pinto")
#should still work to create a new Burrito. The only
#thing changing is the internal reasoning of the
#Burrito class.
#
#Hint 2: Notice that the classes Meat, Beans, and Rice
#already contain the code to validate whether input is
#valid. So, your setters in the Burrito class no
#longer need to worry about that -- they can just pass
#their input to the set_value() methods for those
#classes.
#
#Hint 3: This exercise requires very little actual
#coding: you'll only write nine lines of new code, and
#those nine lines all replace existing lines of code
#in the constructor, getters, and setters of Burrito.
#
#You should not need to modify the code below.

class Meat:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["chicken", "pork", "steak", "tofu"]:
            self.value = value
        else:
            self.value = False

class Rice:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["brown", "white"]:
            self.value = value
        else:
            self.value = False
            
class Beans:
    def __init__(self, value=False):
        self.set_value(value)
            
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        if value in ["black", "pinto"]:
            self.value = value
        else:
            self.value = False
            

#Write your code here!
class Burrito:
    def __init__(self, meat, to_go, rice, beans, extra_meat=False, guacamole=False, cheese=False, pico=False, corn=False):
        self.meat = Meat(meat)
        self.to_go = self.set_to_go(to_go)
        self.rice = Rice(rice)
        self.beans = Beans(beans)
        self.extra_meat = self.set_extra_meat(extra_meat)
        self.guacamole = self.set_guacamole(guacamole)
        self.cheese = self.set_cheese(cheese)
        self.pico = self.set_pico(pico)
        self.corn = self.set_corn(corn)
    
    def get_cost(self):
        base_cost = 5
        if self.meat.value == "steak":
                base_cost += 1.5
        elif self.meat.value == "chicken" or self.meat.value == "pork" or self.meat.value == "tofu":
                base_cost += 1
        else:
            pass
        if self.extra_meat == True and self.meat.value is not False:
            base_cost += 1
        if self.guacamole == True:
            base_cost += 0.75
        return(base_cost)

    def get_meat(self):
        return(self.meat.get_value())   
    def get_to_go(self):
        return(self.to_go)
    def get_rice(self):
        return(self.rice.get_value())
    def get_beans(self):
        return(self.beans.get_value())
    def get_extra_meat(self):
        return(self.extra_meat)
    def get_guacamole(self):
        return(self.guacamole)
    def get_cheese(self):
        return(self.cheese)
    def get_pico(self):
        return(self.pico)
    def get_corn(self):
        return(self.corn)

    def set_meat(self, newMeat):
        self.meat = Meat(newMeat)
    def set_to_go(self, newTogo):
        if newTogo:
            return(newTogo)
        else:
            self.to_go = False
            return(self.to_go)
    def set_rice(self, newRice):
        self.rice = Rice(newRice)
    def set_beans(self, newBeans):
        self.beans = Beans(newBeans)
    def set_extra_meat(self, newExtra_meat):
        if newExtra_meat:
            return(newExtra_meat)
        else:
            self.extra_meat = False
            return(self.extra_meat)
    def set_guacamole(self, newGuacamole):
        if newGuacamole:
            return(newGuacamole)
        else:
            self.guacamole = False
            return(self.guacamole)
    def set_cheese(self, newCheese):
        if newCheese:
            return(newCheese)
        else:
            self.cheese = False
            return(self.cheese)
    def set_pico(self, newPico):
        if newPico:
            return(newPico)
        else:
            self.pico = False
            return(self.pico)
    def set_corn(self, newCorn):
        if newCorn:
            return(newCorn)
        else:
            self.corn = False
            return(self.corn)

#You may add code below to test your program;
#it will not be used for grading.
newBurrito = Burrito("tofu", True, "white", "pinto")
#newBurrito = Burrito(False, True, "brown", "black",extra_meat=True, guacamole=True)
#print(newBurrito.get_cost())
#print(newBurrito.set_to_go(False))
#print(newBurrito.meat.get_value())
#print(newBurrito.meat.value)
#print(newBurrito.rice.value)
#print(newBurrito.beans.value)
#print(newBurrito.set_meat("chicken"))
#print(newBurrito.get_meat())
print(newBurrito.set_rice("white"))
print(newBurrito.get_rice())


#Copy both your code and ours from the previous exercise.
#You should copy your Burrito class and our Meat, Rice, and
#Beans classes into this exercise.
#
#In this exercise, you won't edit any of your code from the
#Burrito class. Instead, you're just going to write a
#function to use instances of the Burrito class.
#
#Write a function called total_cost. total_cost should take
#as input a list of instances of Burrito, and return the
#total cost of all those burritos together as a float.
#
#Hint: Don't reinvent the wheel. Use the work that you've
#already done. The function can be written in only five
#lines, including the function declaration.
#
#Hint 2: The exercise here is to write a function, not a
#method. That means this function should *not* be part of
#the Burrito class.
def total_cost(inList):
    sum = 0
    for plot in inList:
        sum += plot.get_cost()
    return(sum)
newBurrito1 = Burrito("pork", True, "brown", "pinto")
newBurrito2 = Burrito("pork", True, "brown", "black")
newBurrito3 = Burrito("pork", True, "brown", "red")
print(total_cost([newBurrito1, newBurrito2, newBurrito3]))


