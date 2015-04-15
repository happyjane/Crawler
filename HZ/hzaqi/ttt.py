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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webelement
import time
reload(sys)
sys.setdefaultencoding('utf-8')
start_url='http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?wrlx=2&xzqy=330100&x=41&y=13&sjlx=day&kssj=2014-04-28%2C00'
filename='/home/sunying/hello-jane/crawler/hzaqi/hzaqiout.txt'
class Geturl(object):

	def __init__(self,url):
		self.url=url

	def getHtml(self,driver):
		self.driver = webdriver.Firefox()
		self.driver.get(self.url)
		self.soup=self.driver
		return self.soup
	def getTag(self,soup):
		self.tag= self.soup.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
		return self.tag
	def compile(self,tag):
		#self.attribute=self.driver.get_attribute(tag_name)
		self.res=re.compile(r'<td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td><td class=\S+>(\S+)</td>' or r'<td class=\S+>(\S+)</td><td class=\S+ title=\S+>(\S+)</td><td class=\S+ colspan=\S+>(-)</td>')
		self.result=self.res.findall(str(self.tag))
		return self.result
	def Judge(self,soup):
		selem=self.soup.find_element_by_xpath("//input[@value='下一页']")
		if not selem.get_attribute("disabled"):
			judge=1
		else  :
			#attribute= selem.get_attribute("disabled")
			judge=0
		return judge 
	def getnextpage(self,soup):
		self.soup.find_element_by_xpath("//input[@value='下一页']").click()
class Output(object):
	def __init__(self,filename):
		self.filename=filename

	def output1(self,filename):
		f=csv.writer(file(filename, 'ab'))
		f.writerow(result)

	def write2(self,filename):
  		with open(filename,'a') as csvfile:
  			spamwriter = csv.writer(csvfile, dialect='excel')
  			spamwriter.writerow(str(result[i]))
  	def writetxt(self,filename,page):
  		f=open(filename,'a')
  		f.write(page)
class Nextu(object):

	def __init__(self,urlperfix,p):
		
		self.p = p
		self.urlperfix=urlperfix

	def geturl(self,urlperfix,p):
		self.url ='%sdestiny_page=%s'%(self.urlperfix,self.p)
		return self.url
getpage=Geturl(start_url)
output=Output(filename)
html=getpage.getHtml(start_url)
tag=getpage.getTag(html) 
print tag.text
result=getpage.compile(tag)
print result
output.writetxt(filename,tag.text)
judge=1
while judge:
	getpage.getnextpage(html)
	tag2=html.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
	output.writetxt(filename,tag2.text)
	print tag2.text
	judge=getpage.Judge(html)
	