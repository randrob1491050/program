#!python3


'''
find the length of the longest substring that consists of the same letter.
https://py.checkio.org/mission/long-repeat/
https://stackoverflow.com/questions/31084639/finding-the-length-of-longest-repeating
'''
### Another Smart Ways
from itertools import groupby
def long_repeat(line):
    return max((sum(1 for pos in g) for k, g in groupby(line)), default=0)
    '''
    sum(1 for pos in g) #sum() 通常是iterable的对象值累加，这里是个小trick，就是对iterable的对象个数累加
    '''
### some kind of complicated, My Ways
def long_repeat(text):
    counter = 0
    text_l = text.lower()
    max_counter = 0                                   # add
    if len(text) == 0:
        return(0)
    for i in range(len(text_l) - 1):
        #print(text_l[i], text_l[i+1])
        if text_l[i] == text_l[i+1]:
            counter += 1
        else:                                         # add
            max_counter = max(max_counter, counter+1) # add
            counter = 0                               # add
    return max(max_counter, counter+1)                # update
### Very Clever Way, Using BOOLE and While-loop, Then Counting 
def long_repeat(line):
    repetitions = 0
    while any(line):
        line = [ line[i] and line[i] == line[i+1] for i in range(len(line)-1) ]
        repetitions += 1
    return repetitions
print(long_repeat(""))
print(long_repeat("abaab"))
print(long_repeat('sdsffffse'))
print(long_repeat('ddvvrwwwrggg'))



'''
Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
https://py.checkio.org/mission/min-max/
'''
### Other Ways
def min(*args, **kwargs):
    l = list(args)
    if len(l) == 1:
        l = list(*args)
    return sorted(l, **kwargs)[0]
def max(*args, **kwargs):
    l = list(args)
    if len(l) == 1:
        l = list(*args)
    kwargs.update({'reverse': True})    # 对可变keyword参数，更新其的 key:value。
    return sorted(l, **kwargs)[0]
### My Ways
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:          # 这里主要是用于单个参数只有字符串的情况，如果单个参数是数字的话，则会报错无法iter
        args = iter(args[0])    # 迭代字符串对象
    return sorted(args, key=key, reverse=reverse)[0]
def min(*args, key=None):
    return get_first_from_sorted(args, key, False)
def max(*args, key=None):
    return get_first_from_sorted(args, key, True)
print(max(3, 2))
print(min(3, 2))
print(max([1, 2, 0, 3, 4]))
print(min("hello"))
print(max(2.2, 5.6, 5.9, key=int))
print(min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]))



'''
https://py.checkio.org/mission/pawn-brotherhood/
'''
### Clear Way
def safe_pawns(pawns):
    safePawns = 0
    for col, row in pawns:
        defenseRow = str(int(row)-1)                   # 首先得出前面row数
        defenseLeft = chr(ord(col)-1) + defenseRow     # 其次得出当前col数，然后与前面row数合平为左右两个位置。
        defenseRight = chr(ord(col)+1) + defenseRow
        if defenseLeft in pawns or defenseRight in pawns:    # 只要前面row的左右col有pawns，即为Safe
            safePawns += 1                             # 最后符合条件的就计数，比下面的方式更简单明了
    return safePawns
### Complicated Way
def safe_pawns(pawns):
    pawns_indexes = set()
    for p in pawns:
        row = int(p[1]) - 1         # 这里减去1，是代表以前面row数，开始检查是否Safe的基准。因为按照需求，判断前面row中是否有pawnsdraw即为Safe
        col = ord(p[0]) - 97        # 这里减去97，是代表A为第一个col，既为0
        pawns_indexes.add((row, col))       # 转换成了一个 (0-7)x(0-7) 的坐标位置
    #print(pawns_indexes)
    count = 0
    for row, col in pawns_indexes:
        is_safe = ((row - 1, col - 1) in pawns_indexes) or ((row - 1, col + 1) in pawns_indexes)
        if is_safe:
            count += 1
    return(count)
print(safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}))
print(safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}))
print(safe_pawns(["a1","a2","a3","a4","h1","h2","h3","h4"]))
print(safe_pawns(["b4","c4","d4","e4","f4","g4","e3"]))



'''
The player who succeeds in placing three respective marks in a horizontal, vertical, or diagonal rows (NW-SE and NE-SW) wins the game.
you must determine if the game ends in a win or a draw as well as who will be the winner. 
Make sure to return "X" if the X-player wins and "O" if the O-player wins. If the game is a draw, return "D".
https://py.checkio.org/mission/x-o-referee/
'''
### Clever Way
def checkio(game_result):
    sample = "".join(game_result)
    data = game_result + [sample[i:9:3] for i in range(3)] + [sample[0:9:4], sample[2:8:2]]
    if "OOO" in data:
        return "O"
    elif "XXX" in data:
        return "X"
    else:
        return "D"
### My Way
def checkio(game_result):
    for num in range(0, 3):
        if game_result[num] == "XXX":
            return("X")
        elif game_result[num] == "OOO":
            return("O")
        if game_result[0][num] == game_result[1][num] == game_result[2][num] == "X":
            return("X")
        elif game_result[0][num] == game_result[1][num] == game_result[2][num] == "O":
            return("O")
        if game_result[0][0] == game_result[1][1] == game_result[2][2] == "X":
            return("X")
        elif game_result[0][0] == game_result[1][1] == game_result[2][2] == "O":
            return("O")
        if game_result[0][2] == game_result[1][1] == game_result[2][0] == "X":
            return("X")
        elif game_result[0][2] == game_result[1][1] == game_result[2][0] == "O":
            return("O")
    return("D")
print(checkio([
        "X.O",
        ".O.",
        "OOX"]))
print(checkio([
    "X.O",
    "XX.",
    "XOO"]))
print(checkio([
    "OO.",
    "XOX",
    "XOX"]))
print(checkio([
    "OOX",
    "XXO",
    "OXX"]))



'''
You should count how many words are included in the given text. A word should be whole and may be a part of other word. 
Text letter case does not matter. Words are given in lowercase and don't repeat. 
If a word appears several times in the text, it should be counted only once.
https://py.checkio.org/mission/monkey-typing/
'''
## Lambda Way
count_words = lambda t, w: sum([x in t.lower() for x in w])
## Same Way
def count_words(text, words):
    return sum(w in text.lower() for w in words)
### My Way
def count_words(inString, inWords):
    #string_list = inString.lower().split(" ")  ## 一开始想得太复杂了，可以不用转成list，再for-loop去进行判断，直接使用 in string 判断即可
    count = 0
    for word in inWords:
        if word in inString.lower():
            count += 1
    return(count)
print(count_words("How aresjfhdskfhskd you?", {"how", "are", "you", "hello"}))
print(count_words("Bananas, give me bananas!!!", {"banana", "bananas"}))
print(count_words("Lorem ipsum dolor sit amet, consectetuer adipiscing elit.",{"sum", "hamlet", "infinity", "anything"}))



'''
The password will be considered strong enough if its length is greater than or equal to 10 symbols, 
it has at least one digit, as well as containing one uppercase letter and one lowercase letter in it. 
The password contains only ASCII latin letters or digits.
https://py.checkio.org/mission/house-password/
'''
# The Way of Using Lambda
checkio = lambda s: not(
        len(s) < 10
        or s.isdigit()
        or s.isalpha()
        or s.islower()
        or s.isupper()
    ) 
# The Way of Using Try-Except-Else
def checkio(data):
    try:
        data[9]
    except IndexError:
        return False
    return not (data.isdigit() or data.isalpha() or data.islower() or data.isupper())
### Another Smart Way
def checkio(data):
    return all((not data.isdigit(), not len(data) < 10, not data.isupper(),
                not data.islower(), not data.isalpha()))
### The Way of Using Regular expression
import re
DIGIT_RE = re.compile('\d')
UPPER_CASE_RE = re.compile('[A-Z]')
LOWER_CASE_RE = re.compile('[a-z]')
def checkio(data):
    if len(data) < 10:
        return False
    if not DIGIT_RE.search(data):
        return False
    if not UPPER_CASE_RE.search(data):
        return False
    if not LOWER_CASE_RE.search(data):
        return False
    return True
'''
def isPasswordSecure(passwd):
    passwordSecure = True
    if len(passwd)<10:
        passwordSecure = False
    if not re.search(r'\d+', passwd):
        passwordSecure = False
    if not re.search(r'[a-z]+',passwd):
        passwordSecure = False
    if not re.search(r'[A-Z]+',passwd):
        passwordSecure = False
    return passwordSecure
'''
### My Way
import string
def checkio(data):
    lower = False
    upper = False
    digit = False
    if len(data) >= 10:
        for l in data:
            if l in string.ascii_lowercase:
                lower = True
            if l in string.ascii_uppercase:
                upper = True
            if l in string.digits:
                digit = True
        if lower == True and upper == True and digit == True:
            return(True)
        else:
            return(False)
    return(False)
print(checkio('A1213pokl'))
print(checkio('bAse730onE'))
print(checkio('asasasasasasasaas'))
print(checkio('QWERTYqwerty'))
print(checkio('123456123456'))
print(checkio('QwErTy911poqqqq'))



'''
return a list consisting of only the non-unique elements in this list. 
To do so you will need to remove all unique elements (elements which are contained in a given list only once). 
When solving this task, do not change the order of the list.
https://py.checkio.org/mission/non-unique-elements/
'''
### Clever Way
# 首先是lambda函数，d为parameters值(传入list)，对list进行for循环，并以list.count(x)判断条件，return 一个新的list
checkio = lambda d:[x for x in d if d.count(x)>1]
### My Way
def checkio(inList):
    newList = inList[:]
    for n in range(len(inList)):
        if inList.count(inList[n]) == 1:
            newList.remove(inList[n])
    return(newList)
print(checkio([1, 2, 3, 1, 3]))
print(checkio([1, 2, 3, 4, 5]))
print(checkio([5, 5, 5, 5, 5]))
print(checkio([10, 9, 10, 10, 9, 8]))



'''
You should find the most frequent letter in the text. The letter returned must be in lower case.
Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
If you have two or more letters with the same frequency, then return the letter which comes first in the latin alphabet.
https://py.checkio.org/mission/most-wanted-letter/
'''
import string
def checkio(text):
    ### One Way
    '''
    return min([(-1 * text.count(ch), ch) for ch in string.ascii_lowercase])[1]
    '''
    ### Another Way
    '''
    text = text.lower()
    return max(string.ascii_lowercase, key=text.count)
    '''
    ### My Way
    text = text.lower()
    inList = []
    '''
    ## Step1: 循环小写字母列表，与字符串出现过的字母匹配并计数，然后生成一个新列表
    for ch in string.ascii_lowercase:
        inList.append((-1 * text.count(ch), ch))
    ## Step2: 对新列表进行排序，排序规则为一个lambda函数(作用是：return inList[0])
    sortedList = sorted(inList, key=lambda x: x[0])
    ## Step3: 取出最多次的字母
    return(sortedList[0][1])
    '''
#These "asserts" using only for self-checking and not necessary for auto-testing
tests = [
    "Hello World!",
    "How do you do?",
    "One",
    "Oops!",
    "AAaooo!!!!",
    "abe",
]
for t in tests:
    ans = checkio(t)
    print('{{"input": "{0}", "answer": "{1}"}},'.format(t, ans))