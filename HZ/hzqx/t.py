#! /usr/bin/env python
# -*- coding: utf-8 -*-
#import html5lib
import urllib2
import codecs
import re
import csv
from bs4 import BeautifulSoup
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class Crawler(object):

    def __init__(self,year,month,city):
        self.prefix = 'http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?'
        self.pollutetype = pollutetype
        self.datatype = datatype
        self.area=area
        self.data=data
        self.hour=hour
    def url_back(self):
        self.url = '%swrlx=%d&xzqy=%d&x=17&y=9&sjlx=%s&kssj=%s%2C%02d' % (self.prefix, self.pollutetype, self.area, self.data, self.hour)
        return self.url 
        #print self.url
    def getstation(self,city):
        if area=="hzshi":
            return 330100
        else:
            return None
    def getHtml(self,url):
        self.page = urllib2.urlopen(self.url)
        self.html = self.page.read()
        self.soup=BeautifulSoup(self.html)
        self.page.close()
        return self.soup
    def getTag(self,soup):
        self.csoup=self.soup
        self.csoup=str(self.csoup)
        self.soup = BeautifulSoup(self.csoup).soup.find_all("table")
        #self.=self.soup.find_all("table")
        self.csoup=str(self.soup)
        return self.tag
    def compile(self,csoup):
        self.res=re.compile(r'<td><strong>(\d|\d{2})</strong></td>'+r'<td>(-?\d+\.\d|-?\d{2}|-|\d|-?\d|-?\d+\.\d{2}|-?\d+\.\d{2})</td>'*10)
        self.result=self.res.findall(self.csoup)
        return self.result