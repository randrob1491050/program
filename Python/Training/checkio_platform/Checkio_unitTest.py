#!python3


def checkio(express):
    LEFT = '{[('
    RIGHT = '}])'
    l_brackets = []
    r_brackets = []
    for item in express:
        if item in LEFT:
            l_brackets.append(item)
        elif item in RIGHT:
            r_brackets.append(item)
    print(l_brackets)
    print(r_brackets[::-1])
    print(sorted(r_brackets[::-1]))
    print(list(zip(l_brackets, r_brackets)))
    # for l, r in zip(l_brackets, r_brackets[::-1]):
    #    lc, rc = ord(l), ord(r)
    #    print(lc, rc)
    #    if lc != rc-1 and lc != rc-2:
    #        return False
    # return True


# print(checkio("((5+3)*2+1)"))
# print(checkio("{[(3+1)+2]+}"))
print(checkio("(3+{1-1)}"))
print(checkio("[1+1]+(2*2)-{3/3}"))
# print(checkio("(({[(((1)-2)+3)-3]/3}-3)"))
# print(checkio("2+3"))
