import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co

#data
x2= [2,3]
x3= [2,3,4]
x4= [2,3,4,5]

out1 = [0.848812116,1]
out1_ = [1,0.979904816]
out2 = [0.868905758,0.921701283,1]	
out2_ =[1,1,0.980740836]
out3 = [0.888397783,0.904887422,0.940031412,1]
out3_ =[1,1,1,0.978665755]
out4= [0.950018511,1]
out4_ = [1,0.742006773]
out5= [1,0.928961056,1]	
out5_=[0.989130423,1,0.941583712]	
out6=[1,0.923638349,1,1]
out6_=[0.976771196,1,0.866773994,0.91455794]
out7=[0.907180396,1]
out7_=[1,0.98830046]
out8=[0.885615213,0.984477643,1]	
out8_ =[1,1,0.980486652	]
out9= [0.915467678,0.972369213,1,1]
out9_=[1,1,0.980326266,0.96393517]
out10=[0.981283478,1]
out10_=[1,0.95348833]
out11=[1,1,1]
out11_=[0.979166687,0.997996023,0.956754734]	
out12=[0.984455974,0.963178304,1,1]
out12_=[1,1,0.953142875,0.943431803]
out13=[0.934566164,1]
out13_=[1,0.994925827]
out14=[0.905292486,0.941090354,1]	
out14_=[1,1,0.977157112]
out15=[0.915730338,0.921779654,0.961844063,1]
out15_=[1,1,1,0.977915519]
out16=[0.952680266,1]
out16_=[1,0.732184584]
out17=[1,0.928922228,1]
out17_=[0.988439306,1,0.945788009]	
out18=[1,0.92014643,1,1]
out18_=[0.973286928,1,0.873632132,0.920081402]
out19=[1,1]
out19_=[0.981941326,0.95813949]
out20=[1,0.977346254,1]
out20_=[0.9909091,1,0.964568529]	
out21=[1,0.966324567,1,1]
out21_=[0.977220978,1,0.935532132,0.93930603]
out22=[0.986003145,1]
out22_=[1,0.978307961]
out23=[0.982998449,0.986882378,1]	
out23_=[1,1,0.933109387]
out24=[0.987558332,0.99343832,1,1]
out24_=[1,1,0.977493439,0.927179285]
out25=[0.96590907,1]
out25_=[1,0.965475511]
out26=[0.9392265,0.981602383,1]	
out26_=[1,1,0.961500095]
out27=[0.932584331,0.952325576,1,1]
out27_=[1,1,0.97087975,0.941454628]

##out2 = [1236,1673,2203,2803,3288,3610,3675,4132]
##out3 = [492,626,731,850,865,817,659,550]
##out4 = [68,205,325,421,611,883,1343,1646]
##out5 = [1612,2274,2894,3643,4206,4287,4934,5475]
##out6 = [1346,1833,2383,3576,2919,3306,3517,3364]
##out7 = [1252,1634,2149,2761,3071,3205,3088,3278]
##out8 = [13595,18271,23755,29429,33968,36602,36706,39761]
##out9 = [6341,9619,17873,15622,23714,18384,20295,21127]
##out10 = [84,112.6,248.3936402,420.9011487,632,825,971.27,1343.7]
##out11 = [374,535.1847201,821.9746154,1147.672,1526.072807,1857.583225,2165.713401,2712.648204]
##I_out1 = [1305,1991.881,2671.393,3394.5,4093.24719,4706.72,5243.552,6016.643]
##gas1 = [4186,7473,10356,11242,11475,12149,12149,12149]
##gas2 = [0,0,0,7,62,601,342,396,]
##gas3 = [3,7,7.8,13,16,19,20,23]
##flux1 = [0,0,0,1.5001,10.35221696,12.4,25.934,33.727]
##flux2 = [6,13.69,22.358,31.7604005,42.0262,47.8298,56.31445151,72.54693]
##flux3 = [17,20.048,27.779,31.7394,31.211,29.0254371,23.9779,29.64697]
##flux4 = [98,75,91,18,64,88,33,48]

###function to normalize data(right y axis)
##def norm(y):
##    normf = co.normalize()
##    normr = normf(y)
##    return normr
##

#define figure and figure size figsize=(width, height)
fig = plt.figure(figsize=(9, 6))

#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18


ax1 = fig.add_subplot(3,9,1) #gas1
ax1n = fig.add_subplot(3,9,1, sharex=ax1, sharey=ax1, frameon=False) #gas1 nomeeritud


ax2 = fig.add_subplot(3,9,10) #out9
ax2n = fig.add_subplot(3,9,10, sharex=ax2,sharey=ax2, frameon=False) #out9


ax3 = fig.add_subplot(3,9,19) #out8
ax3n = fig.add_subplot(3,9,19, sharex=ax3, sharey=ax3, frameon=False) #out8


ax4 = fig.add_subplot(3,9,2) #out2
ax4n = fig.add_subplot(3,9,2, sharex=ax4, sharey=ax4, frameon=False) #out2

ax5 = fig.add_subplot(3,9,11) #out5
ax5n = fig.add_subplot(3,9,11, sharex=ax5, sharey=ax5, frameon=False) #out5


ax6 = fig.add_subplot(3,9,20) #I_out1
ax6n = fig.add_subplot(3,9,20, sharex=ax6, sharey=ax6, frameon=False) #I_out1


ax7 = fig.add_subplot(3,9,3) #out11
ax7n = fig.add_subplot(3,9,3, sharex=ax7, sharey=ax7,  frameon=False) #out11

ax8 = fig.add_subplot(3,9,12) #out7
ax8n = fig.add_subplot(3,9,12,sharex=ax8, sharey=ax8, frameon=False) #out7


ax9 = fig.add_subplot(3,9,21) #out6
ax9n = fig.add_subplot(3,9,21, sharex=ax9, sharey=ax9,  frameon=False) #out6


ax10 = fig.add_subplot(3,9,4) #out3
ax10n = fig.add_subplot(3,9,4, sharex=ax10, sharey=ax10, frameon=False) #out3


ax11 = fig.add_subplot(3,9,13) #out10
ax11n = fig.add_subplot(3,9,13, sharex=ax11,  sharey=ax11, frameon=False) #out10


ax12 = fig.add_subplot(3,9,22) #out4
ax12n = fig.add_subplot(3,9,22, sharex=ax12,  sharey=ax12, frameon=False) #out4

ax13 = fig.add_subplot(3,9,5) #flux2
ax13n = fig.add_subplot(3,9,5, sharex=ax13,  sharey=ax13, frameon=False) #flux2


ax14 = fig.add_subplot(3,9,14) #flux4
ax14n = fig.add_subplot(3,9,14, sharex=ax14,  sharey=ax14, frameon=False) #flux4

ax15 = fig.add_subplot(3,9,23) #gas2
ax15n = fig.add_subplot(3,9,23, sharex=ax15,  sharey=ax15, frameon=False) #gas2



ax16 = fig.add_subplot(3,9,6) #gas3
ax16n = fig.add_subplot(3,9,6, sharex=ax16,  sharey=ax16, frameon=False) #gas3

ax17 = fig.add_subplot(3,9,15) #flux1
ax17n = fig.add_subplot(3,9,15, sharex=ax17,  sharey=ax17, frameon=False) #flux1


ax18 = fig.add_subplot(3,9,24) #flux3
ax18n = fig.add_subplot(3,9,24, sharex=ax18,  sharey=ax18, frameon=False) #flux3

ax19 = fig.add_subplot(3,9,7) #flux3
ax19n = fig.add_subplot(3,9,7, sharex=ax19,  sharey=ax19, frameon=False) #flux3


ax20 = fig.add_subplot(3,9,16) #flux3
ax20n = fig.add_subplot(3,9,16, sharex=ax20,  sharey=ax20, frameon=False) #flux3


ax21 = fig.add_subplot(3,9,25) #flux3
ax21n = fig.add_subplot(3,9,25, sharex=ax21,  sharey=ax21, frameon=False) #flux3


ax22 = fig.add_subplot(3,9,8) #flux3
ax22n = fig.add_subplot(3,9,8, sharex=ax22,  sharey=ax22, frameon=False) #flux3


ax23 = fig.add_subplot(3,9,17) #flux3
ax23n = fig.add_subplot(3,9,17, sharex=ax23,  sharey=ax23, frameon=False) #flux3


ax24 = fig.add_subplot(3,9,26) #flux3
ax24n = fig.add_subplot(3,9,26, sharex=ax24,  sharey=ax24, frameon=False) #flux3


ax25 = fig.add_subplot(3,9,9) #flux3
ax25n = fig.add_subplot(3,9,9, sharex=ax25,  sharey=ax25, frameon=False) #flux3

ax26 = fig.add_subplot(3,9,18) #flux3
ax26n = fig.add_subplot(3,9,18, sharex=ax26,  sharey=ax26, frameon=False) #flux3

ax27 = fig.add_subplot(3,9,27) #flux3
ax27n = fig.add_subplot(3,9,27, sharex=ax27,  sharey=ax27, frameon=False) #flux3

#plot data and normalized data 
ax1.plot(x2, out1,  marker="s",  color="k")
ax1n.plot(x2, out1_, ls="--", marker="d", mfc="None",   color="k")

ax2.plot(x3, out2,  marker="s", mfc="None",color="k")
ax2n.plot(x3, out2_, ls="--",color="k")

ax3.plot(x4, out3,  marker="s",mfc="None", color="k")
ax3n.plot(x4, out3_, ls="--",marker="d", mfc="None", color="k")

ax4.plot(x2, out4, marker="s", color="k")
ax4n.plot(x2, out4_, ls="--",marker="d", color="k")

ax5.plot(x3, out5, marker="s", color="k")
ax5n.plot(x3, out5_, ls="--",marker="d", mfc="None",color="k")


ax6.plot(x4, out6 , marker="s", color="k")
ax6n.plot(x4, out6_, ls="--", marker="d", mfc="None",color="k")

ax7.plot(x2, out7 , marker="s", color="k")
ax7n.plot(x2, out7_, ls="--", marker="d", mfc="None", color="k")

ax8.plot(x3, out8 , marker="s", color="k")
ax8n.plot(x3, out8_, ls="--",marker="d", mfc="None", color="k")


ax9.plot(x4, out9, marker="s", color="k")
ax9n.plot(x4, out9_, ls="--",marker="d", mfc="None",color="k")

ax10.plot(x2, out10 , marker="s", color="k")
ax10n.plot(x2, out10_, ls="--",marker="d",mfc="None", color="k")

ax11.plot(x3, out11 , marker="s",mfc="None", color="k")
ax11n.plot(x3, out11_, ls="--", marker="d",mfc="None", color="k")

ax12.plot(x4, out12 , marker="s",mfc="None", color="k")
ax12n.plot(x4, out12_, ls="--",marker="d", mfc="None", color="k")

ax13.plot(x2, out13 , marker="s", color="k")
ax13n.plot(x2, out13_, ls="--",marker="d",mfc="None",   color="k")

ax14.plot(x3, out14 , marker="s", color="k")
ax14n.plot(x3, out14_, ls="--",marker="d", mfc="None",  color="k")

ax15.plot(x4, out15 , marker="s", color="k")
ax15n.plot(x4, out15_, ls="--",marker="d", mfc="None",  color="k")

ax16.plot(x2, out16 , marker="s", color="k")
ax16n.plot(x2, out16_, ls="--",marker="d",mfc="None",  color="k")

ax17.plot(x3, out17 , marker="s", color="k")
ax17n.plot(x3, out17_, ls="--",marker="d",mfc="None",  color="k")

ax18.plot(x4, out18, marker="s", color="k")
ax18n.plot(x4, out18_, ls="--", marker="d", mfc="None", color="k")

ax19.plot(x2, out19, marker="s", color="k")
ax19n.plot(x2, out19_, ls="--", marker="d", mfc="None", color="k")

ax20.plot(x3, out20, marker="s", color="k")
ax20n.plot(x3, out20_, ls="--", marker="d", mfc="None", color="k")

ax21.plot(x4, out21, marker="s",  color="k")
ax21n.plot(x4, out21_, ls="--", marker="d",mfc="None", color="k")

ax22.plot(x2, out22, marker="s",  color="k")
ax22n.plot(x2, out22_, ls="--",marker="d", mfc="None", color="k")

ax23.plot(x3, out23, marker="s", color="k")
ax23n.plot(x3, out23_, ls="--",marker="d", mfc="None", color="k")

ax24.plot(x4, out24, marker="s", color="k")
ax24n.plot(x4, out24_, ls="--", marker="d",mfc="None", color="k")

ax25.plot(x2, out25, marker="s",color="k")
ax25n.plot(x2, out25_, ls="--", marker="d",mfc="None", color="k")

ax26.plot(x3, out26, marker="s", color="k")
ax26n.plot(x3, out26_, ls="--",marker="d", mfc="None", color="k")

ax27.plot(x4, out27, marker="s",color="k")
ax27n.plot(x4, out27_, ls="--", marker="d",mfc="None", color="k")

#configure axis

#123
ax1.set_ylim(0.7, 1.05)
ax2.set_ylim(0.8, 1.05)
ax3.set_ylim(0.8, 1.05)

ax1.set_yticks(np.arange(0.7, 1.05, 0.1))
ax2.set_yticks(np.arange(0.8, 1.05, 0.1))
ax3.set_yticks(np.arange(0.8, 1.05, 0.1))

#hide Y tick labels for some plots(only plots on the left and right have labels and ticklabels
##ax2.set_yticklabels([]) 
##ax3.set_yticklabels([])

ax1.set_xlim(2, 3)
ax2.set_xlim(2, 4)
ax3.set_xlim(2, 5)

ax1.set_xticks(np.arange(2, 3, 1))
ax2.set_xticks(np.arange(2, 4, 1))
ax3.set_xticks(np.arange(2, 5, 1))


ax1.set_xticklabels([])
ax2.set_xticklabels([])
ax3.set_xticklabels([])

#456
ax4.set_ylim(0.7, 1.05)
ax5.set_ylim(0.8, 1.05)
ax6.set_ylim(0.8, 1.05)

##ax4.set_yticks(np.arange(1000, 8000, 1500))
##ax5.set_yticks(np.arange(1000, 8000, 1500))
##ax6.set_yticks(np.arange(1000, 8000, 1500))

ax4.set_yticklabels([])
ax5.set_yticklabels([])
ax6.set_yticklabels([])

ax4.set_xlim(2, 3)
ax5.set_xlim(2, 4)
ax6.set_xlim(2, 5)

ax4.set_xticks(np.arange(2, 3, 1))
ax5.set_xticks(np.arange(2, 4, 1))
ax6.set_xticks(np.arange(2, 5, 1))

ax4.set_xticklabels([])
ax5.set_xticklabels([])
ax6.set_xticklabels([])

#789
ax7.set_ylim(0.7, 1.05)
ax8.set_ylim(0.8, 1.05)
ax9.set_ylim(0.8, 1.05)

##ax7.set_yticks(np.arange(500, 4000, 1000))
##ax8.set_yticks(np.arange(500, 4000, 1000))
##ax9.set_yticks(np.arange(500, 4000, 1000))

ax7.set_yticklabels([])
ax8.set_yticklabels([])
ax9.set_yticklabels([])

ax7.set_xlim(2, 3)
ax8.set_xlim(2, 4)
ax9.set_xlim(2, 5)

ax7.set_xticks(np.arange(2, 3, 1))
ax8.set_xticks(np.arange(2, 4, 1))
ax9.set_xticks(np.arange(2, 5, 1))

ax7.set_xticklabels([])
ax8.set_xticklabels([])
ax9.set_xticklabels([])

# 10, 11, 12
ax10.set_ylim(0.7, 1.05)
ax11.set_ylim(0.8, 1.05)
ax12.set_ylim(0.8, 1.05)

##ax10.set_yticks(np.arange(0, 1900, 300))
##ax11.set_yticks(np.arange(0, 1900, 300))
##ax12.set_yticks(np.arange(0, 1900, 300))

ax10.set_yticklabels([])
ax11.set_yticklabels([])
ax12.set_yticklabels([])

ax10.set_xlim(2, 3)
ax11.set_xlim(2, 4)
ax12.set_xlim(2, 5)

ax10.set_xticks(np.arange(2, 3, 1))
ax11.set_xticks(np.arange(2, 4, 1))
ax12.set_xticks(np.arange(2, 5, 1))

ax10.set_xticklabels([])
ax11.set_xticklabels([])
ax12.set_xticklabels([])

# 13, 14, 15
ax13.set_ylim(0.7, 1.05)
ax14.set_ylim(0.8, 1.05)
ax15.set_ylim(0.8, 1.05)

##ax13.set_yticks(np.arange(0, 750, 150))
##ax14.set_yticks(np.arange(0, 750, 150))
##ax15.set_yticks(np.arange(0, 750, 150))

ax13.set_yticklabels([])
ax14.set_yticklabels([])
ax15.set_yticklabels([])

ax13.set_xlim(2, 3)
ax14.set_xlim(2, 4)
ax15.set_xlim(2, 5)

ax13.set_xticks(np.arange(2, 3, 1))
ax14.set_xticks(np.arange(2, 4, 1))
ax15.set_xticks(np.arange(2, 5, 1))

ax13.set_xticklabels([])
ax14.set_xticklabels([])
ax15.set_xticklabels([])

# 16, 17, 18
ax16.set_ylim(0.7, 1.05)
ax17.set_ylim(0.8, 1.05)
ax18.set_ylim(0.8, 1.05)

##ax16.set_yticks(np.arange(0, 50, 10))
##ax17.set_yticks(np.arange(0, 50, 10))
##ax18.set_yticks(np.arange(0, 50, 10))

ax16.set_yticklabels([])
ax17.set_yticklabels([])
ax18.set_yticklabels([])

ax16.set_xlim(2, 3)
ax17.set_xlim(2, 4)
ax18.set_xlim(2, 5)

ax16.set_xticks(np.arange(2, 3, 1))
ax17.set_xticks(np.arange(2, 4, 1))
ax18.set_xticks(np.arange(2, 5, 1))

ax16.set_xticklabels([])
ax17.set_xticklabels([])
ax18.set_xticklabels([])



# 19, 20, 21
ax19.set_ylim(0.7, 1.05)
ax20.set_ylim(0.8, 1.05)
ax21.set_ylim(0.8, 1.05)

##ax16.set_yticks(np.arange(0, 50, 10))
##ax17.set_yticks(np.arange(0, 50, 10))
##ax18.set_yticks(np.arange(0, 50, 10))

ax19.set_yticklabels([])
ax20.set_yticklabels([])
ax21.set_yticklabels([])

ax19.set_xlim(2, 3)
ax20.set_xlim(2, 4)
ax21.set_xlim(2, 5)

ax19.set_xticks(np.arange(2, 3, 1))
ax20.set_xticks(np.arange(2, 4, 1))
ax21.set_xticks(np.arange(2, 5, 1))

ax19.set_xticklabels([])
ax20.set_xticklabels([])
ax21.set_xticklabels([])



# 22, 23, 24
ax22.set_ylim(0.7, 1.05)
ax23.set_ylim(0.8, 1.05)
ax24.set_ylim(0.8, 1.05)

##ax16.set_yticks(np.arange(0, 50, 10))
##ax17.set_yticks(np.arange(0, 50, 10))
##ax18.set_yticks(np.arange(0, 50, 10))

ax22.set_yticklabels([])
ax23.set_yticklabels([])
ax24.set_yticklabels([])

ax22.set_xlim(2, 3)
ax23.set_xlim(2, 4)
ax24.set_xlim(2, 5)

ax22.set_xticks(np.arange(2, 3, 1))
ax23.set_xticks(np.arange(2, 4, 1))
ax24.set_xticks(np.arange(2, 5, 1))

ax22.set_xticklabels([])
ax23.set_xticklabels([])
ax24.set_xticklabels([])


# 25, 26, 27
ax25.set_ylim(0.7, 1.05)
ax26.set_ylim(0.8, 1.05)
ax27.set_ylim(0.8, 1.05)

##ax16.set_yticks(np.arange(0, 50, 10))
##ax17.set_yticks(np.arange(0, 50, 10))
##ax18.set_yticks(np.arange(0, 50, 10))
ax25.set_yticklabels([])
ax26.set_yticklabels([])
ax27.set_yticklabels([])

ax25.set_xlim(2, 3)
ax26.set_xlim(2, 4)
ax27.set_xlim(2, 5)

ax25.set_xticks(np.arange(2, 3, 1))
ax26.set_xticks(np.arange(2, 4, 1))
ax27.set_xticks(np.arange(2, 5, 1))

ax15.set_xticklabels([])
ax16.set_xticklabels([])
ax27.set_xticklabels([])



#disable labels for some plots
##ax1n.set_yticklabels([])
##ax2n.set_yticklabels([])
##ax3n.set_yticklabels([])
##
##ax4n.set_yticklabels([])
##ax5n.set_yticklabels([])
##ax6n.set_yticklabels([])

##ax7n.set_yticklabels([])
##ax8n.set_yticklabels([])
##ax9n.set_yticklabels([])
##
##ax10n.set_yticklabels([])
##ax11n.set_yticklabels([])
##ax12n.set_yticklabels([])
##
##ax13n.set_yticklabels([])
##ax14n.set_yticklabels([])
##ax15n.set_yticklabels([])
##
##ax16n.set_yticklabels([])
##ax17n.set_yticklabels([])
##ax18n.set_yticklabels([])
##
##ax19n.set_yticklabels([])
##ax20n.set_yticklabels([])
##ax21n.set_yticklabels([])
##
##ax22n.set_yticklabels([])
##ax23n.set_yticklabels([])
##ax24n.set_yticklabels([])
##
##ax25n.set_yticklabels([])
##ax26n.set_yticklabels([])
##ax27n.set_yticklabels([])

#define the location of ticks

##ax1n.yaxis.tick_right()
##ax2n.yaxis.tick_right()
##ax3n.yaxis.tick_right()
##ax4n.yaxis.tick_right()
##ax5n.yaxis.tick_right()
##ax6n.yaxis.tick_right()
##ax7n.yaxis.tick_right()
##ax8n.yaxis.tick_right()
##ax9n.yaxis.tick_right()
##ax10n.yaxis.tick_right()
##ax11n.yaxis.tick_right()
##ax12n.yaxis.tick_right()
##ax13n.yaxis.tick_right()
##ax14n.yaxis.tick_right()
##ax15n.yaxis.tick_right()
##ax16n.yaxis.tick_right()
##ax17n.yaxis.tick_right()
##ax18n.yaxis.tick_right()

ax1.yaxis.tick_left()
ax2.yaxis.tick_left()
ax3.yaxis.tick_left()
ax4.yaxis.tick_left()
ax5.yaxis.tick_left()
ax6.yaxis.tick_left()
ax7.yaxis.tick_left()
ax8.yaxis.tick_left()
ax9.yaxis.tick_left()
ax10.yaxis.tick_left()
ax11.yaxis.tick_left()
ax12.yaxis.tick_left()
ax13.yaxis.tick_left()
ax14.yaxis.tick_left()
ax15.yaxis.tick_left()
ax16.yaxis.tick_left()
ax17.yaxis.tick_left()
ax18.yaxis.tick_left()
ax19.yaxis.tick_left()
ax20.yaxis.tick_left()
ax21.yaxis.tick_left()
ax22.yaxis.tick_left()
ax23.yaxis.tick_left()
ax24.yaxis.tick_left()
ax25.yaxis.tick_left()
ax26.yaxis.tick_left()
ax27.yaxis.tick_left()



##
##ax1n.set_ylim(-0.1,1.05)
##ax2n.set_ylim(-0.1,1.05)
##ax3n.set_ylim(-0.1,1.05)
##ax4n.set_ylim(-0.1,1.05)
##ax5n.set_ylim(-0.1,1.05)
##ax6n.set_ylim(-0.1,1.05)
##ax7n.set_ylim(-0.1,1.05)
##ax8n.set_ylim(-0.1,1.05)
##ax9n.set_ylim(-0.1,1.05)
##ax10n.set_ylim(-0.1,1.05)
##ax11n.set_ylim(-0.1,1.05)
##ax12n.set_ylim(-0.1,1.05)
##ax13n.set_ylim(-0.1,1.05)
##ax14n.set_ylim(-0.1,1.05)
##ax15n.set_ylim(-0.1,1.05)
##ax16n.set_ylim(-0.1,1.05)
##ax17n.set_ylim(-0.1,1.05)
##ax18n.set_ylim(-0.1,1.05)
##

##ax3n.yaxis.set_label_position("right")
##ax6n.yaxis.set_label_position("right")
##ax9n.yaxis.set_label_position("right")
##ax12n.yaxis.set_label_position("right")
##ax15.yaxis.set_label_position("right")
##ax18.yaxis.set_label_position("right")


#enable grid lines

##ax1.grid(True)
##ax2.grid(True)
##ax3.grid(True)
##ax4.grid(True)
##ax5.grid(True)
##ax6.grid(True)
##ax7.grid(True)
##ax8.grid(True)
##ax9.grid(True)
##ax10.grid(True)
##ax11.grid(True)
##ax12.grid(True)
##ax13.grid(True)
##ax14.grid(True)
##ax15.grid(True)
##ax16.grid(True)
##ax17.grid(True)
##ax18.grid(True)



#set Y labels
ax3.set_xlabel(r"$SUT_{1}$")
ax6.set_xlabel(r"$SUT_{2}$")
ax9.set_xlabel(r"$SUT_{3}$")
ax12.set_xlabel(r"$SUT_{4}$")
ax15.set_xlabel(r"$SUT_{5}$")
ax18.set_xlabel(r"$SUT_{6}$")
ax21.set_xlabel(r"$SUT_{7}$")
ax24.set_xlabel(r"$SUT_{8}$")
ax27.set_xlabel(r"$SUT_{9}$")
#set X labels
ax1.set_ylabel(r"$ICA(2,3)$")
ax2.set_ylabel(r"$ICA(2,4)$")
ax3.set_ylabel(r"$ICA(2,5)$")

#adjust plot spacing
plt.subplots_adjust(left=0.15, bottom=0.1, right=0.93, top=0.97, wspace=0.05, hspace=0.05)

#finally draw the plot
plt.show()
