import os
def change_format(filename):
	f=open(filename)
	n=int(f.readline().strip('\n'))
	data=[]
	for i in range(n):
		f.readline()
		temp=f.readline().strip('\n')[2:]
		data.append(list(map(lambda x:int(x)-1,temp.split(' - '))))
	for i in data:
		i.sort()
	f.close()
	f=open(filename,'w')
	f.write(str(n)+'\n')
	for row in data:
		f.write(str(len(row))+'\n')
		f.write('- '+' - '.join(list(map(lambda x:str(x),row)))+'\n')
	f.close()

if __name__ == '__main__':
        files=os.listdir()
        cons=list(filter(lambda x:'.constraints' in x,files))
        list(map(lambda x:change_format(x),cons))
        
