import os

def cal(filename):
	f=open(filename,encoding='utf-8')
	line = f.readline()
	size=line.split(u'，')[0].split(u'：')[1]
	t=line.split(u'，')[1].split(u'：')[1].split(u'秒')[0]
	f.close()
	return (size,t)


if __name__=='__main__':
    files=os.listdir()
 #   models=list(filter(lambda x:'.model' in x,files))
 #   models=list(map(lambda x:x.split('.')[0],models))
    models1 = []
    for i in range(1,21):
            models1.append('benchmark_'+ str(i))
    models2 = []
    for i  in range(1,36):
            models2.append('benchmark_'+str(i))

    models3 =['Banking1','Banking2','CommonProtocal','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

    models4 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]
    
    res=dict()
    for i in models1:
            res[i]=[-1,-1,-1,-1,-1,-1]


    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model=name[0]+'_'+name[1]
            strength=int(name[2].split('w')[0])
            res[model][strength-2]=cal(i)
            #  print (res[model][strength-2][0] + ' ' + res[model][strength-2][1])


    f=open('resSize.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    for i in models1:
            f.write(i+',')
            value=res[i]
            for j in range(5):
                    if value[j] != -1:
                            f.write(value[j][0]+',')
                    else:
                            f.write('-,')
            f.write('\n')
    f.close()


    f=open('resTime.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    for i in models1:
            f.write(i+',')
            value=res[i]
            for j in range(5):
                    if value[j] != -1:
                            f.write(value[j][1]+',')
                    else:
                            f.write('-,')
            f.write('\n')
    f.close()
	    
	    

	    
	    

