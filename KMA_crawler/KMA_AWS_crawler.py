# -*- coding: utf-8 -*-
"""
@author: guitar79@naver.com, yyyyy@snu.ac.kr
view-source:http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?201008262022&0&MINDB_01M&0&a
"""
from urllib.request import urlopen
from urllib2 import urlopen
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import time
from datetime import date

for year in range(2016,2017):
	for Mo in range(1,2):
		for Da in range(1,2):
			for Ho in range(0,2):
				for Mn in range(0,2): # looks like the interval is 5min. often omitted.
					url = "http://www.kma.go.kr/cgi-bin/aws/nph-aws_txt_min?%d%02d%02d%02d%02d&0&MINDB_01M&0&a" 	% (year, Mo, Da, Ho, Mn)
					bsObj = BeautifulSoup(url, "html.parser")
					print = (bsObj)              