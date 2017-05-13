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
    models1 = []
    for i in range(1,21):
	    models1.append('benchmark_'+ str(i))
    models2 = []
    for i  in range(1,36):
	    models2.append('benchmark_'+str(i))

    models3 =['Banking1','Banking2','CommProtocol','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

    models4 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]
    
    res=dict()
    for i in models3:
            res[i]=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model=name[0]
            strength=int(name[2])
            repeat=int(name[3])
            res[model][strength-2][repeat-1]=cal(i)
	
    f=open('resSize.csv','w')
    f.write('model,2_1,2_2,2_3,3_1,3_2,3_3,4_1,4_2,4_3,5_1,5_2,5_3,6_1,6_2,6_3\n')
    for key in models3:
            f.write(key+',')
            value=res[key]
            for i in range(5):
                    for j in range(3):
                            if not value[i][j]==0:
                                    f.write(value[i][j][0]+',')
                            else:
                                    f.write('-,')
            f.write('\n')
    f.close()
	    
    f=open('resTime.csv','w')
    f.write('model,2_1,2_2,2_3,3_1,3_2,3_3,4_1,4_2,4_3,5_1,5_2,5_3,6_1,6_2,6_3\n')
    for key in models3:
            f.write(key+',')
            value=res[key]
            for i in range(5):
                    for j in range(3):
                            if not value[i][j]==0:
                                    f.write(value[i][j][1]+',')
                            else:
                                    f.write('-,')
            f.write('\n')
    f.close()
