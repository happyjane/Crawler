 #! /usr/bin/env python
# -*- coding: UTF-8 -*-
import html5lib
import urllib2
import argparse
import codecs
from lxml import etree
from BeautifulSoup import BeautifulSoup
from html5lib import treebuilders
from sgmllib import SGMLParser
import re
import csv
from sgmllib import SGMLParser
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='http://www.hzqx.com/'
class Crawler(object):
	def __init__(self,url):
		self.url=url
		print self.url
	def getHtml(self,url):
			self.page = urllib2.urlopen(self.url)
			self.html = self.page.read()
			self.soup=BeautifulSoup(self.html)
			#f=open('/home/sunying/hello-jane/weathercrawler/f.txt','w')
			#f.write(self.html)
			#f.close()
			self.page.close()
			return self.soup
				
crawler= Crawler(url)
csoup=crawler.getHtml(url)
#f=open('/home/sunying/hello-jane/weathercrawler/sucess/soup.html','w')
csoup=str(csoup)
#print csoup
#f.close()
#soup=open('/home/sunying/hello-jane/weathercrawler/sucess/soup.html')
soup = BeautifulSoup(csoup)
#soup= soup.prettify() 
csoup=soup.find_all("div",id="tqyDiv")
csoup=csoup.find_all("div",id="gdDiv")
csoup=csoup.find_all("div",class_="hzDqDivClass")
#,id="gdDiv")
#print soup
res=re.compile(r'<div id=\"dq\d\" onclick=\".+\">([\u4e00-\u9fa5]{2})</div>')
result=res.findall(str(csoup))
print result
#print len(result)
#f=open('/home/sunying/hello-jane/weathercrawler/re.csv','w')
with open('/home/sunying/hello-jane/weathercrawler/hzqx.csv', 'wb') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    i=0
    while i < len(result):
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(result[i])
        i+=1