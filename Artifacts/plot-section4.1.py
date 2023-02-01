#!/usr/bin/python3
#
# Usage: python plot-section4.1.py
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
# Figure 3 # Best case T_PHY
#########################################
df = pd.read_csv('plot-section4.1.csv')
fig = plt.figure(figsize=(2, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.15, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)
ax0 = plt.subplot(gs1[0])

sns.kdeplot(data=df, x='Phy Data', ax=ax0, color='#81C6E8', linewidth=2.2, common_norm=False, label='0', bw_adjust=.1)

ax0.set_xticks([0.5, 1.5, 2.5, 3.5])
ax0.set_yticks([0, 1, 2, 3])
ax0.set_ylabel('PDF', fontsize=13)
ax0.set_xlabel('$T_{Phy}$ (in ms)', fontsize=13)
ax0.tick_params(axis='x', labelsize=13)
ax0.tick_params(axis='y', labelsize=13)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')

plotme(plt, '4.1', 'Fig-3', show_flag=SHOW_PLOT_FLAG)
print('Min T_PHY = ', df['Phy Data'].min(), 'Max T_PHY = ', df['Phy Data'].max())


##########################################
# Figure 4 # Breakdown of T_PHY into Control and Data
#########################################

fig = plt.figure(figsize=(2.5, 1.4))
gs1 = gridspec.GridSpec(1, 1, wspace=0.12, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')

ax0.scatter(df['Phy Layer Delay'], df['T_Phy Data [ms]'], s=13, c=colors['tphyData'], label='$T_{Phy}^{Data}$') #,
ax0.scatter(df['Phy Layer Delay'], df['T_Phy Ctrl [ms]'], s=66, marker='4', c=colors['tphyCtrl'], label='$T_{Phy}^{Ctrl}$')

ax0.legend()
ax0.set_ylabel('Time (in ms)', fontsize=12)
ax0.set_xlabel('$T_{Phy}$ (in ms)', fontsize=12)
ax0.set_yticks([0, 1, 2, 3])
ax0.set_xticks([1, 2, 3, 4])

ax0.legend(ncol=2, loc='upper center', fontsize=12, handlelength=2.4, columnspacing=-0.4,  bbox_to_anchor=(0.53, 1.03), borderpad=.01,
          bbox_transform=plt.gcf().transFigure)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

plotme(plt, '4.1', 'Fig4', show_flag=SHOW_PLOT_FLAG)
