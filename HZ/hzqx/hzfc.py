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
#url='http://www.tutiempo.net/en/Climate/Hangzhou/584570.htm'
year=2012
city='hangzhou'
prefix='http://lishi.tianqi.com/'
class Crawler(object):

    def __init__(self,url):
        
        self.url=url
    def getHtml(self,url):
        self.page = urllib2.urlopen(self.url)
        self.html = self.page.read()
        self.soup=BeautifulSoup(self.html)
        self.page.close()
        return self.soup
    def getTag(self,soup):
        self.csoup=str(self.soup)
        self.soup = BeautifulSoup(self.csoup)
        #soup= soup.prettify() 
        self.csoup=self.soup.find_all("ul")
        return self.csoup
    def compile(self,csoup):
        #self.res=re.compile(r'<li><a\s+\S+>(\d+\S+)</a></li>\n|<li>(\S+)</li>\n'+r'<li>\d+</li>\n'*2+r'<li>(\S+)</li>\n'*3)
        #self.res=re.compile(r'<li><a\s+\S+>(\d+\S+)</a></li>\n<li>\d+</li>\n<li>\d+</li>\n<li>(\S+)</li>\n<li>(\S+)</li>\n<li>(\S+)</li>\n|<li>(\S+)</li>\n<li>\d+</li>\n<li>\d+</li>\n<li>(\S+)</li>\n<li>(\S+)</li>\n<li>(\S+)</li>\n)')
        self.result=self.res.findall(str(self.csoup))
        return self.result

m=1
while m<=12:
    if m<10:
        url='%s/%s/2012%s.html'%(prefix,city,'0'+str(m))
        date = '2012%s'%('0'+str(m))
    else:
        url='%s/%s/2012%s.html'%(prefix,city,str(m))
        date = '2012%s'%(str(m))
    print url
    crawler= Crawler(url)
    f=open('/home/sunying/crawler/hzqx/hzfc.txt','a')
    f.write(str(crawler.getTag(crawler.getHtml(url))))
    #print crawler.getTag(crawler.getHtml(url))
    result=crawler.compile(crawler.getTag(crawler.getHtml(url)))
    print result
    with open('/home/sunying/crawler/hzqx/hzfc.csv','a') as csvfile:
        spamwriter = csv.writer(csvfile, dialect='excel')
        #spamwriter.writerow(['%4d-%02d'%(2012,month)])
        #spamwriter.writerow(['Day','T','TM','Tm','SLP','H','PP','VV','V','VM','VG'])        
        i=0
        while i < len(result):
                #day=result[i][0]
                #day='%4d-%02d-%s'%(2012,month,day)
                #print day
                #result[i]=list(result[i])
                #result[i][0] =day
                spamwriter.writerow(result[i])
                print result[i]
                i+=1
    print m
    m+=1