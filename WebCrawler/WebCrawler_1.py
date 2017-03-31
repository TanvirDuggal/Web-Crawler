# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 18:38:56 2016

@author: Duggal
"""

import os

#----Each New Crawler is in new Dir--------
def create_Project_dir(directory):
    if not os.path.exists(directory):
        print("Creating Project " + directory)
        os.makedirs(directory)

#-------Create Queue & Crawled Files-------     
def create_data_files(projectName, baseURL):
    queue = os.path.join(projectName , 'queue.txt')
    crawled = os.path.join(projectName,"crawled.txt")
    if not os.path.isfile(queue):
        writeFile(queue, baseURL)
    if not os.path.isfile(crawled):
        writeFile(crawled, '')

#--------------Create New File-------------       
def writeFile(path, data):
    with open(path, 'w') as f:
        f.write(data)
        
#--------------Append New Data-------------
def appendFile(path, data):
    with open(path, 'a') as fa:
        fa.write(data + '\n')
        
#-------------Deleting File Data-----------
def delFileContent(path):
   open(path, 'w').close()
    
#------Read File and convert to Set--------
def fileToSet(file_name):
    result = set()
    with open(file_name, 'rt') as fs:
        for line in fs:
            result.add(line.replace('\n', ' '))
    return result
    
    
#---------Iterate Through File---------------
def SetToFile(links, file):
   with open(file,"w") as f:
        for l in sorted(links):
            f.write(l + "\n")