import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co



#data
x = []
for i in range(0, 5):
    x.append(i)

data = [
[0.02422194824170573, 0.020060184206286448, 0.02530746360809572, 0.08609621688620778, 0.10240502672251914, ], 
[0.2345590946726169, 0.6069321440975062, 0.6903628711053735, 0.6218891168320645, 0.39860602573281245, ], 
[0.39713907245287444, 0.29656544212028435, 0.42448452201368864, 0.3739290311304982, 0.7576914087107622, ], 
[0.7828512202544969, 0.5963529213229939, 0.6726046657269189, 0.5789043120737929, 0.39860602573281245, ],
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
fig.text(0.02, 0.5, 'Time with degrees (normalized)', va='center', rotation='vertical', fontsize=15)

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
