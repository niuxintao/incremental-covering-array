#!/usr/local/python3/bin/python3.5
from os import system
import os
from multiprocessing import Pool

def generate(model):
    constraints=model.split('.')[0]+'.constraints'
    tables=[]
    for j in range(6):
        temp=[]
        temp.append([])
        temp.append([])
        temp.append([])
        tables.append(temp)
    #calculate the first 4 tables
    tlt='java -jar -Xms4g -Xmx8g IPOG.jar %s %s %d %s > %s'
    #2_1
    command=tlt%(model,constraints,2,'',model.split('.')[0]+'_result_2_1')
    system(command)
    f=open(model.split('.')[0]+'_result_2_1')
    ca=f.readlines()
    para=ca[3].split(",")[0].split(": ")[1]
    ca=ca[7:]
    f.close()
    ca=ca[:-1]
    tables[0][0].append(ca)
    tables[0][0].append(0)
    #3_1
    f=open(model.split('.')[0]+"_seed.txt","w")
    f.write(str(para)+"\n")
    f.write(str(len(tables[0][0][0]))+'\n')
    f.write("".join(tables[0][0][0]))
    f.close()
    command=tlt%(model,constraints,3,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_3_1')
    system(command)
    f=open(model.split('.')[0]+'_result_3_1')
    ca=f.readlines()
    para=ca[3].split(",")[0].split(": ")[1]
    ca=ca[7:]
    f.close()
    ca=ca[:-1]
    tables[1][0].append(ca)
    tables[1][0].append(len(tables[0][0][0]))
    #2_2
    f=open(model.split('.')[0]+"_seed.txt","w")
    f.write(str(para)+"\n")
    f.write("5\n")
    start=tables[1][0][1]
    f.write("".join(tables[1][0][0][start:(start+5)]))
    tables[1][0][1]=tables[1][0][1]+5
    f.close()
    command=tlt%(model,constraints,2,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_2_2')
    system(command)
    f=open(model.split('.')[0]+'_result_2_2')
    ca=f.readlines()
    para=ca[3].split(",")[0].split(": ")[1]
    ca=ca[7:]
    f.close()
    ca=ca[:-1]
    tables[0][1].append(ca)
    tables[0][1].append(5)
    #2_3
    f=open(model.split('.')[0]+"_seed.txt","w")
    f.write(str(para)+"\n")
    f.write("5\n")
    start=tables[1][0][1]
    f.write("".join(tables[1][0][0][start:(start+5)]))
    tables[1][0][1]=tables[1][0][1]+5
    f.close()
    command=tlt%(model,constraints,2,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_2_3')
    system(command)
    f=open(model.split('.')[0]+'_result_2_3')
    ca=f.readlines()
    para=ca[3].split(",")[0].split(": ")[1]
    ca=ca[7:]
    f.close()
    ca=ca[:-1]
    tables[0][2].append(ca)
    tables[0][2].append(5)
    for j in range(4):
        #t+1
        f=open(model.split('.')[0]+"_seed.txt","w")
        f.write(str(para)+"\n")
        f.write(str(len(tables[j+1][0][0]))+'\n')
        f.write("".join(tables[j+1][0][0]))
        f.close()
        command=tlt%(model,constraints,j+4,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_'+str(j+4)+'_1')
        system(command)
        f=open(model.split('.')[0]+'_result_'+str(j+4)+'_1')
        ca=f.readlines()
        para=ca[3].split(",")[0].split(": ")[1]
        ca=ca[7:]
        f.close()
        ca=ca[:-1]
        tables[j+2][0].append(ca)
        tables[j+2][0].append(len(tables[j+1][0][0]))
        size=len(tables[j][0][0])
        #t_2
        seed=size
        f=open(model.split('.')[0]+"_seed.txt","w")
        f.write(str(para)+"\n")
        if len(tables[j][1][0])-tables[j][1][1]<size:
            #two part
            f.write(str(size)+"\n")
            f.write("".join(tables[j][1][0][tables[j][1][1]:]))
            n=size-(len(tables[j][1][0])-tables[j][1][1])
            f.write("".join(tables[j+2][0][0][tables[j+2][0][1]:tables[j+2][0][1]+n]))
            tables[j+2][0][1]=tables[j+2][0][1]+n
        else:
            f.write(str(len(tables[j][1][0])-tables[j][1][1])+"\n")
            f.write("".join(tables[j][1][0][tables[j][1][1]:]))
            seed=len(tables[j][1][0])-tables[j][1][1]
        f.close()
        command=tlt%(model,constraints,j+3,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_'+str(j+3)+'_2')
        system(command)
        f=open(model.split('.')[0]+'_result_'+str(j+3)+'_2')
        ca=f.readlines()
        para=ca[3].split(",")[0].split(": ")[1]
        ca=ca[7:]
        f.close()
        ca=ca[:-1]
        tables[j+1][1].append(ca)
        tables[j+1][1].append(seed)
        #t_3
        seed=size
        f=open(model.split('.')[0]+"_seed.txt","w")
        f.write(str(para)+"\n")
        if len(tables[j][2][0])-tables[j][2][1]<size:
            #two part
            f.write(str(size)+"\n")
            f.write("".join(tables[j][2][0][tables[j][2][1]:]))
            n=size-(len(tables[j][2][0])-tables[j][2][1])
            f.write("".join(tables[j+2][0][0][tables[j+2][0][1]:tables[j+2][0][1]+n]))
            tables[j+2][0][1]=tables[j+2][0][1]+n
        else:
            f.write(str(len(tables[j][2][0])-tables[j][2][1])+"\n")
            f.write("".join(tables[j][2][0][tables[j][2][1]:]))
            seed=len(tables[j][2][0])-tables[j][2][1]
        f.close()
        command=tlt%(model,constraints,j+3,model.split('.')[0]+'_seed.txt',model.split('.')[0]+'_result_'+str(j+3)+'_3')
        system(command)
        f=open(model.split('.')[0]+'_result_'+str(j+3)+'_2')
        ca=f.readlines()
        para=ca[3].split(",")[0].split(": ")[1]
        ca=ca[7:]
        f.close()
        ca=ca[:-1]
        tables[j+1][2].append(ca)
        tables[j+1][2].append(seed)

if __name__ == '__main__':
    files=os.listdir()
    models=list(filter(lambda x:'.model' in x,files))
    #constraints=list(map(lambda x: x.split('.')[0]+'.constraints',models))
    pool=Pool(5)
    pool.map(generate,models)
    pool.close()
    pool.join()
    print('done')
    
    
    
    
    
    
