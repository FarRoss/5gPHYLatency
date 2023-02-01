#!/usr/bin/python3
#
# Usage: python plot-section6.py
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import itertools
import matplotlib.gridspec as gridspec

SHOW_PLOT_FLAG = False

c = ['#E95C20FF', '#006747FF', 'red',  'blue',  'orange', 'cyan', 'olive',  'pink', 'magenta', 'darkorange', 'm', 'darkgreen', 'dodgerblue', 'yellow',
       'magenta', 'teal', 'darkgoldenrod', 'darkolivegreen']

##########################################
# Figure 16 # Variability in T_PHY caused by mobility when UE is in CQI_High and no ReTxs
#########################################
df1 = pd.read_csv('plot-section6.1-Fig16a.csv')
df2 = pd.read_csv('plot-section6.1-Fig16b.csv')

fig = plt.figure(figsize=(6.4, 1.6))
gs1 = gridspec.GridSpec(1, 2, wspace=0.3, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)


# ======= Walking
n = 100
ax1 = plt.subplot(gs1[0])

ct = 0
order = 10
labels = []
par = 'WB CQI'
m = ['8', '*']
mt = 0


for server, tmpDF in df1.groupby('Mobility'):
    tmpDF = tmpDF.sample(n=n)
    tmpDF = tmpDF.reset_index(drop=True)
    ax1.plot(tmpDF.index.to_list(), tmpDF[par], zorder=order, label=server, c=c[ct], alpha=0.6,
             linewidth=1, marker=m[mt], markersize=6)
    mt = mt + 1
    order = order - 5
    labels.append(server)
    ct = ct + 1
ax1.set_ylabel('Time [ms]',fontsize=12)
ax1.yaxis.grid(True, which='major')
ax1.set_xlim([0, n])
ax1.set_xticks([x for x in range(0, n+1, 20)])
ax1.set_yticks([12, 13, 14, 15])
ax1.patch.set_alpha(0.3)
ax1.set_ylim([12, 15])
xmin, xmax, ymin, ymax = plt.axis()
ax1.set_xlabel('Num. of Pkts. ', fontsize=12)


ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)


ax1.set_ylabel('$CQI_{high}$', fontsize=12)
ax1.set_xlabel('Num. of Pkts.', fontsize=12)

n = 100
ct = 0
mt = 0
ax2 = plt.subplot(gs1[1])
par = 'Phy Layer Delay [ms]'

for server, tmpDF in df2.groupby('Mobility'):
    tmpDF = tmpDF.sample(n=n)
    tmpDF = tmpDF.reset_index(drop=True)
    ax2.plot(tmpDF.index.to_list(), tmpDF[par], zorder=order, label=server, c=c[ct], alpha=0.6,
             linewidth=1, marker=m[mt], markersize=5.5)
    mt = mt + 1
    order = order - 5
    labels.append(server)
    ct = ct + 1
ax2.set_ylabel('Time [ms]', fontsize=12)
ax2.yaxis.grid(True, which='major')
ax2.set_xlim([0, n])
ax2.set_xticks([x for x in range(0, n+1, 20)])
ax2.set_yticks([0, 2, 4, 6, 8])
ax2.patch.set_alpha(0.3)
ax2.set_ylim([0, 8])
xmin, xmax, ymin, ymax = plt.axis()
ax2.set_xlabel('Num. of Pkts. ', fontsize=12)

ax2.legend(ncol=2, loc='upper center', prop={'size': 11}, bbox_to_anchor=(0.59, 1.19), borderpad=.22,
          bbox_transform=plt.gcf().transFigure)

ax2.tick_params(axis='x', labelsize=12)
ax2.tick_params(axis='y', labelsize=12)
ax2.set_ylabel('$T_{Phy}$ (in ms)', fontsize=12)
ax2.set_xlabel('Num. of Pkts.', fontsize=12)

plotme(plt, '6.1', 'Fig16', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)


##########################################
# Figure 17 # Impact of mobility on MCS
#########################################
df1 = pd.read_csv('plot-section6.2-Fig17-Stat.csv')
df2 = pd.read_csv('plot-section6.2-Fig17-Walk.csv')
df3 = pd.read_csv('plot-section6.2-Fig17-Drive.csv')

fig = plt.figure(figsize=(2.1, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.07, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)

# ======= Walking
n = 100
ax1 = plt.subplot(gs1[0])
c = ['#E95C20FF', '#006747FF', '#4F2C1DFF']

ct = 0
order = 20
par = 'MCS UL'

sns.kdeplot(df1[par], linewidth=3, ax=ax1, cumulative=True, zorder=order, color=c[0], label='Stat', common_norm=False, bw_adjust=.1)
sns.kdeplot(df2[par], ax=ax1, color=c[1], linewidth=3, linestyle='-.', cumulative=True, label='Walk', common_norm=False, bw_adjust=.1)
sns.kdeplot(df3[par], ax=ax1, color=c[2], linewidth=3, linestyle='dotted', cumulative=True, label='Drive', common_norm=False, bw_adjust=.3)

ax1.set_xlim([0, 30])
ax1.set_ylabel('CDF', fontsize=12)
ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')
ax1.set_xlabel(' MCS ', fontsize=12)

ax1.legend(loc='best',  fontsize=11, handlelength=1.3, columnspacing=-0.4,
           bbox_to_anchor=(0.58, 0.63), borderpad=.01,
          bbox_transform=plt.gcf().transFigure,)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

plotme(plt, '6.2', 'Fig17', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)


##########################################
# Figure 18 # Impact of mobility of T_PHY
#########################################
df1 = pd.read_csv('plot-section6.2-Fig18-Stat.csv')
df2 = pd.read_csv('plot-section6.2-Fig18-Walk.csv')

fig = plt.figure(figsize=(2.1, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.07, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)

# ======= Walking
ax1 = plt.subplot(gs1[0])

c = ['#E95C20FF', '#006747FF', '#4F2C1DFF']
order = 30
par = 'Phy Layer Delay [ms]'

sns.kdeplot(df1[par], linewidth=1.7, ax=ax1, color=c[0], label='Stationary', common_norm=False, bw_adjust=.1)
sns.kdeplot(df2[par], ax=ax1, color=c[1], linestyle='--', linewidth=2, zorder=order, label='Walking', common_norm=False,
            bw_adjust=.1)

ax1.set_xticks([0, 1, 2, 3, 4, 5])
ax1.set_ylabel('PDF', fontsize=12)
ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')
ax1.set_xlabel('$T_{Phy}$ (in ms)', fontsize=12)

ax1.legend(loc='upper center', fontsize=11, handlelength=1.3, columnspacing=-0.4,
           bbox_to_anchor=(0.62, 1.03), borderpad=.01,
           bbox_transform=plt.gcf().transFigure)
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

plotme(plt, '6.2', 'Fig18', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

print('Stationary min', df1[par].min(), 'max', df1[par].max())
print('Walking min', df2[par].min(), 'max', df2[par].max())


##########################################
# Figure 19 # Impact of 5G -> 5G HOs on T_PHY
#########################################
df1 = pd.read_csv('plot-section6.2-Fig19-Drive.csv')
df2 = pd.read_csv('plot-section6.2-Fig19-Walk.csv')

fig = plt.figure(figsize=(2, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.07, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)

# ======= Walking
ax1 = plt.subplot(gs1[0])
order = 20
c = ['#E95C20FF', '#006747FF', '#4F2C1DFF']

sns.kdeplot(df1['T_HO'], cumulative=True, linewidth=2, linestyle='--', ax=ax1, zorder=order, color=c[2], label='Driving',
            common_norm=False, bw_adjust=.01)
sns.kdeplot(df2['T_HO'], cumulative=True, ax=ax1, color=c[1], linewidth=2, label='Walking', common_norm=False, bw_adjust=0.1)

ax1.legend(loc='best', fontsize=12, handlelength=1.3, columnspacing=-0.4,
           bbox_to_anchor=(0.4, 0.626), borderpad=.12,
           bbox_transform=plt.gcf().transFigure, )
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

ax1.set_xticks([0, 2.5, 5, 7.5, 10, 15, 20, 25, 30])
ax1.set_xlim([0, 10])

ax1.set_yticks([0, 0.25, 0.5, 0.75, 1.0])

ax1.set_ylabel('CDF', fontsize=12)
ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')
ax1.set_xlabel('$T_{Phy}^{HO}$ (in ms)', fontsize=12)

plotme(plt, '6.2', 'Fig19', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)
