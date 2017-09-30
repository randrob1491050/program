#!python3

# Import the regex module with import re.
import re


def validPhoneNumber(filename):
    '''Create a Regex object with the re.compile() function, Use a RAW string.'''
    #phoneNumRegex = re.compile(r'\d{3}-\d{3}-\d{4}')
    '''by putting an r before the first quote of the string value, you can mark the string as a raw string, which does not escape characters.
    And Adding parentheses will create groups in the regex.
    '''
    phoneNumRegex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
    newPhoneNumArea = []
    with open(filename, "r") as f:
        for read_data in f.readlines():
            # print(read_data.strip())
            '''Pass the string you want to search into the Regex object’s search() method. This returns a Match object.'''
            mo = phoneNumRegex.search(read_data.strip())
            if mo != None:
                '''Call the Match object’s group() method to return a string of the actual matched text.'''
                newPhoneNumArea.append(mo.group(1))
                '''retrieve all the groups at once, use the groups() method'''
                #areaCode, mainNumber = mo.groups()
            # else:
            #    return("Cannot found any Phone number")
    f.close
    return("Phone number have area code: ", newPhoneNumArea)


print(validPhoneNumber("input.txt"))
