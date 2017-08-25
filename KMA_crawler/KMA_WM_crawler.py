# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:32:11 2017

@author: User
"""

import requests
from bs4 import BeautifulSoup

# Preparing entry data for bs4
TAGNAME = "a"
ATTR    = "class"
VALUE   = "target-class"
TARGET  = "http://randomblog.com/page/"
TG_ATTR = "href"

def crawler(max_pages):
  page = 1
  while page < max_pages:
    url    = TARGET + str(page) + "/"
    source = requests.get(url).text
    soup   = BeautifulSoup(source, "html.parser")
    
    for link in soup.findAll(TAGNAME, {ATTR: VALUE}):
      href = link.get(TG_ATTR)
      print(href)
      
    page += 1

crawler(5)