"""
This is a webscrape of a video podcast I watch.
The website has been removed for the sake of the website,
but has been uploaded to a private repo for posterity's sake.
The way this works is that it downloads segmented sections of the video,
which can then be converted to a full video in a third party software.
A goal is to be able to convert these parts into full videos within this
script but I accomplished my initial goal with this.
"""

import urllib
import logging
import time
import re
import requests

download_url = 'REDACTED'
#logging.basicConfig(level=logging.DEBUG)

for i in range(0, 400):

    print (i)
    if i < 10:
        i = '00' + str(i)
    elif i < 100: 
        i = '0' + str(i)
    else: 
        i = str(i)
    print(download_url + i + '.ts')
    response = requests.get(download_url + i + '.ts')
    print (response)
    
    with open('./Podcasts/' + i + '.ts', 'wb') as f:
        for block in response.iter_content(1024):
            f.write(block)
