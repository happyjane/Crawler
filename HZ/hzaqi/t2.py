#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
from selenium import webdriver 
from ClientForm import ParseResponse
import codecs
import re
import csv
import requests
#from scrapy.http import Request
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
start_url='http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?wrlx=1&xzqy=330100&x=41&y=11&sjlx=day12&kssj=2012-1-1%2C00'
urlperfix='http://218.108.6.116:8080/zxjc/datashow_page?'
filename='/home/sunying/hello-jane/weathercrawler/hzaqi/hzaqi.csv'
class Geturl(object):

	def __init__(self,url):
		self.url=url
		#self.url2=url2

	def getHtml(self,url):
		self.page = urllib2.urlopen(self.url)
		#self.page = urllib2.urlopen(self.url2)
		self.html = self.page.read()
		self.soup=BeautifulSoup(self.html)
		self.page.close()
		return self.soup
	def getTag(self,soup):
		self.csoup=self.soup
		self.csoup=str(self.csoup)
		self.tag = BeautifulSoup(self.csoup).find_all("tbody")
		#self.=self.soup.find_all("table")
		#self.csoup=str(self.soup)
		return self.tag
	def compile(self,tag):
		#self.res=re.compile(r'<tr><td class=\S+>(\S+)</td>'+r'<td class=\S+ >(\S+)</td>'+r'<td class=\S+>(\S+)</td>'*3+r'</tr>'
		#self.res=re.compile(r'<tr>'+r'<td class=\S+>(\S+)</td>'*5+r'</tr>')#<td class=\S+ >(\S+)</td>')
		#self.res=re.compile(r"""((<td class=\S+>(\S+)</td>)*6|<td class=\S+>\S+</td><td class=\S+ title=\S+</td><td class=\S+ colspan=\S+>)""", re.VERBOSE)#<td class=\S+ >(\S+)</td>|<td class=\S+>(\S+)</td>
		#self.res=re.compile(r'<td class=\S+>(\S+)</td>'*6)
		#self.res=re.compile(r'<td class=\S+>(\S+)</td><td class=\S+ title=\S+>(\S+)</td><td class=\S+ colspan=\S+>(-)</td>')
		self.res=re.compile(r'<td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td>' or r'<td class=\S+>(\S+)</td><td class=\S+ title=\S+>(\S+)</td><td class=\S+ colspan=\S+>(-)</td>')
		#self.res=re.compile(r'<td class=\S+>(\S+)</td><<td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td>td class=\S+>(\S+)</td><td class<td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td>=\S+>(\S+)</td>)'|#<td class=\S+>(\S+)</td><td class=\S+ title=\S+</td><td class=\S+ colspan=\S+>(-)</td>')#<td class=\S+ >(\S+)</td>|<td class=\S+>(\S+)</td>
		self.result=self.res.findall(str(self.tag))
		return self.result

class Ouput(object):
	def __init__(self,filename):
		self.filename=filename

	def output1(self,filename):
		f=csv.writer(file(filename, 'ab'))
		f.writerow(result)

	def write2(self,filename):
  		with open(filename,'a') as csvfile:
  			spamwriter = csv.writer(csvfile, dialect='excel')
  			spamwriter.writerow(str(result[i]))
class Nextu(object):

	def __init__(self,urlperfix,p):
		
		self.p = p
		self.urlperfix=urlperfix

	def geturl(self,urlperfix,p):
		self.url ='%sdestiny_page=%s'%(self.urlperfix,self.p)
		return self.url

getpage=Geturl(start_url)
print getpage.getTag(getpage.getHtml(start_url))
result=getpage.compile(getpage.getTag(getpage.getHtml(start_url)))
print result
#with open('/home/sunying/hello-jane/weathercrawler/sucess/hzaqi.csv', 'a') as csvfile:
	#spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#f=open('/home/sunying/hello-jane/weathercrawler/sucess/hzaqi.txt', 'a')
#i=0
#while i < len(result): 
#	print result[i]
#	f.write(str(result[i]))
#	f.write('\n')
#	f.close
	#spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL, dialect='excel')
	#spamwriter.writerow(result[i])
#	i+=1
#output=Ouput(filename)  
#i=0
#while i<len(result):
#	output.write2(filename)
#	i+=1
p=2
while p<=5:
	urlperfix='http://218.108.6.116:8080/zxjc/datashow_page?'
	nexturl=Nextu(urlperfix,p)
	newurl=nexturl.geturl(urlperfix,p)
	print newurl
	getpage=Geturl(newurl)
	print getpage.getTag(getpage.getHtml(newurl))
	result=getpage.compile(getpage.getTag(getpage.getHtml(newurl)))
	print result
	p+=1

#while p<=5:
#	newurl=Nextu.geturl(urlperfix,p)
#	print newurl
#	result=getpage.compile(getpage.getTag(getpage.getHtml(newurl)))
#	print result
#	p+=1

		
