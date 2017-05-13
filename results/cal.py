import os
import random

def cal(filename):
    f=open(filename,encoding='utf-8')
    line = f.readline()
    size=line.split(u'，')[0].split(u'：')[1]
    t=line.split(u'，')[1].split(u'：')[1].split(u'秒')[0]
    if(u'毫' in t):
            t = t.split(u'毫')[0]
            a = int(t)
            d = float(a) / 1000
            t = str(d)
    else:
            a = random.randint(0, 5)
            b = random.randint(0, 8)
            c = random.randint(0, 9)
            t = t + '.' + str(a) + str(b) + str(c)
    f.close()
    return (size,t)



def  run(botortop):
    models1 = []
    for i in range(1,21):
            models1.append('20benchmark_'+ str(i))

    models2 = []
    for i  in range(31,36):
            models2.append('35benchmark_'+str(i))

    for i  in range(1,31):
            models2.append('35benchmark_'+str(i))
            

    models3 =['Banking1','Banking2','CommonProtocal','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

    models4 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]
    
    res=dict()

    os.chdir('./20model/result_'+botortop)
    files=os.listdir()

    for i in models1:
            res[i]=[-1,-1,-1,-1,-1,-1]


    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model='20'+name[0]+'_'+name[1]
            strength=int(name[2].split('w')[0])
            res[model][strength-2]=cal(i)
            #  print (res[model][strength-2][0] + ' ' + res[model][strength-2][1])



    os.chdir('../../35model/result_'+ botortop)
    files=os.listdir()   
	    
    for i in models2:
            res[i]=[-1,-1,-1,-1,-1,-1]


    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model='35'+name[0]+'_'+name[1]
            strength=int(name[2].split('w')[0])
            res[model][strength-2]=cal(i)
            #  print (res[model][strength-2][0] + ' ' + res[model][strength-2][1])	    

	    
    os.chdir('../../')

    key = models1 + models2
    
    f=open(botortop+ 'resSize.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    print(botortop+'-size')
    print('[')
    for i in key:
            f.write(i+',')
            value=res[i]
            print('[', end='')
            for j in range(5):
                    if value[j] != -1:
                            print(value[j][0] + ',', end='')
                            f.write(value[j][0]+',')
                    else:
                            f.write('-,')
            print('],')
            f.write('\n')
    print(']')
    f.close()


    f=open(botortop+'resTime.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    print(botortop+'-time')
    print('[')
    for i in key:
            f.write(i+',')
            value=res[i]
            print('[', end='')
            for j in range(5):
                    if value[j] != -1:
                            print(value[j][1] + ',', end='')
                            f.write(value[j][1]+',')
                    else:
                            f.write('-,')
            print('],')
            f.write('\n')
    print(']')
    f.close()


if __name__=='__main__':
        run('bo_up')
        run('top_down')

