import re
#! /usr/bin/env python
# -*- coding: utf-8 -*-
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
#url='http://www.tutiempo.net/en/Climate/ANQING/584240.htm'
year=2012
city='Hangzhou'
class Crawler(object):

    def __init__(self,year,month,city):
        self.prefix = 'http://www.tutiempo.net/clima'
        self.year = year
        self.month = month
        self.city=city
    def url_back(self):
        self.url = '%s/%s/%02d-%04d/%d.htm' % (self.prefix, self.city, self.month, self.year, self.getstation(self.city))
        #url= str(self.prefix) + '/'+ self.city+'/'+ self.month + '-' + self.year + '/' + getstation(self.city)+".html"
        return self.url 
        print self.url
    def getstation(self,city):
        if city=="Hangzhou":
            return 584570
        else:
            return None
    def getHtml(self,url):
        self.page = urllib2.urlopen(self.url)
        self.html = self.page.read()
        self.soup=BeautifulSoup(self.html)
        #f=open('/home/sunying/hello-jane/weathercrawler/f.txt','w')
        #f.write(self.html)
        #f.close()
        self.page.close()
        return self.soup
month=1
while month<=12:            
    crawler= Crawler(year,month,city)
    #print crawler.url_back()
    csoup=crawler.getHtml(crawler.url_back())
    #f=open('/home/sunying/hello-jane/weathercrawler/sucess/soup.html','w')
    csoup=str(csoup)
    #print csoup
    #f.close()
    #soup=open('/home/sunying/hello-jane/weathercrawler/sucess/soup.html')
    soup = BeautifulSoup(csoup)
    #soup= soup.prettify() 
    csoup=soup.find_all("table")
    #print soup
    res=re.compile(r'<td><strong>(\d|\d{2})</strong></td>'+r'<td>(-?\d+\.\d|-?\d{2}|-|\d|-?\d|-?\d+\.\d{2}|-?\d+\.\d{2})</td>'*10)
    result=res.findall(str(csoup))
    result=list(result)
    with open('/home/sunying/hello-jane/weathercrawler/hzqx/hzweather.csv','a') as csvfile:
        #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(['%4d-%02d'%(2012,month)])
        spamwriter.writerow(['Day','T','TM','Tm','SLP','H','PP','VV','V','VM','VG'])        
        i=0
        while i < len(result):
                day=result[i][0]
                day='%4d-%02d-%s'%(2012,month,day)
                print day
                result[i]=list(result[i])
                result[i][0] =day
                spamwriter.writerow(result[i])
                print result[i]
                i+=1
    print month
    #print str(result)
    month=month+1
