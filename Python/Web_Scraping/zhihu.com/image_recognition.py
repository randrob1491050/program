#!python3

""" this scripts for recognize verify code from images  """
__author__ = 'iBSD@siteop.me'

import pytesseract
from PIL import Image, ImageEnhance, ImageFilter

try:
    IMGS = Image.open("captcha.gif")
    IMGS = IMGS.convert('RGB')
    #print(IMGS.format, IMGS.size, IMGS.mode)
    IMGS = IMGS.filter(ImageFilter.SHARPEN)
    ENHANCER = ImageEnhance.Sharpness(IMGS)
    IMGS = ENHANCER.enhance(2)
    #IMGS = IMGS.convert('1')
    IMGS.show()
    IMGS.save('tmp.jpg')
    TEXT = pytesseract.image_to_string(Image.open('tmp.jpg'))
    print(TEXT)
except IOError:
    print("Unable to open image")


#  IMGS = IMGS.filter(ImageFilter.MedianFilter())
