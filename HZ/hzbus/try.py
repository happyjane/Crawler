#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.dom import  minidom 
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/tryaaa.csv', 'w'))
f.writerow(['uid','name','x','y','fRoadName','fAroundMarks'])     
def addline(filename):
    '''Add a new line Tel'''
    f=csv.writer(file(filename, 'ab'))
    #record=[name,x,y,uid,fRoadName,fAroundMarks]
    #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
    f.writerow([uid,name,x,y,fRoadName,fAroundMarks])
def addline2(filename):
    '''Add a new line Tel'''
    f=csv.writer(file(filename, 'ab'))
    f.writerow([name2,linetype])
    #print 'New line has been added!'
    #f.close()
ls=[]    
#with open('/home/sunying/hello-jane/weathercrawler/hzbus/tryaa.csv','ab') as csvfile:
        #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
#    spamwriter = csv.writer(csvfile, dialect='excel') 
#    spamwriter.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
i=1
while i<=276:
    #line='line%d'% (i)
    #3print line
    f=open('/home/sunying/hello-jane/weathercrawler/hzbus/raw/line%s.txt'%str(i),'r')
    page = f.read()
    f.close 
    #print 'line%s.txt'%str(i)
    if len(page)!=0:
        xf=open('/home/sunying/hello-jane/weathercrawler/hzbus/line/line%s.xml'%str(i),'w')
        xf.write(str(page))
        xf.close()
        #print 'line%s.xml'%str(i)
        doc = minidom.parse('/home/sunying/hello-jane/weathercrawler/hzbus/line/line%s.xml'%str(i))  
        root = doc.documentElement 
        #node = root.getAttribute("name")
        #print node
        #spamwriter.writerow([node])
        #spamwriter.writerow(['uid','name','x','y','fRoadName','fAroundMarks'])
        #f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/try.csv', 'w'))  
        #f.writerow([node])
        #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks']) 
        nodes= root.getElementsByTagName("Stop") 
        
        #with open('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'ab') as csvfile:
            #spamwriter = csv.writer(csvfile, dialect='excel') 
        #f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'aw'))
        #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])  
        for n in nodes: 
            uid= n.getAttribute("uid")
            name= n.getAttribute("name")
            x= n.getAttribute("x")
            y= n.getAttribute("y")
            fRoadName= n.getAttribute("fRoadName")
            fAroundMarks= n.getAttribute("fAroundMarks")
            #print name,x,y,uid,fRoadName,fAroundMarks
            #lin=[name,x,y,uid,fRoadName,fAroundMarks]
            #spamwriter.writerow(lin)
            if uid not in ls:
                ls.append(uid)
                addline(r'/home/sunying/hello-jane/weathercrawler/hzbus/tryaaa.csv')
                nodes2=n.getElementsByTagName("LineName")
                for n in nodes2:
                    name2=n.getAttribute("name")
                    linetype=n.getAttribute("type")
                    addline2(r'/home/sunying/hello-jane/weathercrawler/hzbus/tryaaa.csv')
    else:
        pass
    i+=1    