import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as co


#data
x = []
for i in range(0, 55):
    x.append(i)

data = [
[0.98, 0.07, 0.10, 0.02, 0.00, 0.01, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.03, 0.00, 0.09, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ], 
[0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.19, 0.12, 0.00, 0.05, 0.09, 0.14, 0.00, 0.00, 0.00, 0.01, 0.11, 0.06, 0.00, 0.01, 0.15, 0.01, 0.00, 0.36, 0.97, 0.17, 0.01, 0.34, 0.21, 0.16, 0.10, 0.14, 0.71, 0.41, 0.12, 0.08, 0.36, 0.49, 1.00, 0.53, 0.27, 0.03, 0.04, 0.28, 0.25, 0.23, 0.25, 0.89, 0.90, 0.36, 0.07, 0.21, 1.00, 1.00, 0.01, ], 
[1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.38, 0.08, 0.00, 0.02, 0.53, 0.73, 0.00, 1.00, 0.60, 0.09, 0.03, 0.01, 1.00, 0.15, 0.00, 0.01, 1.00, 1.00, 0.13, 0.33, 1.00, 0.10, 1.00, 0.03, 0.04, 0.04, 0.28, 0.19, 0.20, 0.14, 0.12, 0.10, 0.17, 0.10, 0.22, 0.04, 1.00, 0.07, 0.04, 0.16, 0.26, 0.11, 0.43, 0.92, 0.75, 0.24, 0.71, 0.27, 0.03, ], 
[0.20, 0.04, 0.08, 0.02, 0.17, 0.15, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.04, 1.00, 1.00, 1.00, 1.00, 0.10, 1.00, 1.00, 1.00, 0.16, 0.94, 1.00, 1.00, 0.00, 1.00, 0.19, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.88, 1.00, 1.00, 1.00, 0.10, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.02, 0.96, 1.00, ], 
[0.08, 0.00, 0.04, 0.03, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.04, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.01, 0.00, 0.08, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.84, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, ], 
[0.00, 0.00, 0.00, 0.00, 0.07, 0.31, 0.69, 0.59, 0.08, 0.04, 0.01, 0.09, 0.01, 0.00, 0.04, 0.05, 0.04, 0.23, 0.07, 0.01, 1.00, 1.00, 0.50, 1.00, 1.00, 0.74, 0.61, 1.00, 1.00, 1.00, 0.99, 1.00, 1.00, 1.00, 0.23, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.89, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.07, 0.62, 1.00, 1.00, 0.39, ], 
[1.00, 1.00, 1.00, 1.00, 0.34, 1.00, 0.03, 0.01, 1.00, 1.00, 0.00, 0.00, 0.00, 1.00, 0.52, 0.01, 1.00, 1.00, 0.26, 0.01, 0.01, 0.00, 0.20, 0.00, 0.61, 0.02, 1.00, 0.00, 0.08, 0.00, 0.00, 0.01, 0.01, 0.01, 0.01, 0.02, 0.00, 0.00, 0.53, 0.83, 0.02, 0.02, 1.00, 0.01, 0.00, 0.01, 0.02, 0.00, 0.01, 0.04, 0.03, 0.01, 0.56, 0.01, 0.05, ], 
[0.20, 0.02, 0.13, 0.02, 1.00, 0.78, 1.00, 1.00, 0.08, 0.04, 1.00, 1.00, 1.00, 0.04, 1.00, 1.00, 0.04, 0.23, 1.00, 1.00, 0.69, 0.25, 1.00, 0.51, 1.00, 1.00, 0.03, 0.49, 0.20, 0.40, 1.00, 0.25, 0.19, 0.46, 1.00, 0.07, 0.37, 0.48, 1.00, 1.00, 0.49, 0.24, 0.63, 0.64, 0.65, 0.37, 0.66, 1.00, 0.11, 0.96, 1.00, 1.00, 1.00, 0.07, 1.00, ], 
[0.00, 0.00, 0.00, 0.01, 0.00, 0.00, 1.00, 0.00, -1.00, -1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -1.00, -1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -1.00, 0.00, 0.00, 0.12, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.03, -1.00, -1.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -1.00, 0.00, 0.00, 0.00, 0.00, -1.00, 0.00, 0.00, ], 
[0.28, 1.00, 0.13, 0.00, 0.15, 0.20, 0.50, 1.00, -1.00, -1.00, 0.18, 0.48, 0.60, 0.00, 0.26, 0.25, -1.00, -1.00, 0.52, 0.05, 0.46, 1.00, 1.00, 1.00, -1.00, 1.00, 1.00, 1.00, 1.00, 1.00, 0.87, 1.00, 1.00, 0.45, 1.00, 1.00, 1.00, 1.00, -1.00, -1.00, 0.52, 1.00, 1.00, 1.00, 1.00, 1.00, 0.56, -1.00, 1.00, 1.00, 0.07, 0.22, -1.00, 1.00, 1.00, ], 
[1.00, 0.46, 1.00, 1.00, 0.06, 0.06, 0.00, 0.72, -1.00, -1.00, 0.00, 0.00, 1.00, 1.00, 0.68, 0.01, -1.00, -1.00, 0.31, 0.00, 1.00, 0.88, 0.02, 0.01, -1.00, 0.01, 0.07, 0.00, 0.01, 0.03, 1.00, -1.00, 0.50, 1.00, 0.00, 0.84, 0.07, 0.00, -1.00, -1.00, 1.00, 0.86, 0.06, 0.54, -1.00, 0.62, 1.00, -1.00, -1.00, 0.01, 0.00, 1.00, -1.00, -1.00, 0.01, ], 
[0.96, 0.34, 0.18, 0.01, 1.00, 1.00, 0.50, 1.00, -1.00, -1.00, 1.00, 1.00, 0.60, 0.00, 1.00, 1.00, -1.00, -1.00, 1.00, 1.00, 0.46, 1.00, 0.50, 0.06, -1.00, 0.07, 0.02, 1.00, 0.03, 1.00, 0.87, 1.00, 1.00, 0.45, 0.28, 1.00, 1.00, 1.00, -1.00, -1.00, 0.52, 1.00, 0.25, 1.00, 1.00, 1.00, 0.56, -1.00, 1.00, 0.04, 1.00, 0.22, -1.00, 1.00, 0.02, ], 
[0.00, 0.00, 0.00, 0.00, 0.00, 0.00, -1.00, -1.00, -1.00, -1.00, 0.07, 0.57, -1.00, -1.00, 0.00, 1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, 0.00, 0.00, -1.00, 0.00, 0.02, -1.00, 0.23, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, -1.00, 0.00, ], 
[0.42, 1.00, 0.24, 0.01, 0.20, 0.33, -1.00, -1.00, -1.00, -1.00, 0.00, 1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, 1.00, 0.13, -1.00, -1.00, 1.00, 1.00, -1.00, 1.00, 1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, 0.34, -1.00, -1.00, -1.00, 1.00, ], 
[1.00, 0.06, 1.00, 1.00, 0.04, 0.01, -1.00, -1.00, -1.00, -1.00, 1.00, 0.00, -1.00, -1.00, 1.00, 0.33, -1.00, -1.00, 0.26, 0.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, 0.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.66, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.01, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, 0.73, ], 
[0.42, 0.21, 0.11, 0.01, 1.00, 1.00, -1.00, -1.00, -1.00, -1.00, 0.00, 1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, 0.84, 1.00, -1.00, -1.00, 0.09, 1.00, -1.00, 1.00, 0.01, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.06, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, 1.00, -1.00, -1.00, -1.00, 1.00, ], 
[-1.00, 0.00, 0.00, -1.00, 0.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.01, 0.01, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, ], 
[-1.00, 1.00, 0.04, -1.00, 0.07, 0.09, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, 0.40, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.39, -1.00, -1.00, -1.00, -1.00, ], 
[-1.00, 0.92, 1.00, -1.00, 1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, 1.00, -1.00, -1.00, 0.03, -1.00, -1.00, -1.00, 0.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.63, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, ], 
[-1.00, 1.00, 0.04, -1.00, 0.07, 0.09, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.00, 0.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, 0.40, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, -1.00, 0.39, -1.00, -1.00, -1.00, -1.00, ], 
]


fig = plt.figure(figsize=(15, 7))

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
for i in range(1, 6):
     ax.append(fig.add_subplot(5, 1, i))
     ax1.append(fig.add_subplot(5, 1, i, sharex=ax[i-1], sharey=ax[i-1], frameon=False) )
     ax2.append(fig.add_subplot(5, 1, i, sharex=ax[i-1], sharey=ax[i-1], frameon=False) )
     ax3.append(fig.add_subplot(5, 1, i, sharex=ax[i-1], sharey=ax[i-1], frameon=False) )

fig.tight_layout()
fig.text(0.5, 0.04, 'Subjects', ha='center', fontsize=15)
fig.text(0.02, 0.5, 'Time (normalized)', va='center', rotation='vertical', fontsize=15)

#plot data and normalized data
line_up, = ax[0].plot(x, data[0],  marker="o", mfc="None", color="k")
line_down, = ax1[0].plot(x, data[1], ls="--", marker="s",  mfc="None", color="k")
line_issta, = ax2[0].plot(x, data[2], ls=":", marker="x",   mfc="None", color="k")
line_haiming, = ax3[0].plot(x, data[3], ls="-.", marker="^",   mfc="None", color="k")

for i in range(1, 5):
    ax[i].plot(x, data[i*4 + 0],  marker="o", mfc="None", color="k")
    ax1[i].plot(x, data[i*4 + 1], ls="--", marker="s", mfc="None", color="k")
    ax2[i].plot(x, data[i*4 + 2], ls=":", marker="x",  mfc="None", color="k")
    ax3[i].plot(x, data[i*4 + 3], ls="-.", marker="^",   mfc="None", color="k")


#configure legend

fig.legend([line_up, line_issta, line_down, line_haiming ], ['bottom-up', 'collaborative bottom-up', 'top-down',  'top-down-hamming'],'upper left',
           ncol=4,prop={'size':10})

#fig.legend([line_up, line_issta, line_down ], ['bottom-up', 'collaborative bottom-up', 'top-down'],'upper left',
#           ncol=3,prop={'size':10})


ax[0].set_ylabel(r"$2-way$")
ax[1].set_ylabel(r"$3-way$")
ax[2].set_ylabel(r"$4-way$")
ax[3].set_ylabel(r"$5-way$")
ax[4].set_ylabel(r"$6-way$")


labels = ['1','5', '10', '15', '20', '25', '30', '35', '40', '45', '50', '55']
x=[0,4,9,14,19,24,29,34,39,44,49,54]
plt.setp(ax, xticks=x,xticklabels=labels)
plt.setp(ax1, xticks=x,xticklabels=labels)
plt.setp(ax2, xticks=x,xticklabels=labels)
plt.setp(ax3, xticks=x,xticklabels=labels)
ax[0].set_xlim(0,55)
ax[1].set_xlim(0,55)
ax[2].set_xlim(0,55)
ax[3].set_xlim(0,55)
ax[4].set_xlim(0,55)

#adjust plot spacing
plt.subplots_adjust(left=0.08, bottom=0.11, right=0.97, top=0.95, wspace=0.25, hspace=0.55)

#finally draw the plot
plt.show()
