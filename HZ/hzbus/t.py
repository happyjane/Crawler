lis=[]
i=1
while i<=10:
	name=raw_input('name:')
	if name not in lis:
		lis.append(name)
	i+=1
print lis