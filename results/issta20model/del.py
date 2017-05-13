import os
files=os.listdir()
results=list(filter(lambda x:'result' in x,files))
for i in result:
	f=open('i')
	c=f.readlines()
	f.close()
	if len(c)<3:
		os.remove(i)