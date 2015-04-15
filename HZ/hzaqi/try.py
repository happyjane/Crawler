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
arealist=[330100,330183,330182,330109,330122,330108,330110,330185,330101,
330102,330104,330127,330103,330105,330106]
prefix ='http://218.108.6.116:8080/zxjc/datashow_getdatashowhtml?'
ptype=[1,2]
ttype=['day','hour']
k=0
while k<len(ttype):
	j=0
	while j<len(ptype):
		print ptype[j]
		i=0
		while i<len(arealist):
			m=1
			while m<=12:
				d=1	
				while d<=31:
					h=00
					while h<=23:
						if h<10:
							url='%swrlx=%s&xzqy=%s&x=41&y=11&sjlx=%s12&kssj=2012-%d-%d%%2C%s'%(prefix,ptype[k],arealist[i],ttype[j],m,d,'0'+str(h))
						else:
							url='%swrlx=%s&xzqy=%s&x=41&y=11&sjlx=%s12&kssj=2012-%d-%d%%2C%s'%(prefix,ptype[k],arealist[i],ttype[j],m,d,h) 
						f=open('/home/sunying/hello-jane/crawler/hzaqi/url.txt','a')
						page = f.write(str(url))
						f.close 
						h+=1
					d+=1
					
				m+=1
			
			i=i+1 	
		j=j+1
	k+=1
	

