#!/usr/bin/python3
#
# Usage: python plots-section4.3.py
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import matplotlib.gridspec as gridspec

df = pd.read_csv('plot-section4.3-Fig7.csv')
SHOW_PLOT_FLAG = True

cmap10 = plt.cm.tab10  # define the colormap
colorlist10 = [cmap10(i) for i in range(cmap10.N)]
colors = {'a': colorlist10[2], 'b': colorlist10[1], 'c': colorlist10[0],
          'tulData': '#1c747a', 'tulCtrl': '#cc8d3d',
          'tdlData': '#1c747a', 'tdlCtrl': '#7a221c',
          'tphyCtrl': '#db7461', 'tphyData': '#61c8db',
          'tulGrant': '#61db74', 'tulSR': '#7461db',
          'tul': '#fbb7b4', 'tdl': '#f5f4ed', 'tphy': '#addcd6',
          'stat': '#E95C20FF', 'walk': '#006747FF', 'drive': '#4F2C1DFF'
          }


##########################################
# Figure 7a # Best case T_UL
#########################################

fig = plt.figure(figsize=(1.8, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.1, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.set_ylabel('Density', fontsize=12)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.set_xticks([0, 1, 2, 3])
ax0.set_xlabel('$T_{UL}$ (in ms)', fontsize=12)

ax0.set_xlim([0, 3])
ax0.set_ylim([0, 5])

df = df.reset_index(drop=True)

sns.kdeplot(data=df, x='T_UL Total [ms]', linewidth=3, ax=ax0, color=colors['a'], label='a', bw_adjust=.2)

ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.3a', 'T_UL', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 7b # Breakdown of T_UL into Control and Data
#########################################

fig = plt.figure(figsize=(2.5, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.12, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)


ax0 = plt.subplot(gs1[0])

ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')

ax0.scatter(df['T_UL Total [ms]'], df['T_UL Data Plane [ms]'], s=55, marker='.', c=colors['tulData'], label='$T_{UL}^{Data}$') #,
ax0.scatter(df['T_UL Total [ms]'], df['T_UL Control Delay [ms]'], s=55, marker='4', c=colors['tulCtrl'], label='$T_{UL}^{Ctrl}$')

ax0.legend()
ax0.set_ylabel('Time (in ms)', fontsize=12)
ax0.set_xlabel('$T_{UL}$ (in ms)', fontsize=12)
ax0.set_yticks([0, 1, 2])
ax0.set_xticks([1, 1.5, 2, 2.5])


ax0.legend(ncol=2, loc='upper center', fontsize=12, handlelength=2.4, columnspacing=-0.4, bbox_to_anchor=(0.53, 1.025), borderpad=.01,
          bbox_transform=plt.gcf().transFigure)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.3b', 'T_UL_Ctrl_and_Data', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 7c # U1 vs U2
#########################################

fig = plt.figure(figsize=(1.6, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.1, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.set_ylabel('CDF', fontsize=12)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.set_yticks([0, 0.50, 1.00])
ax0.set_xticks([0, 1, 2])
ax0.set_xlabel('Time (in ms)', fontsize=12)
ax0.set_xlim([0, 2])

sns.kdeplot(df['UL Grant to Ul Data Delay  [ms]'], cumulative=True, linewidth=2, ax=ax0, color=colors['tulGrant'], label='U2', common_norm=False, bw_adjust=.2,)
sns.kdeplot(df['SR Delay [ms]'], cumulative=True, ax=ax0, linewidth=2, linestyle="--",  color=colors['tulSR'], label='U1', common_norm=False, bw_adjust=.2)

ax0.legend(loc='best',  fontsize=12, handlelength=1.3, columnspacing=-0.4,
           bbox_to_anchor=(0.5, 0.62), borderpad=.1,
          bbox_transform=plt.gcf().transFigure,)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.3c', 'T_UL_Tsr_Tgrant', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)