#!python3

""" this scripts for recognize verify code from images  """
__author__ = 'iBSD@siteop.me'

import requests

def ocr_space_file(filename, overlay=False, api_key='bb8400852288957', language='eng'):
    """ OCR.space API request with local file.
        Python3.5 - not tested on 2.7
    :param filename: Your file path & name.
    :param overlay: Is OCR.space overlay required in your response.
                    Defaults to False.
    :param api_key: OCR.space API key.
                    Defaults to 'helloworld'.
    :param language: Language code to be used in OCR.
                    List of available language codes can be found on https://ocr.space/OCRAPI
                    Defaults to 'en'.
    :return: Result in JSON format.
    """

    payload = {'isOverlayRequired': overlay,
               'apikey': api_key,
               'language': language,
               }
    with open(filename, 'rb') as f:
        r = requests.post('https://api.ocr.space/parse/image',
                          files={filename: f},
                          data=payload,
                          )
    #print(r.status_code)
    #print(r.content.decode())
    return r.content.decode()

# Use examples:
text = ocr_space_file(filename='tmp.jpg', language='eng')
print("DISPLAY: %s " % text)
