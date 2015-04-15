import re
import csv
from sgmllib import SGMLParser
from bs4 import BeautifulSoup
import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
soup=open('/home/sunying/hello-jane/weathercrawler/sucess/soup.html')
soup = BeautifulSoup(soup)
#soup= soup.prettify() 
soup=soup.find_all("table")
#print soup
res=re.compile(r'<td><strong>(\d|\d{2})</strong></td>'+r'<td>(-?\d+\.\d|-?\d{2}|-|-?\d|-?\d+\.\d{2}|-?\d{2}+\.\d|-?\d{2}+\.\d{2})</td>'*10)
result=res.findall(str(soup))
print result
#f=open('/home/sunying/hello-jane/weathercrawler/re.csv','w')
with open('/home/sunying/hello-jane/weathercrawler/sucess/result.csv', 'wb') as csvfile:
    #spamwriter = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    i=0
    while i < len(result):
        spamwriter = csv.writer(csvfile, dialect='excel')
        spamwriter.writerow(result[i])
        i+=1