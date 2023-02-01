#!/usr/bin/python3
#
# Usage: python plot-section4.2.py
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import matplotlib.gridspec as gridspec

SHOW_PLOT_FLAG = False

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
# Figure 6a # Best case T_DL
#########################################

df = pd.read_csv('plot-section4.2-Fig6a.csv')

fig = plt.figure(figsize=(1.6, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.1, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.set_ylabel('Density', fontsize=12)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.set_xticks([0, 0.2, 0.4, 0.6])
ax0.set_yticks([0, 10, 20])
ax0.set_xlabel('$T_{DL}$ (in ms)', fontsize=12)
ax0.set_xlim([0, 0.6])
sns.kdeplot(data=df, x='T_DL Total [ms]', ax=ax0, linewidth=2, color=colors['c'], label='a', common_norm=False, bw_adjust=.2)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)
print('T_DL Min', df['T_DL Total [ms]'].min(), 'T_DL Max', df['T_DL Total [ms]'].max())

plotme(plt, '4.2', 'Fig6a', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 6b # Breakdown of T_DL into Control and Data
#########################################
df = pd.read_csv('plot-section4.2-Fig6b.csv')

fig = plt.figure(figsize=(2, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.12, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)
ax0 = plt.subplot(gs1[0])
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')

ax0.scatter(df['T_DL Control Delay [ms]'], df['T_DL Data Plane [ms]'], s=12, marker='d', c=colors['tdlData'], label='$T_{DL}^{Data}$') #,
ax0.scatter(df['T_DL Control Delay [ms]'], df['T_DL Control Delay [ms]'], s=12, marker='1', c=colors['tdlCtrl'], label='$T_{DL}^{Ctrl}$')

ax0.legend()
ax0.set_ylabel('Time (in ms)', fontsize=12)
ax0.set_xlabel('$T_{DL}$ (in ms)', fontsize=12)
ax0.set_yticks([0, 0.5, 1, 1.5])
ax0.set_xticks([0, 0.5, 1, 1.5])
ax0.set_xlim([0, 1.5])

ax0.legend(ncol=2, loc='upper center', fontsize=12, handlelength=1.7, columnspacing=-0.1,
           bbox_to_anchor=(0.52, 1.02), borderpad=.01,
          bbox_transform=plt.gcf().transFigure)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.2', 'Fig6b', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 6c # Harq Delay
#########################################
df = pd.read_csv('plot-section4.2-Fig6c.csv')

fig = plt.figure(figsize=(1.3, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.1, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.set_ylabel('CDF', fontsize=12)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.set_xticks([0, 1, 2])
ax0.set_yticks([0, 0.5, 1])
ax0.set_xlabel('# of Slots', fontsize=12)
ax0.set_xlim([0, 2])

sns.kdeplot(data=df, x='DL HarqDelayWithProc [Slots]', cumulative=True, ax=ax0, linewidth=2.2, color=colors['b'], label='a', common_norm=False, bw_adjust=.2)

ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.2', 'Fig6c', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)