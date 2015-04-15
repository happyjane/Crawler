 #! /usr/bin/env python
# -*- coding: UTF-8 -*-
from xml.dom import  minidom       
doc = minidom.parse("config.xml") 
root = doc.documentElement  
nodes= root.getElementsByTagName("Stop") 
for n in nodes:  
    print n.getAttribute("name") #获取属性值  
    #print n.childNodes[0].data  #获取文本值  
    print n.getAttribute("type")


    #Filename: TelBook.py

import sys
import os
import time
import csv

def addPerson(filename):
    '''Add a new Person\'s Tel'''
    person = raw_input('Enter the person\'s name: ')
    tel = raw_input('Enter the person\'s tel: ')
    update=time.strftime('%Y-%m-%d %H:%m:%S')
    
    f=csv.writer(file(filename, 'a'))
    f.writerow([person,tel,update])
    #f.close()
    
    print 'New Person\'s tel has been added!'
    
if (os.path.isfile('TelBook.csv'))==False:
        title=['NAME','TEL','TIME']
        f=csv.writer(file('TelBook.csv','w'))
        f.writerow(title)
        #f.close()
        
input=raw_input('Do you wanna Enter a new Person\' tel?(y/n)')
if input=='y':
    flag=True
else:
    flag=False
    print 'Thanks, Bye!'
while flag:     
    addPerson('TelBook.csv')
    t=raw_input('Do you wanna Enter another?(y/n)')
    if t!='y':
        print 'Thanks, Bye!'
        break
