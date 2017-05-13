import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co


def mean(data):
    """Return the sample arithmetic mean of data."""
    n = len(data)
    if n < 1:
        raise ValueError('mean requires at least one data point')
    return sum(data)/n # in Python 2 use sum(data)/float(n)

def _ss(data):
    """Return sum of square deviations of sequence data."""
    c = mean(data)
    ss = sum((x-c)**2 for x in data)
    return ss

def pstdev(data):
    """Calculates the population standard deviation."""
    n = len(data)
    if n < 2:
        raise ValueError('variance requires at least two data points')
    ss = _ss(data)
    pvar = ss/n # the population variance
    return pvar**0.5



#data
x= [[2,3],[2,3,4],[2,3,4,5],[2,3,4,5,6]]


out_bot_up = [
[15,57,153,212,],
[11,35,99,229,529,],
[19,51,95,166,243,],
[6,8,8,8,],
[30,109,338,868,1780,],
[16,66,228,706,2052,],
[38,214,1026,4327,16241,],
[49,304,1675,8294,38373,],
[527,6950,75676,511471,2942290,],
[112,1117,6429,30411,119219,],
[29,154,649,2595,9329,],
[36,195,904,3900,15305,],
[106,932,6866,38077,164999,],
[17,25,25,],
[18,77,217,486,],
[50,244,758,2154,5321,],
[121,923,6136,36423,185212,],
[218,1887,13334,78874,400356,],
[17,59,162,353,654,],
[30,128,415,1135,2672,],
[26,112,428,1434,4247,],
[45,293,1676,8547,],
[23,106,444,],
[33,180,867,],
[19,73,236,739,2193,],
[48,303,1719,8794,],
[32,185,892,3977,],
[19,76,211,605,1591,],
[22,103,381,1322,],
[54,380,2471,],
[25,124,501,1725,],
[12,35,96,248,613,],
[47,325,1979,],
[22,83,272,845,],
[47,336,2125,],
[47,322,1959,10416,],
[43,269,1476,],
[40,214,1036,],
[39,253,1222,5444,],
[32,180,789,3041,],
[25,121,460,1633,],
[41,278,1586,],
[52,334,2095,],
[51,377,2528,],
[60,472,3295,],
[39,238,1140,4651,],
[37,171,696,2529,],
[14,50,141,379,971,],
[48,349,2170,],
[52,407,2682,],
[34,209,1154,5356,],
[37,213,1037,4525,],
[57,427,2891,],
[29,153,696,],
[22,100,388,1367,],
]

out_top_down = [
[55,204,211,212,],
[51,104,248,360,523,],
[86,213,221,230,240,],
[7,8,8,8,],
[93,584,671,1394,1776,],
[143,171,571,1581,1978,],
[153,656,1004,],
[252,1039,1644,],
[5240,6866,],
[1033,1125,],
[85,1815,2409,2588,],
[124,788,3511,3880,],
[1822,4622,6855,],
[25,25,25,],
[436,468,484,486,],
[355,1100,1712,2106,],
[758,898,],
[966,1879,],
[47,390,487,488,540,],
[290,1085,1674,2285,2565,],
[140,512,1519,4095,4185,],
[147,1046,1631,],
[134,350,444,],
[128,527,838,],
[41,184,626,1737,2183,],
[200,1084,1680,],
[153,872,2721,3852,],
[64,265,626,1157,1571,],
[118,337,892,1323,],
[210,1237,2442,],
[154,592,1510,1644,],
[23,63,149,413,604,],
[183,1040,1988,],
[72,201,592,829,],
[301,1246,2063,],
[291,1384,1885,],
[317,977,1465,],
[121,719,1040,],
[143,875,1163,],
[174,885,2443,2992,],
[173,507,1175,1614,],
[163,1083,1514,],
[150,1309,2145,],
[188,1262,2535,],
[248,1576,3278,],
[174,765,1070,],
[143,691,1953,2509,],
[50,167,342,782,956,],
[199,1190,2105,],
[228,1467,2673,],
[190,711,1111,],
[162,720,1004,],
[194,1497,2888,],
[102,589,681,],
[91,519,1108,1362,],
]


out_issta = [
[17.333333333333332,57.333333333333336,158.0,212.0,212.0,],
[12.0,37.666666666666664,99.66666666666667,236.33333333333334,529.0,],
[19.666666666666668,52.0,103.33333333333333,169.33333333333334,241.0,],
[6.0,8.0,8.0,8.0],
[31.666666666666668,108.33333333333333,340.3333333333333,873.6666666666666,1828.6666666666667,],
[18.0,67.0,229.0,722.3333333333334,2052.0,],
[38.333333333333336,214.66666666666666,1031.6666666666667,4326.0,16241.0,],
[50.333333333333336,304.3333333333333,1682.0,8294.0,],
[534.0,6953.666666666667,75676.0,],
[117.66666666666667,1118.0,6480.333333333333,30762.666666666668,119219.0,],
[30.666666666666668,164.66666666666666,645.3333333333334,2601.6666666666665,9329.0,],
[35.666666666666664,190.0,902.6666666666666,3917.3333333333335,15305.0,],
[110.66666666666667,927.6666666666666,6919.0,38394.0,164999.0,],
[18.0,25.0,25.0],
[20.333333333333332,77.33333333333333,221.0,485.0],
[52.333333333333336,241.66666666666666,765.0,2182.0,5321.0,],
[124.66666666666667,913.3333333333334,6192.333333333333,36601.333333333336,185212.0,],
[220.0,1881.0,13342.666666666666,79099.0,400356.0,],
[18.0,59.666666666666664,161.0,360.6666666666667,654.0,],
[31.333333333333332,127.33333333333333,413.0,1156.3333333333333,2672.0,],
[27.0,114.66666666666667,428.0,1464.3333333333333,4247.0,],
[45.0,295.0,1676.0,],
[23.333333333333332,106.0,],
[34.333333333333336,180.0,],
[19.333333333333332,71.66666666666667,235.0,739.0,],
[47.0,301.6666666666667,1713.6666666666667,8794.0,],
[35.0,184.33333333333334,901.6666666666666,3977.0,],
[20.333333333333332,72.66666666666667,213.0,610.6666666666666,1591.0,],
[24.0,104.0,381.0,],
[53.333333333333336,380.0,],
[28.333333333333332,122.33333333333333,501.0,],
[12.0,35.333333333333336,96.66666666666667,251.0,613.0,],
[48.666666666666664,325.3333333333333,1979.0,],
[22.0,82.33333333333333,275.0,845.0,],
[49.0,337.3333333333333,2125.0,],
[49.0,323.6666666666667,1959.0,10416.0,],
[45.0,269.0,],
[42.0,211.33333333333334,1036.0,],
[45.0,250.66666666666666,1235.0,5444.0,],
[35.333333333333336,177.66666666666666,795.6666666666666,3056.3333333333335,10678.0,],
[27.666666666666668,121.66666666666667,466.6666666666667,1633.0,],
[46.0,276.6666666666667,1586.0,],
[50.0,340.6666666666667,2095.0,],
[52.0,377.0,],
[59.333333333333336,471.0,3295.0,],
[44.0,239.33333333333334,1145.0,4651.0,],
[39.333333333333336,171.33333333333334,694.6666666666666,2529.0,],
[14.666666666666666,49.666666666666664,142.33333333333334,387.0,971.0,],
[49.666666666666664,350.0,2170.0,],
[55.666666666666664,407.0,],
[36.0,211.0,1166.3333333333333,5356.0,],
[40.333333333333336,212.66666666666666,1043.0,4525.0,],
[56.666666666666664,426.0,2891.0,],
[31.0,153.0,],
[23.666666666666668,100.0,388.0,],
]



out1 = [0, 0, 0, 0, 0]

out1_d = [0, 0, 0, 0, 0]

out2 = [0, 0, 0, 0, 0]

out2_d = [0, 0, 0, 0, 0]

out3 = [0, 0, 0, 0, 0]


out_m_1 = [0, 0, 0, 0, 0]

out_m_1_d = [[], [], [], [], []]

out_m_2 = [0, 0, 0, 0, 0]

out_m_2_d = [[], [], [], [], []]

models1 =['Banking1','Banking2','CommProtocol','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

models2 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]

for i in range(0, 55):
    for j in range(0, 5):
        if (len(out_bot_up[i]) > j and len(out_top_down[i]) > j):
            if(out_bot_up[i][j] < out_top_down[i][j]):
                out1[j] += 1
                out1_d[j] += out_top_down[i][j]  - out_bot_up[i][j]
            elif (out_top_down[i][j] < out_bot_up[i][j]):
                out2[j] += 1
                out2_d[j] += out_bot_up[i][j] - out_top_down[i][j]
            else:
                out3[j] += 1
        elif(len(out_bot_up[i]) > j):  #bot up more
            out_m_1[j]  += 1
            if (i < 20):
                out_m_1_d[j].append(models1[i])
            elif (i < 25):
                out_m_1_d[j].append(models2[i-20])
            else:
                out_m_1_d[j].append('Syn' + str(i-24))
        elif(len(out_top_down[i]) > j): #down more
            out_m_2[j]  += 1
            if (i < 20):
                out_m_2_d[j].append(models1[i])
            elif (i < 25):
                out_m_2_d[j].append(models2[i-20])
            else:
                out_m_2_d[j].append('Syn' + str(i-24))
            
            


print('Degree' + ' & ', end='')
print('Bottom-up' + ' & ', end='')
print('Top-up' + ' & ', end='')
print('Equal \\\\')
for i in range(0, 5):
    print(str(i+2) + ' & ', end='')
    
    avg = '-'
    if (not out1[i] == 0):
        avg = str(round(out1_d[i]/out1[i], 2))
    print(str(out1[i])+ ' ('+ avg +') & ', end='')

    avg2 = '-'
    if (not out2[i] == 0):
        avg2 = str(round(out2_d[i]/out2[i], 2))
    print(str(out2[i])+ ' ('+ avg2 +') & ', end='')

    
    print(str(out3[i]) + ' \\\\')

print (out_m_1)
print (out_m_1_d)
print (out_m_2)
print (out_m_2_d)



out1 = [0, 0, 0, 0, 0]

out1_d = [0, 0, 0, 0, 0]

out2 = [0, 0, 0, 0, 0]

out2_d = [0, 0, 0, 0, 0]

out3 = [0, 0, 0, 0, 0]


out_m_1 = [0, 0, 0, 0, 0]

out_m_1_d = [[], [], [], [], []]

out_m_2 = [0, 0, 0, 0, 0]

out_m_2_d = [[], [], [], [], []]

models1 =['Banking1','Banking2','CommProtocol','Concurrency','Healthcare1','Healthcare2','Healthcare3','Healthcare4','Insurance','NetworkMgmt','ProcessorComm1','ProcessorComm2','Services','Storage1','Storage2','Storage3','Storage4','Storage5','SystemMgmt','Telecom']

models2 =['SPIN-S','SPIN-V','GCC','Apache','Bugzilla',]

for i in range(0, 55):
    for j in range(0, 5):
        if (len(out_bot_up[i]) > j and len(out_issta[i]) > j):
            if(out_bot_up[i][j] < out_issta[i][j]):
                out1[j] += 1
                out1_d[j] += out_issta[i][j]  - out_bot_up[i][j]
            elif (out_issta[i][j] < out_bot_up[i][j]):
                out2[j] += 1
                out2_d[j] += out_bot_up[i][j] - out_issta[i][j]
            else:
                out3[j] += 1
        elif(len(out_bot_up[i]) > j):  #bot up more
            out_m_1[j]  += 1
            if (i < 20):
                out_m_1_d[j].append(models1[i])
            elif (i < 25):
                out_m_1_d[j].append(models2[i-20])
            else:
                out_m_1_d[j].append('Syn' + str(i-24))
        elif(len(out_issta[i]) > j): #down more
            out_m_2[j]  += 1
            if (i < 20):
                out_m_2_d[j].append(models1[i])
            elif (i < 25):
                out_m_2_d[j].append(models2[i-20])
            else:
                out_m_2_d[j].append('Syn' + str(i-24))
            
            


print('Degree' + ' & ', end='')
print('Bottom-up' + ' & ', end='')
print('Traditional' + ' & ', end='')
print('Equal \\\\')
for i in range(0, 5):
    print(str(i+2) + ' & ', end='')
    
    avg = '-'
    if (not out1[i] == 0):
        avg = str(round(out1_d[i]/out1[i], 2))
    print(str(out1[i])+ ' ('+ avg +') & ', end='')

    avg2 = '-'
    if (not out2[i] == 0):
        avg2 = str(round(out2_d[i]/out2[i], 2))
    print(str(out2[i])+ ' ('+ avg2 +') & ', end='')

    
    print(str(out3[i]) + ' \\\\')

print (out_m_1)
print (out_m_1_d)
print (out_m_2)
print (out_m_2_d)    
