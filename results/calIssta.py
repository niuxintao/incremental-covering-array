import os
import random

def cal(filename):
    f=open(filename)
    for i in range(3):
            f.readline()
    size=f.readline()
    size=size.split(',')[2].split(':')[1][1:]
    t=f.readline()
    t=t.split(',')[0]
    t=t.split('m')[0]
    a = float(t)/1000
    t = str(a)
    f.close()
    return (size,t)

def run():
    models1 = []
    for i in range(1,21):
            models1.append('20benchmark_'+ str(i))

    models2 = []
    for i  in range(31,36):
            models2.append('35benchmark_'+str(i))

    for i  in range(1,31):
            models2.append('35benchmark_'+str(i))
            

    models3 =['Banking1','Banking2','CommProtocol','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

    models4 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]
    
    res=dict()

    os.chdir('./issta20model/')
    files=os.listdir()

    for i in models3:
            res[i]=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model=name[0]
            strength=int(name[2])
            repeat=int(name[3])
            res[model][strength-2][repeat-1]=cal(i)
           

    os.chdir('../issta35model/')
    files=os.listdir()   
	    
    for i in models2:
            res[i]=[[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]


    results=list(filter(lambda x:'result' in x,files))
    for i in results:
            name=i.split('_')
            model='35'+name[0]+'_'+name[1]
            strength=int(name[3])
            repeat=int(name[4])
            res[model][strength-2][repeat-1]=cal(i)
	    
    os.chdir('../')

    key = models3 + models2
    
    f=open('issta'+ 'resSize.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    print('issta-size')
    print('[')
    for i in key:
            f.write(i+',')
            value=res[i]
            print('[', end='')
            for j in range(5):
                    minimal = 0
                    times = 0
                    for k in range(3):
                            if not value[j][k]==0:
                                    minimal += int(value[j][k][0])
                                    times += 1

                    if not times == 0:
                            f.write(str(float(minimal)/times)+',')                                
                            print(str(float(minimal)/times) + ',', end='')
                    else:
                            f.write('-,')
            print('],')
            f.write('\n')
    print(']')
    f.close()


    f=open('issta'+'resTime.csv','w')
    f.write('model, 2, 3, 4, 5, 6\n')
    print('issta'+'-time')
    print('[')
    for i in key:
            f.write(i+',')
            value=res[i]
            print('[', end='')
            for j in range(5):
                    minimal = 0
                    times = 0
                    for k in range(3):
                            if not value[j][k]==0:
                                    minimal += float(value[j][k][1])
                                    times += 1

                    if not times == 0:
                            f.write(str(float(minimal)/times)+',')                                
                            print(str(float(minimal)/times) + ',', end='')
                    else:
                            f.write('-,')
            print('],')
            f.write('\n')
    print(']')
    f.close()


if __name__=='__main__':
        run()
