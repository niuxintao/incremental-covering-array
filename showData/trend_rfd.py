import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co



#data
x = []
for i in range(0, 5):
    x.append(i)

data = [
[0.5595505951270747, 0.4623134980754892, 0.7377797546178948, 0.6823269249818047, 1.0, ], 
[0.9581530584598182, 0.9090909090909091, 0.604222775621356, 0.49678581719973747, 0.0, ], 
[0.18866844129997043, 0.29712896852519977, 0.3489609657906925, 0.25184081135493275, 0.9132976452980994, ], 
[0.17785999924688478, 0.17514161203341766, 0.16452178526766326, 0.13556538280690922, 0.0, ],
]


fig = plt.figure(figsize=(10, 4))

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
#fig.text(0.5, 0.04, 'Subjects', ha='center', fontsize=15)
fig.text(0.02, 0.5, 'RFD with degrees (normalized)', va='center', rotation='vertical', fontsize=15)

#plot data and normalized data
line_up, = ax[0].plot(x, data[0],  marker="o", mfc="None", color="k")
line_down, = ax1[0].plot(x, data[1], ls="--", marker="s",  mfc="None", color="k")
line_issta, = ax2[0].plot(x, data[2], ls=":", marker="x",   mfc="None", color="k")
line_haiming, = ax3[0].plot(x, data[3], ls="-.", marker="^",   mfc="None", color="k")


#configure legend

fig.legend([line_up, line_issta, line_down, line_haiming ], ['bottom-up', 'collaborative bottom-up', 'top-down',  'top-down-haiming'],'upper left',
           ncol=4,prop={'size':10})


#ax[0].set_ylabel(r"$2-way$")


labels = ['2-way','3-way', '4-way', '5-way','6-way']
x=[0,1,2,3,4]
plt.setp(ax, xticks=x,xticklabels=labels)


ax[0].set_xlim(0,4)


#adjust plot spacing
plt.subplots_adjust(left=0.08, bottom=0.11, right=0.97, top=0.9, wspace=0.25, hspace=0.55)

#finally draw the plot
plt.show()
