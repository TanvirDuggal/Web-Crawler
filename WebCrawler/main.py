# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 14:03:34 2016

@author: Duggal
"""

import threading
from queue import Queue
import domain
from spider import spider
import WebCrawler_1

PROJECT_NAME = 'mindfsck'
HOMEPAGE     = 'http://mindfsck.net/'
DOMAIN_NAME  = domain.get_domain_name(HOMEPAGE)
QUEUE_FILE   =  PROJECT_NAME + '/queue.txt'
CRAWLED_FILE =  PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREAD = 50
queue        = Queue()

spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)  

#---------------------Thread Spiders------------------------
def create_workers():
    for _ in range(8):
        t = threading.Thread(target = work)
        t.daemon = True
        t.start()

def work():
    while True:
        url = queue.get()
        spider.crawl_page(threading.current_thread().name, url)
        queue.task_done()


#------------------Each Queue is new Job---------------------
def create_jobs():
    for links in WebCrawler_1.fileToSet(QUEUE_FILE):
        queue.put(links)
    queue.join()
    crawl()

#----------Check If there are links in queue to proceed-------
def crawl():
    queued_links = WebCrawler_1.fileToSet(QUEUE_FILE)
    if len(queued_links) > 0:
        print(str(len(queued_links)) + " Links Left in Queue")
        create_jobs()
        
create_workers()
crawl()