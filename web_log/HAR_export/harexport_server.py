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
from selenium.webdriver.support.ui import WebDriverWait
import selenium.webdriver.remote #import webelement
import time
import threading as thread 
reload(sys)
sys.setdefaultencoding('utf-8')

export_log='/home/sunying/crawl/tongyong/HAR_export/export_log/'#local dir to store the HAR

class Browser_get(object):

	def __init__(self,profile):
		
		self.profile = webdriver.FirefoxProfile( "/home/sunying/.mozilla/firefox/4kb8s0v6.default");#import local firefox preference
		self.domain = "extensions.firebug.";
	
		try:
			self.profile.add_extension(extension="/home/sunying/crawl/tongyong/HAR_export/xpi/firebug-2.0.2-fx.xpi")
			self.profile.add_extension(extension="/home/sunying/crawl/tongyong/HAR_export/xpi/netExport-0.9b6.xpi")
			#self.profile.add_extension(extension="/home/sunying/crawl/tongyong/HAR_export/xpi/tab_mix_plus-0.4.1.4-fx.xpi")
		except IOError:
			print "error1"
		

		# Set default Firefox preferences
		self.profile.set_preference("app.update.enabled", "false");
		self.profile.set_preference("browser.link.open_newwindow","1")
		self.profile.set_preference("browser.tabs.loadInBackground","false")
		#self.profile.set_preference(" browser.tabs.opentabfor.windowopen","false")
		#self.profile.set_preference(" browser.tabs.loadInBackground","false")
		#self.profile.set_preference("browser.link.open_newwindow","1")
		#self.profile.native_events_enabled = True
		#self.profile.set_preference("webdriver.log.file", "D:/crawl/export_log")

		# Set default firebug preferences
		self.profile.set_preference(self.domain + "currentVersion", "2.0.2");
		self.profile.set_preference(self.domain + "allPagesActivation", "on");
		self.profile.set_preference(self.domain + "defaultPanelName", "net");
		self.profile.set_preference(self.domain + "net.enableSites", "true");
		#self.profile.set_preference(self.domain + "delayLoad", "false");
		
		# Set default NetExport preferences
		self.profile.set_preference(self.domain + "netexport.alwaysEnableAutoExport", "true");
		self.profile.set_preference(self.domain + "netexport.showPreview", "false" );
		self.profile.set_preference(self.domain + "netexport.saveFiles", "true");
		# Auto export feature stores results into a local file
		self.profile.set_preference(self.domain + "netexport.autoExportToFile", "true");
		self.profile.set_preference(self.domain + "netexport.compress", "true");
		self.profile.set_preference(self.domain + "netexport.exportFromBFCache", "false");
		 #If set to true, requests coming from BFCache will also be exported.
		#self.profile.set_preference(self.domain + "netexport.defaultLogDir",export_log);
		self.profile.set_preference(self.domain + "netexport.pageLoadedTimeout", "15000");
		# URL of the server where the collected data should be send to.
		#self.profile.set_preference(self.domain + "netexport.beaconServerURL", "http://www.showslow.com/beacon/har/");
		self.profile.set_preference("extensions.tabmix.loadOnNewTab.type","2")
		#self.driver = webdriver.Firefox(self.profile);'''

		self.driver = webdriver.Firefox(self.profile);
		
	def openurl(self,url):
		self.url=url
		try:

			# Load test page
			self.driver.implicitly_wait(30)
			self.driver.get(self.url);
			self.driver.implicitly_wait(30)
			self.soup=self.driver
			return self.soup
		except Exception:
			print "error2"
		

	def getTag(self,soup):#get all interlink list of the page
		#self.tag_list= self.soup.find_elements_by_tag_name('a')
		self.tag_list=WebDriverWait(self.soup,30).until(lambda x: x.find_elements_by_tag_name('a'))
		return self.tag_list

	def lenth_tag(self,tag_list):#get the new interlink 
		self.tag_lenth=len(self.tag_list)
		self.number=int(self.tag_lenth/6)
		return self.number
		
	def getnextpage(self,soup,number):#click the link

		#elm=WebDriverWait(self.soup, 5).until(lambda x:x.find_elements_by_tag_name('a')[num])#.click())
		#elm.click()
		self.driver.implicitly_wait(10)
		self.soup.find_elements_by_tag_name('a')[num].click()
		self.driver.implicitly_wait(10)
		return self.soup
	
	def quit(self,driver):
		self.driver.quit()

f = open("/home/sunying/crawl/tongyong/HAR_export/url_list.txt")
url=f.readline() 
geturl=Browser_get(object)
geturl.openurl("http://www.baidu.com/")
#set the preference
try:
	i=raw_input("input 1:")
except:
	print "not 1"
while i:
	continue
	i=0

while url:
	print url 
	html=geturl.openurl(url)
	print html.title
	tag=geturl.getTag(html) 
	num=geturl.lenth_tag(tag) 
	i=1
	while i<5:
		print i
		t=1
		e=1
		while e and t<=10:
			try:
				print num
				html=geturl.getnextpage(html,num)
				e=0
			except Exception:
				print "error3"
				e=1
				num+=5
				t+=1
		print html.title
		tag=geturl.getTag(html)
		num=geturl.lenth_tag(tag) 
		i+=1
	url=f.readline() 





