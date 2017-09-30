#!python3
# DATE:   2017.03.08

"""this scripts for transform origianl file to new with re feature"""
__author__ = 'iBSD@siteop.me'

import re

# TEST FILE_PATH
# FILE_PATH = 'D:\\Dropbox\\Project\\Python\\GET_CN_ROUTE\\unit_test\\words.txt'
# Windows
# FILE_PATH = 'D:\\Dropbox\\Project\\Python\\GET_CN_ROUTE\\apnic-latest'
# OSX
FILE_PATH = '/Users/ibsd/Dropbox/Project/Python/GET_CN_ROUTE/apnic-latest'

APNIC_DATA = open(FILE_PATH, mode='r')
#print(APNIC_DATA.readlines())
#for item in APNIC_DATA.readlines():
#    print(type(item))

def get_cn_asn():
    """ this def for pick cn_address up from apnic-latest"""
    asn_regex = re.compile("CN\\|ipv4.*")
    for apnic_items in list(APNIC_DATA):
    #for apnic_items in APNIC_DATA.readlines():
        result = asn_regex.search(apnic_items)
        if result:
            #print(result.group(0))
            cn_address = result.group(0).split('|')[2]
            print(cn_address)
		#	cnasn_file.write("%s\n" % result.group(0))

get_cn_asn()

APNIC_DATA.close()
