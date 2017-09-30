#!python3

"""this scripts for testing or debug some code snippet"""
__author__ = 'iBSD@siteop.me'

# print python version
import sys
print(sys.version_info[0])

# print type of strings
S = '''[34343] | ****. "Example": <one>, yellow dog
        tstring0 123
        tstring1 456
        tstring2 789'''
print(type(S))

# file read/write method on windows
# FILE_PATH = 'D:\\Dropbox\\Project\\Python\\GET_CN_ROUTE\\words.txt'
# on osx
FILE_PATH = '/Users/ibsd/Dropbox/Project/Python/GET_CN_ROUTE/unit_test/words.txt'
APNIC_DATA = open(FILE_PATH, mode='r')
print(APNIC_DATA.readlines())
APNIC_DATA.close()
