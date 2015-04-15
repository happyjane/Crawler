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
import time
reload(sys)
sys.setdefaultencoding('utf-8')
start_url='http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?wrlx=2&xzqy=330100&x=41&y=13&sjlx=day&kssj=2014-04-28%2C10'
#urlperfix='http://218.108.6.116:8080/zxjc/datashow_page?'
filename='/home/sunying/hello-jane/crawler/hzaqi/hzaqiout.txt'
class Geturl(object):

	def __init__(self,url):
		self.url=url
		#self.url2=url2

	def getHtml(self,driver):
		self.driver = webdriver.Firefox()
		self.driver.get(self.url)
		#self.page = urllib2.urlopen(self.url)
		#self.page = urllib2.urlopen(self.url2)
		#self.html = self.driver.read() 
		#self.soup=BeautifulSoup(self.driver)
		#self.page.close()
		# self.driver.find_element_by_xpath("//input[@value='下一页']").click()
		# self.driver.find_element_by_xpath("//input[@value='下一页']").click()
		#self.driver.find_element_by_xpath("//input[@value='下一页']").click()
		#url=self.driver.geturl
		#print url
		self.soup=self.driver
		return self.soup
	def getTag(self,soup):
		#self.csoup=self.soup
		#self.csoup=str(self.csoup)
		#self.tag= self.soup.find_elements_by_xpath("//td[@class='checkBox|checkBoxs']")
		#self.tag= self.soup.find_element_by_tag_name("tbody")
		self.tag= self.soup.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
		#self.tag = BeautifulSoup(self.csoup).find_all("tbody")
		#self.=self.soup.find_all("table")
		#self.csoup=str(self.soup)
		return self.tag
	def judge(self,soup):
		if self.soup.find_element_by_xpath("//input[@disabled='disabled']"):
			judge=0
		else:
			judge=1
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
# attribute=get_attribute(tag_name) 
print tag.text
#output=Output(filename)
output.writetxt(filename,tag.text)

judge=1
while judge:
	#html=getpage.getHtml(start_url)
	getpage.getnextpage(html)
	tag2=html.find_element_by_xpath("/html/body/form/table/tbody/tr/td/div/div/div[2]/table/tbody[2]")
	#driver.switch_to_alert().accept()
	output.writetxt(filename,tag2.text)
	print tag2.text
	#html=getpage.getHtml(start_url)
	#print newdriver
	#newurl=driver.geturl
	#print newurl
	#getpage.judge(html)

# result= getpage.compile(getpage.getTag(getpage.getHtml(start_url)))
# print result.text
# result=getpage.compile(getpage.getTag(getpage.getHtml(start_url)))
# print result
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
# p=2
# while p<=5:
# 	urlperfix='http://218.108.6.116:8080/zxjc/datashow_page?'
# 	nexturl=Nextu(urlperfix,p)
# 	newurl=nexturl.geturl(urlperfix,p)
# 	print newurl
# 	getpage=Geturl(newurl)
# 	print getpage.getTag(getpage.getHtml(newurl))
# 	result=getpage.compile(getpage.getTag(getpage.getHtml(newurl)))
# 	print result
# 	p+=1

#while p<=5:
#	newurl=Nextu.geturl(urlperfix,p)
#	print newurl
#	result=getpage.compile(getpage.getTag(getpage.getHtml(newurl)))
#	print result
#	p+=1

		
