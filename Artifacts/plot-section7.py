#!/usr/bin/python3
#
# Usage: python plots-section7.py
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import itertools
import matplotlib.gridspec as gridspec

import sys
sys.path.append("../Data")

SHOW_PLOT_FLAG = False

cmap10 = plt.cm.tab10  # define the colormap
colorlist10 = [cmap10(i) for i in range(cmap10.N)]

colors = {'WL': colorlist10[2], 'LZ': colorlist10[1], 'RG': colorlist10[0],
          '5G_Ran': (0.8, 0.4, 0.5, 0.8), '5G_Core': (0.5, 0.5, 0.2, 0.9), 'E2E_RTT': (0.1, 0.4, 0.7, 0.8),
          'tulData': '#1c747a', 'tulCtrl': '#cc8d3d',
          'tdlData': '#1c747a', 'tdlCtrl': '#7a221c',
          'tphyCtrl': '#db7461', 'tphyData': '#61c8db',
          'tulGrant': '#61db74', 'tulSR': '#7461db',
          'tul': '#fbb7b4', 'tdl': '#f5f4ed', 'tphy': '#addcd6',
          'stat': '#E95C20FF', 'walk':'#006747FF', 'drive': '#4F2C1DFF'}

##########################################
# Figure 22 # Impact of CDRX and server placement on PHY-Layer
#########################################
df1 = pd.read_csv('plot-section7.2-Fig22a.csv')
df2 = pd.read_csv('plot-section7.2-Fig22b.csv')

fig = plt.figure(figsize=(5.5, 1.6))
gs1 = gridspec.GridSpec(1, 3, wspace=1.1, hspace=0.08, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)

ax0 = plt.subplot(gs1[0, :-1])

sns.kdeplot(df1[df1['server'] == 'WL']['PhyE2E Delay [ms]'], cumulative=True, linestyle='-.', linewidth=2.3, ax=ax0, color=colors['WL'],
            label='WL', common_norm=False, bw_adjust=.1)
sns.kdeplot(df1[df1['server'] == 'LZ']['PhyE2E Delay [ms]'], cumulative=True, linestyle=':', linewidth=3, ax=ax0, color=colors['LZ'],
            label='LZ', common_norm=False, bw_adjust=.1)
sns.kdeplot(df1[df1['server'] == 'RG']['PhyE2E Delay [ms]'], cumulative=True, linewidth=2.3, ax=ax0, color=colors['RG'], label='RG',
            common_norm=False, bw_adjust=.1)
ax0.set_yticks([0.0, 0.25, 0.5, 0.75, 1.00])
ax0.set_xticks([0, 10, 20, 30, 40, 50])
ax0.yaxis.grid(True, which='major')
ax0.xaxis.grid(True, which='major')
ax0.set_ylabel('CDF', fontsize=13)
ax0.set_xlabel('$T_{PhyRTT\_CDRX}$ (in ms)', fontsize=12)
ax0.legend(loc='best', prop={'size': 11}, bbox_to_anchor=(0.68, 0.69), borderpad=.24,
           bbox_transform=plt.gcf().transFigure)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)

myColor = [colors['LZ'], colors['RG']]

ax1 = plt.subplot(gs1[0, -1])
sns.set_palette(myColor)
sns.boxplot(x='EdgeServer', y='cdrx Overhead [ms]', palette=myColor, ax=ax1, data=df2,
            medianprops={'visible': True, 'marker': 'o', "markerfacecolor": "white", "markersize": "3"}, width=0.3)
print(ax1.artists)

ax1.set_yticks([0, 5, 10, 15, 20, 25])
ax1.yaxis.grid(True, which='major')
ax1.xaxis.grid(True, which='major')
ax1.set_ylim([0, 25])
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)
ax1.set_ylabel('$T_{CDRX\_Overhead}$ \n (in ms)', fontsize=12)
ax1.set_xlabel('EdgeServer', fontsize=12)

plotme(plt, '7.2', 'Fig22', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 24 # Impact of Payload size on T_PHY
#########################################
df = pd.read_csv('plot-section7.3-Fig24.csv')

fig = plt.figure(figsize=(2.7, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.07, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)
ax1 = plt.subplot(gs1[0])
order = 20
c = ['#E3A619', '#334162', '#4F2C1DFF']

sns.kdeplot(df[df['Payload Bytes'] == '100 bytes']['Phy Phy'], cumulative=True, linewidth=3, ax=ax1, zorder=6, color=c[0], label='100 bytes', common_norm=False, bw_adjust=.9)
sns.kdeplot(df[df['Payload Bytes'] == '1200 bytes']['Phy Phy'], cumulative=True,  ax=ax1, linestyle='--', color=c[1], zorder=18,linewidth=2, label='1200 bytes', common_norm=False, bw_adjust=.9)

ax1.legend(loc='upper center',  fontsize=12, handlelength=1, columnspacing=-0.4,
           bbox_to_anchor=(0.75, 0.57), borderpad=.01,
          bbox_transform=plt.gcf().transFigure,)
ax1.set_xlabel('$T_{Phy}$ (in ms)', fontsize=12)
ax1.set_ylabel('CDF', fontsize=12)
ax1.yaxis.grid(True, which='major')
ax1.xaxis.grid(True, which='major')
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

plotme(plt, '7.3', 'Fig24', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 25 # Payload size has little to no impact on T_PHY_Data and E2E RTT
#########################################
df = pd.read_csv('plot-section7.3-Fig25.csv')

fig = plt.figure(figsize=(4.5, 1.3))
gs1 = gridspec.GridSpec(1, 2, wspace=0.52, hspace=0.05, top=.99, bottom=0.23, left=0.2, right=0.99, figure=fig)
ax1 = plt.subplot(gs1[0])
order = 20
c = ['#E3A619', '#334162', '#4F2C1DFF']

sns.kdeplot(df[df['Payload Bytes'] == '100 bytes']['Phy DataTx'], linewidth=2, ax=ax1, zorder=4, color=c[0], label='100 bytes', common_norm=False, bw_adjust=.4)
sns.kdeplot(df[df['Payload Bytes'] == '1200 bytes']['Phy DataTx'],  ax=ax1, color=c[1], linestyle='--', linewidth=2, label='1200 bytes', common_norm=False, bw_adjust=.4)

ax1.set_xticks([0, 0.4, 0.8, 1.2])
ax1.set_xlabel('$T_{Phy}^{Data}$ (in ms)', fontsize=13)
ax1.set_ylabel('PDF', fontsize=13)
ax1.set_yticks([0, 2.5, 5])
ax1.yaxis.grid(True, which='major')
ax1.xaxis.grid(True, which='major')
ax1.tick_params(axis='x', labelsize=13)
ax1.tick_params(axis='y', labelsize=13)


# -------> Plotting E2E

ax1 = plt.subplot(gs1[1])
c = ['#E3A619', '#334162', '#4F2C1DFF']

sns.kdeplot(df[df['Payload Bytes'] == '100 bytes']['RTT [ms]'], cumulative=True,  linewidth=2, ax=ax1, zorder=6, color=c[0], label='100 bytes', common_norm=False)
sns.kdeplot(df[df['Payload Bytes'] == '1200 bytes']['RTT [ms]'],  cumulative=True, linestyle='--', ax=ax1, color=c[1], linewidth=2, label='1200 bytes', common_norm=False)

ax1.legend(ncol=2, loc='upper center',  fontsize=12, handlelength=1, columnspacing=1,
           bbox_to_anchor=(0.55, 1.23), borderpad=.01,
          bbox_transform=plt.gcf().transFigure,)
ax1.set_xticks([10, 14, 18, 22])
ax1.set_xlabel('E2E RTT (in ms)', fontsize=12)
ax1.set_ylabel('CDF', fontsize=12)
ax1.set_yticks([0, 0.5, 1])
ax1.yaxis.grid(True, which='major')
ax1.xaxis.grid(True, which='major')
ax1.tick_params(axis='x', labelsize=12)
ax1.tick_params(axis='y', labelsize=12)

plotme(plt,  '7.3', 'Fig25', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)