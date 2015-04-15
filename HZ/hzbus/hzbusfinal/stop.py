#! /usr/bin/env python
# -*- coding: utf-8 -*-
from xml.dom import  minidom 
import csv
import sys
import Cookie
reload(sys)
sys.setdefaultencoding( "utf-8" )
import os
#f=csv.writer(file('/home/sunying/hello-jane/weathercrawler/hzbus/Stop.csv', 'w'))
#f.writerow(['uid'+" "+'name','x','y','fRoadName','fAroundMarks','Linename,linetype'])     
def addline(filename):
    '''Add a new line Tel'''
    f=csv.writer(file(filename, 'ab'),delimiter=';', quoting=csv.QUOTE_MINIMAL)
    #record=[name,x,y,uid,fRoadName,fAroundMarks]
    #f.writerow(['name','x','y','uid','fRoadName','fAroundMarks'])
    f.writerow([uid,name,x,y,fRoadName,fAroundMarks,line])
def addline2(filename):
    '''Add a new line Tel'''
    f=csv.writer(file(filename, 'ab'))
    f.writerow([name2,linetype])
    #print 'New line has been added!'
    #f.close()
ls=[] 
ss=[]

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
                #addline(r'/home/sunying/hello-jane/weathercrawler/hzbus/Stop.csv')
                nodes2=n.getElementsByTagName("LineName")
                #ss=[]
                line='' 
                for n in nodes2:
                    linename=n.getAttribute("uid")
                    line=line+str(linename)
                    linetype=n.getAttribute("type")
                    line=line+","+str(linetype)+","
                    #ss.append(linetype)
                #ss = ss.encode( "UTF-8" )
                addline(r'/home/sunying/hello-jane/weathercrawler/hzbus/hzbusfinal/Stop.csv')
                print line
                
    else:
        pass
    i+=1   
#print ls
print len(ls) 
