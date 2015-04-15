ls=[]
i=1
while i<=5:	
	name=raw_input('name:')
	if name not in ls:
		ls.append(name)
	i+=1
print ls