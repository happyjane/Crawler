filename='/home/sunying/crawler/greatfire/url_greatfire.txt'
f=open(filename,'r')
f_write=open('/home/sunying/crawler/greatfire/url_fianl.txt','aw')
lines=f.readlines()
count=0
for line in lines:
	list=line.replace('%','').split(' ')
	print list
	if int(list[3])==0:
		pass
	else:
		count+=1
		f_write.write(str(list[0])+'\t'+str(list[3])+'%'+'\r\n')
f_write.write(str(count))
f_write.close
f.close