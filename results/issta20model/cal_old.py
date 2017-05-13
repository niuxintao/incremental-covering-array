import os

def cal(filename):
	f=open(filename)
	for i in range(3):
		f.readline()
	size=f.readline()
	size=size.split(',')[2].split(':')[1][1:]
	t=f.readline()
	t=t.split(',')[0]
	f.close()
	return (size,t)


if __name__=='__main__':
    files=os.listdir()
    models=list(filter(lambda x:'.model' in x,files))
    models=list(map(lambda x:x.split('.')[0],models))
    res=dict()
    for i in models:
    	res[i]=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    results=list(filter(lambda x:'result' in x,files))
    for i in results:
    	name=i.split('_')
    	model=name[0]
    	strength=int(name[2])
    	repeat=int(name[3])	
    	res[model][strength-2][repeat-1]=cal(i)
    f=open('res.csv','w')
    f.write('model,2_1,2_2,2_3,3_1,3_2,3_3,4_1,4_2,4_3,5_1,5_2,5_3,6_1,6_2,6_3\n')
    for key in res:
    	f.write(key+',')
    	value=res[key]
    	for i in range(5):
            for j in range(3):
            	if not value[i][j]==0:
            		f.write(value[i][j][0]+'/'+value[i][j][1]+',')
            	else:
            		f.write('-,')
    	f.write('\n')
    f.close()
            

