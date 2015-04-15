#! /usr/bin/env python
# -*- coding: utf-8 -*-
import urllib2
import cookielib
from selenium import webdriver 
import codecs
import re
import csv
import sys 
import selenium.webdriver.firefox.firefox_profile 
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote import webelement
import time
import threading as thread 
#import org.openqa.selenium.WebDriver;
#import org.openqa.selenium.firefox.FirefoxDriver;
#import org.openqa.selenium.firefox.Firefoxself.profile;
reload(sys)
sys.setdefaultencoding('utf-8')
url_list='/home/sunying/crawl/tongyong/list_url.txt'
#export_log='/home/sunying/crawl/export_log/'
class Get_url(object):
	"""docstring for Get_url"""
	def __init__(self, url):#,firebug,netexport):
		self.url=url
		self.profile = webdriver.FirefoxProfile();
		self.domain = "extensions.firebug.";
		#self.firebug =open("/home/sunying/crawl/tongyong/xpi/firebug-2.0.2-fx.xpi");
		#self.netexport = open("/home/sunying/crawl/tongyong/xpi/netExport-0.8b10.xpi");
	def open_url(self,domain):
		try:
			self.profile.add_extension(extension="/home/sunying/crawl/tongyong/xpi/firebug-2.0.2-fx.xpi")#firebug)
			self.profile.add_extension(extension="/home/sunying/crawl/tongyong/xpi/netExport-0.8b10.xpi")#netexport)
		except IOError:
			print "error"
		#System.out.println(err);

		# Set default Firefox preferences
		self.profile.set_preference("app.update.enabled", "false");

		# Set default firebug preferences
		self.profile.set_preference(self.domain + "currentVersion", "2.0.2");
		self.profile.set_preference(self.domain + "allPagesActivation", "on");
		self.profile.set_preference(self.domain + "defaultPanelName", "net");
		self.profile.set_preference(self.domain + "net.enableSites", "true");

		# Set default NetExport preferences
		self.profile.set_preference(self.domain + "netexport.alwaysEnableAutoExport", "true");
		self.profile.set_preference(self.domain + "netexport.showPreview", "false" );
		self.profile.set_preference(self.domain + "netexport.defaultLogDir","/home/sunying/crawl/export_log/");
		self.driver = webdriver.Firefox(self.profile);

		#driver = webdriver.Firefox()
		try:

			#  Wait till self.firebug is loaded
			time.sleep(5);

			# Load test page
			self.driver.get(url);
			time.sleep(30);

		except Exception:
			print "error!"
		#driver.get(url)
		#ef get_html(self,driver):
		self.soup=self.driver
		return self.soup 
	def getTag(self,soup):
		self.tag_list= self.soup.find_elements_by_tag_name("a")
		return self.tag_list
	def compile(self,tag):
		self.res=re.compile(r'<a\s+href=.*<\a>')#\"(\S+)\"\S+>\S+<\a>'
		self.result=self.res.findall(str(self.tag))
		return self.result
	'''def Judge(self,soup):
		selem=self.soup.find_element_by_xpath("//input[@value='下一页']")
		if not selem.get_attribute("disabled"):
			judge=1
		else  :
			judge=0
		return judge '''
	def getnextpage(self,tag_list):
		self.tag_list.get(2).get_attribute("href").click()
		#self.soup.find_element_by_xpath("//a[@name,'tj_news']").click()
	def quit(self,driver):
		self.driver.quit()
#url="http://www.baidu.com"
f_url=open('/home/sunying/crawl/url_list.txt','r')
url=f_url.readline
while url:
	geturl=Get_url(url)
	#print geturl.open_url(url)
	html=geturl.open_url(url)
	print html
	tag_list=geturl.getTag(html)
	#print tag_list
	'''new_url=tag_list.get(2).get_attribute("href")
	i=0
	while i<=50:
		href=tag_list.get(i).get_attribute("href").get_txt
		f=open('/home/sunying/hello-jane/weathercrawler/hzqx.txt','w')
		f.write(href)
		f.close()
		i+=2

	tagtxt=geturl.compile(tag)
	print tagtxt
	geturl.getnextpage(html)
	'''
	i=1
	while i<=5:
		geturl.getnextpage(tag_list)
		i+=1
	url=f_url.readline
	


