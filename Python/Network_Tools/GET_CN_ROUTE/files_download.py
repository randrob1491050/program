#!python3
# DATE:   2017.03.08

"""This Scripts for download files from internet"""
__author__ = 'iBSD@siteop.me'

import sys

if sys.version_info[0] >= 3:
    from urllib.request import urlretrieve
else:
    from urllib import urlretrieve

URL_TEST = "https://cdn.51img3.com/32.jpg"
#URL = "ftp://ftp.apnic.net/pub/stats/apnic/delegated-apnic-latest"
if urlretrieve(URL_TEST, filename="32.jpg"):
    print("Download Completed!")
else:
    print("Downlad Failed")
