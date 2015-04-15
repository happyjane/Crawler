#! /usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.dom import  minidom 
import csv
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
#f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/try.csv', 'w'))
#f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])     
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
        node = root.getAttribute("name")
        print node
        #f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/try.csv', 'w'))  
        #f.writerow([node])
        #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks']) 
        f=open('/home/sunying/hello-jane/weathercrawler/hzbus/hzbusfinal/linestop1.txt','a')
        f.write("\n"+str(node)+";",) 
        nodes= root.getElementsByTagName("Stop")
        #lis=[]
        #with open('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'ab') as csvfile:
            #spamwriter = csv.writer(csvfile, dialect='excel') 
        #f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/line1.csv', 'aw'))
        #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])  
        for n in nodes: 
            #name= n.getAttribute("name")
            #f=open('/home/sunying/hello-jane/weathercrawler/hzbus/linestop.txt','a')
            #f.write('\n'+str(node))
    #shape=root.getAttribute("shape")
            f.write(n.getAttribute("uid")+",")
    else:
        pass
    i+=1    