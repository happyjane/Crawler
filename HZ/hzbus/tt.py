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
def addline(filename):
    '''Add a new line Tel'''
    f=csv.writer(file(filename, 'ab'))
    #record=[name,x,y,uid,fRoadName,fAroundMarks]
    #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
    f.writerow([name,x,y,uid,fRoadName,fAroundMarks])
    #print 'New line has been added!'
    #f.close()
lis=[]    
with open('/home/sunying/hello-jane/weathercrawler/hzbus/try.csv','a') as csvfile:
        #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter = csv.writer(csvfile, dialect='excel')  
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
            #print node
            spamwriter.writerow([node])
            spamwriter.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
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
                print name
                if uid not in lis:
                    lis.append(name)
                    nodes= n.getElementsByTagName("Stop") 
                    #print nodes
                    x= n.getAttribute("x")
                    y= n.getAttribute("y")
                    uid= n.getAttribute("uid")
                    fRoadName= n.getAttribute("fRoadName")
                    fAroundMarks= n.getAttribute("fAroundMarks")
                    #print name,x,y,uid,fRoadName,fAroundMarks
                    #lin=[name,x,y,uid,fRoadName,fAroundMarks]
                    #spamwriter.writerow(lin)
                    addline(r'/home/sunying/hello-jane/weathercrawler/hzbus/try.csv')
            else:
                pass
        i+=1  
print lis