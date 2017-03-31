# -*- coding: utf-8 -*-
"""
Created on Tue Dec 13 13:45:12 2016

@author: Duggal
"""

from urllib.parse import urlparse


def get_domain_name(url):
    try:
        result = get_sub_domain_name(url).split('.')
        return result[-2] + '.' + result[-1]
    except Exception as e:
#        print("Exception Domain get_domain_name " + str(e))
        return ''

def get_sub_domain_name(url):
    try:
        return urlparse(url).netloc
    except Exception as e:
#        print("Exception Domain get_sub_domain_name " + str(e))
        return ''