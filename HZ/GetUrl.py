import html5lib
import urllib2
from BeautifulSoup import BeautifulSoup
url='http://www.hzqx.com/'
def getHtml(url):
	page = urllib2.urlopen(url)
	html = page.read()
	soup=BeautifulSoup(html)
	f=open('/home/sunying/hello-jane/weathercrawler/hzqx.txt','w')
	f.write(html)
	f.close()
	page.close()
        return html
print getHtml(url)

