#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.dom import  minidom 
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
#import decode

def addline(filename):
	'''Add a new line Tel'''
	f=csv.writer(file(filename, 'a'))
	#record=[name,x,y,uid,fRoadName,fAroundMarks]
	#f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
	f.writerow([nam,x,y,uid,fRoadName,fAroundMarks])
	#print 'New line has been added!'
	#f.close()
	#line='line%d'% (i)
	#print line
f=open('/home/sunying/hello-jane/weathercrawler/hzbus/raw/line1.txt','r')
page = f.read()
f.close 
xf=open('/home/sunying/hello-jane/weathercrawler/hzbus/line/line1.xml','w')
xf.write(page)
xf.close()
doc = minidom.parse('/home/sunying/hello-jane/weathercrawler/hzbus/line/line1.xml')  
root = doc.documentElement 
#print root.getElementsByTagName("LineName")
node = root.getAttribute("name")
print node
f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/newt.csv', 'w'))
f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])	
f.writerow([node])
#node=node.encode('utf-8')
#name=node.getAttribute("name")
#f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/newt.csv', 'w'))
##f.writerow([node])
#f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
#print nodes.getAttribute("name")
nodes= root.getElementsByTagName("Stop") 
#print nodes#lis=[]
	#with open('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'ab') as csvfile:
		#spamwriter = csv.writer(csvfile, dialect='excel') 
	#f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'aw'))
	#f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])	
for n in nodes: 
 	nam= n.getAttribute("name")
 	x= n.getAttribute("x")
 	y= n.getAttribute("y")
 	uid= n.getAttribute("uid")
 	fRoadName= n.getAttribute("fRoadName")
 	fAroundMarks= n.getAttribute("fAroundMarks")
	print nam,x,y,uid,fRoadName,fAroundMarks
		#lin=[name,x,y,uid,fRoadName,fAroundMarks]
		#spamwriter.writerow(lin)
	addline(r'/home/sunying/hello-jane/weathercrawler/hzbus/newt.csv')
	