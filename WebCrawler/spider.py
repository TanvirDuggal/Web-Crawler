# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 19:55:25 2016

@author: Duggal
"""

from urllib.request import urlopen
import link_Finder
import WebCrawler_1
import domain

class spider:
#----------Class Variables Shared Among Spider--------

    project_Name = ''
    base_URL     = ''
    domain_Name  = ''
    queue_File   = ''
    crawled_File = ''
    queue        = set()
    crawled      = set()
    
    def __init__(self, project_Name, base_URL, domain_Name):
        spider.project_Name = project_Name
        spider.base_URL     = base_URL
        spider.domain_Name  = domain_Name
        spider.queue_file   = spider.project_Name + '/queue.txt'
        spider.crawled_file = spider.project_Name + '/crawled.txt'
        self.boot()
        self.crawl_page('First Spider', spider.base_URL)
        
    @staticmethod  
    def boot():
       WebCrawler_1.create_Project_dir(spider.project_Name)
       WebCrawler_1.create_data_files(spider.project_Name, spider.base_URL)
       spider.queue   =  WebCrawler_1.fileToSet(spider.queue_file)
       spider.crawled =  WebCrawler_1.fileToSet(spider.crawled_file)
       
    @staticmethod   
    def crawl_page(thread_name, page_url):
        try:
            if page_url not in spider.crawled:
                print(thread_name + " Now Crawling " + page_url)
                print('Queue ', str(len(spider.queue)), " || ", "Crawled ", str(len(spider.crawled)))
                spider.add_links_to_queue(spider.gatherLinks(page_url))
                spider.queue.remove(page_url)
                spider.crawled.add(page_url)        
                spider.update_file()
        except Exception as e:
            pass
#            print("Exception Crawl Page : " + str(e
                
#Connect to website, gather HTML and convert to reading form and send it to Link Finder
    @staticmethod   
    def gatherLinks(page_url):
        html_string = ''
        try:
            response = urlopen(page_url)
            if 'text/html' in response.getheader('Content-Type'):
                html_bytes  = response.read()
                html_string = html_bytes.decode('utf-8')
                
            finder = link_Finder.LinkFinder(spider.base_URL, page_url)
            finder.feed(html_string)
        except Exception as e:
            print("Error : Cannot Crawl The Page " + str(e))
            return set()
        return finder.page_links()
        
    @staticmethod   
    def add_links_to_queue(links):
        for url in links:
            if (url in spider.queue) or(url in spider.crawled) :
                continue
            if spider.domain_Name != domain.get_domain_name(url):
                continue
            spider.queue.add(url)
    @staticmethod           
    def update_file():
        WebCrawler_1.SetToFile(spider.queue, spider.queue_file)    
        WebCrawler_1.SetToFile(spider.crawled, spider.crawled_file)