# -*- coding: utf-8 -*-
"""
Created on Tue Dec 27 11:18:38 2016

@author: Duggal
"""

import urllib.request
from bs4 import BeautifulSoup
import os

#urlImg = urllib.request.urlretrieve("http://www.ommzi.com/images/logo_text.png", "asd.jpg")

def Parsing(soup, urlName, folderName):
    for ImagesURL in soup.find_all('img'):
        try:
            parse = ImagesURL.get('src')
            if parse[0] == '/':      
                ImgName = urlName + parse 
                FileName = ImgName.rsplit('/')[-1]
            else:
                ImgName = urlName + '/' + parse 
                FileName = ImgName.rsplit('/')[-1]
            print(ImgName)
            
            try:     
                urlImg = urllib.request.urlretrieve(ImgName, folderName + "/" + FileName)
            except:
                urlImg = urllib.request.urlretrieve(parse, folderName + "/" + FileName)
        except Exception as e:
            print("------------ " + str(e) + "----------------")
            pass

try:
    url      = 'http://getbootstrap.com/'
#    url      = 'https://thenewboston.com/'
    headers  = {} 
    headers['User-Agent'] = "Mozilla/5.0"
    content      = urllib.request.Request(url, headers=headers)
    resp     = urllib.request.urlopen(content)
#    print(resp.read())
#    urlImg = urllib.request.urlretrieve("http://www.ommzi.com/images/logo_text.png", "asd.jpg")

except Exception as e:
    print("++++++++++++++++ " + str(e) + "+++++++++++++++")
    
soup    = BeautifulSoup(resp.read(), 'lxml')
urlName = url.rsplit('/', 1)[0]
folderName = urlName.rsplit('//',)[-1]
print(urlName)
print(folderName)


if os.path.exists(folderName):    
    Parsing(soup, urlName, folderName)
else:
    os.mkdir(folderName)
    print("Creating Directory : " + folderName)
    Parsing(soup, urlName, folderName)