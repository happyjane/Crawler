#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
from selenium import webdriver 
import codecs
import re
import csv
import sys 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webelement
import time
import threading as thread 
reload(sys)
sys.setdefaultencoding('utf-8')
filename='/home/sunying/crawler/greatfire/url_greatfire.txt'
class Geturl(object):

	def __init__(self,url):
		self.url=url
	def getHtml(self,driver):
		self.driver = webdriver.Chrome()
		self.driver.get(self.url)
		self.soup=self.driver
		return self.soup
	def getcontent(self,soup):
		#self.tag= self.soup.find_elements_by_tag_name('h1')
		self.url=self.soup.find_elements_by_xpath("//td[@class='first']")
		#self.data=self.tag.find_elements_by_xpath("//li[@class='wl228']")[3]
		return self.url
	# def inputdata(self,soup,name):
	# 	self.soup.find_element_by_id('ad1').send_keys('2011.01.01')
	# 	self.soup.find_element_by_id('ad2').send_keys('2011.09.28')
	# 	self.soup.find_element_by_id('pa').send_keys(unicode('上海交通大学'))
	# 	self.soup.find_element_by_id('inn').send_keys(unicode(self.name))
	def getwhole(self,soup):
		self.whole=self.soup.find_element_by_tag_name('tbody')
		return self.whole
	def getcontricted(self,soup):
		self.contricted =self.soup.find_elements_by_xpath("//td[@style='background-size: %d%;'"%(100))#class='blocked']" or "//td[@class='restricted']")
		return self.contricted
	def getnextpage(self,soup):
		self.soup.find_element_by_link_text('下一页 ›').click()
	def judge(self,soup):
		#selem=self.soup.find_element_by_xpath("//a[@href='javascript:zl_fy(2);']")
		if self.soup.find_element_by_xpath("//td[@class='restricted']"):
			judge=0
		else :
			judge=1
		return judge 
	def judge2(self,soup):
		if self.soup.find_element_by_link_text('下一页 ›'):
			judge=1
		else:
			judge=0
		return judge
	def quit(self,driver):
		self.driver.quit()
class Output(object):
	def __init__(self,filename):
		self.filename=filename

	def write(self,filename,page):
  		with open(filename,'a') as csvfile:
  			spamwriter = csv.writer(csvfile, dialect='excel')
  			spamwriter.writerow(page)
  	def writetxt(self,filename,page):
  		f=open(filename,'a')
  		f.write(page)
  		f.close
  	def writetitle(self,filename):
  		f=open(filename,'a')
  		return f
  
url='https://zh.greatfire.org/search/alexa-top-1000-domains'


getpage=Geturl(url)
output=Output(filename)
web=getpage.getHtml(url)
whole=getpage.getwhole(web)
print whole.text
output.writetxt(filename,whole.text)
output.writetxt(filename,'\r\n')
# content=getpage.getcontent(web)
# contricted=getpage.getcontricted(web)
# # judge = getpage.judge(web)
# print content[0].text
# output.writetxt(filename,str(content[0].text))
# output.writetxt(filename,'\r\n')

# i = 0
# while i<len(content) :
# 	output.writetxt(filename,content[i].text+'\t')
# 	output.writetxt(filename,contricted[i].text)
# 	output.writetxt(filename,'\r\n')
# 	# else:pass
# 	i+=1
judge2 = getpage.judge2(web)	
while judge2:
	getpage.getnextpage(web)
	whole=getpage.getwhole(web)
	output.writetxt(filename,whole.text)
	output.writetxt(filename,'\r\n')
	# content=getpage.getcontent(web)
	# contricted=getpage.getcontricted(web)
	# # judge = getpage.judge(web)
	# print len(content)
	# print len(contricted)
	# i = 0
	# while i<len(content) :
	# 	output.writetxt(filename,content[i].text+'\t')
	# 	output.writetxt(filename,contricted[i].text)		
	# 	output.writetxt(filename,'\r\n')
	# 	# else:pass
	# 	i+=1
	judge2 = getpage.judge2(web)	
output.writetxt.close



# 	getpage.getnextpage(contentweb)
# i=0
# while i<len(namelist):
# 	name=namelist[i]
# 	print name
# 	judge=1
# 	while  judge:
# 		getpage=Geturl(url,name)
# 		output=Output(filename)
# 		output.writetxt(filename,name)
# 		output.writetxt(filename,'\r\n')
# 		web=getpage.getHtml(url)
# 		contentweb=getpage.inputdata(web,name)
# 		getpage.getnextpage(contentweb)
# 		tag=web.find_elements_by_tag_name('h1')
# 		#zhuanliname=web.find_element_by_xpath("html/body/div.main/div.w790.right/div.cp_box/div.cp_linr")
# 		data=web.find_elements_by_xpath("//li[@class='wl228']")
# 		qianru=web.find_element_by_xpath("//div[@style]")
# 		j=0
# 		while j<len(tag):
# 			#print len(tag)
# 			zhuanliname=tag[j].text
# 			number=data[j*6+2].text
# 			time=data[j*6+3].text
# 			#print zhuanliname,number,time
# 			output.writetxt(filename,tag[j].text)
# 			output.writetxt(filename,data[j*6+0].text)
# 			output.writetxt(filename,data[j*6+1].text)
# 			output.writetxt(filename,data[j*6+2].text)
# 			output.writetxt(filename,data[j*6+3].text)
# 			output.writetxt(filename,data[j*6+4].text)
# 			output.writetxt(filename,data[j*6+5].text)
# 			output.writetxt(filename,qianru.text)
# 			output.writetxt(filename,'\r\n')
# 			#print web.find_elements_by_xpath("//a[@href='javascript:zl_fy(2);']")[1].text
# 			j+=1	
# 		judge=0

# 	i+=1


# 	