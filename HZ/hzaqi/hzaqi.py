#! /usr/bin/env python
# -*- coding: GB2312 -*-
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
        #self.ptype = ptype
        #self.month = month
        self.area=getarea()

    def url_back(self):
        self.url = '%s/wrlx=/%d+&xzqy=%6d&x=41&y=11&sjlx=%s&kssj=2014-04-01%2C00' % (self.prefix, getptype(pt),self.area[i], self.month, self.year, self.getstation(self.city))
        #url= str(self.prefix) + '/'+ self.city+'/'+ self.month + '-' + self.year + '/' + getstation(self.city)+".html"
        return self.url 
    #def getstation(self,city):
        if city=="Hangzhou":
            return 584570
        else:
            return None
    def getptype():
    	if ptype="polluteair"
    		return 2
    	if ptype="pollutewater"
    		return 1
   	def getarea():
        arealist=[330100,330183,330182,330109,330122,330108,330110,330185,330101,330102,330104,330127,330103,330105,330106]
   	    return	arealist
    def gettime():
        timelist=[day,hour]
        return timelist
        url = '%swrlx=%s&xzqy=%s&x=41&y=11&sjlx=%s&kssj=2014-04-01' % (prefix, ptype[j], arealist[i],ttype[j])
with open('/home/sunying/hello-jane/weathercrawler/hzqx/hzweather2.csv','a') as csvfile:
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

