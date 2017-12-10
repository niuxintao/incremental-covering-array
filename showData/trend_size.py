import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co



#data
x = []
for i in range(0, 5):
    x.append(i)

data = [
[6.33708771536425E-4, 0.1096951081637486, 0.38093856258635694, 0.2927776724109105, 0.9075944560470856, ], 
[0.08147510917813781, 0.11958722748026039, 0.10284462043527631, 0.17767644795476548, 0.0, ], 
[0.015476941058212144, 0.08837012292166027, 0.38619814731277496, 0.2774996346749365, 0.9333333333333332, ], 
[1.0, 0.8545454545454545, 0.5217391304347826, 0.5909090909090909, 0.0, ],
]


fig = plt.figure(figsize=(3, 2))

#define subplots 3x6
# 1        2    3 
# 4        5    6
# 7        8    9
# 10    11    12
# 13    14    15
# 16    17    18

ax = []
ax1 = []
ax2 = []
ax3 = []

# from degree 2 to 6
ax.append(fig.add_subplot(1, 1, 1))
ax1.append(fig.add_subplot(1, 1, 1, sharex=ax[1-1], sharey=ax[1-1], frameon=False) )
ax2.append(fig.add_subplot(1, 1, 1, sharex=ax[1-1], sharey=ax[1-1], frameon=False) )
ax3.append(fig.add_subplot(1, 1, 1, sharex=ax[1-1], sharey=ax[1-1], frameon=False) )

#fig.tight_layout()
#fig.text(0.5, 0.04, 'Summary', ha='center', fontsize=15)
#fig.text(0.02, 0.5, 'Summary', va='center', rotation='vertical', fontsize=15)

#plot data and normalized data
line_up, = ax[0].plot(x, data[0],  marker="o", mfc="None", color="k")
line_down, = ax1[0].plot(x, data[1], ls="--", marker="s",  mfc="None", color="k")
line_issta, = ax2[0].plot(x, data[2], ls=":", marker="x",   mfc="None", color="k")
line_haiming, = ax3[0].plot(x, data[3], ls="-.", marker="^",   mfc="None", color="k")


#configure legend

#fig.legend([line_up, line_issta, line_down, line_haiming ], ['bottom-up', 'collaborative bottom-up', 'top-down',  'top-down-haiming'],'upper left',
#           ncol=2,prop={'size':10})


#ax[0].set_ylabel(r"$2-way$")


labels = ['2-way','3-way', '4-way', '5-way','6-way']
x=[0,1,2,3,4]
plt.setp(ax, xticks=x,xticklabels=labels)


ax[0].set_xlim(0,4)


#adjust plot spacing
plt.subplots_adjust(left=0.15, bottom=0.17, right=0.90, top=0.90, wspace=0.25, hspace=0.55)

#finally draw the plot
plt.show()
