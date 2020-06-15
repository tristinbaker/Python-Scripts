"""
This is a webscraper I wrote that finds and downloads
every ROM on a certain ROM website. I have redacted the
website for the website's sake, just in case anyone finds this
script and abuses it. For posterity's sake, I have uploaded the 
unedited script to a private repo.
"""

import requests
import urllib
import logging
import time
import re
from google_drive_downloader import GoogleDriveDownloader as gd
from bs4 import BeautifulSoup

download_url = 'REDACTED'
url = 'REDACTED'
#logging.basicConfig(level=logging.DEBUG)

for i in range(3203, 9755):

    print (i)
    response = requests.get(url + str(i))

    soup = BeautifulSoup(response.text, "html.parser")
    try:
        title = soup.find("span", {"style":"text-decoration:underline"}).text
        title = re.sub("[^a-zA-Z0-9]", "", title)
    except AttributeError:
        continue
        
    print("Downloading " + title)

    try:
        mediaId = soup.find("input", {"name":"mediaId"})['value']
    except TypeError: 
        continue

    try:
        t1 = soup.find("input", {"name":"t1"})['value']
    except TypeError:
        continue

    try:
        t2 = soup.find("input", {"name":"t2"})['value']
    except TypeError:
        continue
    
    
        
    try:
        type = soup.find("span", {"class":"sectionTitle"}).text
    except AttributeError:
        continue

    quoted_mediaId = urllib.parse.quote(mediaId)
    quoted_t1 = urllib.parse.quote(t1)
    quoted_t2 = urllib.parse.quote(t2)

    download_url = 'REDACTED' % (quoted_mediaId, quoted_t1, quoted_t2)

    headers = {
        'Host': 'REDACTED',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }  
    response = requests.get(download_url, headers=headers, stream=True)

    time.sleep(1)
    if response.history:
        for resp in response.history:
            print(response.url)
            id = response.url.split('id=')[1]
            gd.download_file_from_google_drive(file_id=id, dest_path='./Games/' + type + '/' + title + '.7z')
    else: 
        with open('./Games/' + type + '/' + title + '.7z', 'wb') as handle: 
            for block in response.iter_content(1024):
                handle.write(block)
