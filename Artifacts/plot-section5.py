#!/usr/bin/python3
#
# Usage: python plot-section5.py
#

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from utils import *
import itertools
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
# Figure 9 # Impact of CQI on Modulation Coding Scheme (MCS)
#########################################
df = pd.read_csv('plot-section5.1-Fig9.csv')

fig = plt.figure(figsize=(3.3, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.15, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax = plt.subplot(gs1[0])

sns.violinplot(y='MCS UL', x='WB CQI_bins', data=df, palette='coolwarm', ax=ax)
ax.set_ylim([0, 30])
ax.set_yticks([0, 5, 10, 15, 20, 25, 30])
ax.set_ylabel('MCS', fontsize=13)
ax.set_xlabel('CQI', fontsize=13)
ax.tick_params(axis='x', labelsize=13)
ax.tick_params(axis='y', labelsize=13)
ax.xaxis.grid(True, which='major')
ax.yaxis.grid(True, which='major')

plotme(plt, '5.0', 'Fig9', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)


##########################################
# Figure 10 # Impact of CQI on Number of ReTx
#########################################
d1 = pd.read_csv('plot-section5.1-Fig10-CQI-High.csv')
d2 = pd.read_csv('plot-section5.1-Fig10-CQI-Medium.csv')
d3 = pd.read_csv('plot-section5.1-Fig10-CQI-Low.csv')

fig = plt.figure(figsize=(2.5, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.15, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])
ax0.set_ylabel('CDF', fontsize=12)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.set_yticks([0, 0.25, 0.50, 0.75, 1.00])
ax0.set_xticks([0, 1, 2, 3, 4, 5])
ax0.set_xlim([0, 5])

sns.kdeplot(data=d1, x='Num ReTx UL', cumulative=True,  ax=ax0,color=colorlist10[6], label='$CQI_{high}$', common_norm=False, bw_adjust=.8)
sns.kdeplot(data=d2, x='Num ReTx UL', cumulative=True, linewidth=3, linestyle=":", ax=ax0,color=colorlist10[5], label='$CQI_{medium}$', common_norm=False, bw_adjust=.7)
sns.kdeplot(data=d3, x='Num ReTx UL', cumulative=True, linewidth=2, linestyle="--", ax=ax0,color=colorlist10[4], label='$CQI_{low}$', common_norm=False, bw_adjust=.3)

ax0.set_xlabel('Num. of ReTx', fontsize=12)
ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)
ax0.legend(loc='upper center', title='CQI Range',fontsize=9, handlelength=1.2, columnspacing=-0.4,
           bbox_to_anchor=(0.78, 0.73), borderpad=.01,
          bbox_transform=plt.gcf().transFigure)

plotme(plt, '5.0', 'Fig10', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

##########################################
# Figure 11 # 1ms T_PHY is defeated with one ReTx
#########################################
df_ZeroReTx = pd.read_csv('plot-section5.1-Fig11-No-ReTx.csv')
df_withOneReTx = pd.read_csv('plot-section5.1-Fig11-WithOne-ReTx.csv')

fig = plt.figure(figsize=(2, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.15, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)

ax0 = plt.subplot(gs1[0])

sns.kdeplot(data=df_ZeroReTx, x='Phy Data', ax=ax0, color='#81C6E8', linewidth=2.2, common_norm=False, label='0', bw_adjust=.1)
sns.kdeplot(data=df_withOneReTx, x='Phy Data', ax=ax0, color='#DB61C8', linewidth=2.2, linestyle="--", common_norm=False, label='1', bw_adjust=.15)

ax0.legend(loc='upper center', title='Num. ReTx', fontsize=12, handlelength=1.5, columnspacing=-0.4,
           bbox_to_anchor=(0.73, 1.02), borderpad=.08,
          bbox_transform=plt.gcf().transFigure)


ax0.set_xticks([0.5, 1.5, 2.5, 3.5])
ax0.set_yticks([0, 1, 2, 3])
ax0.set_ylabel('PDF', fontsize=13)
ax0.set_xlabel('$T_{Phy}$ (in ms)', fontsize=13)
ax0.tick_params(axis='x', labelsize=13)
ax0.tick_params(axis='y', labelsize=13)
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')


plotme(plt, '5.1', 'Fig11', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)

print('Min T_PHY with Zero ReTx = ', df_ZeroReTx['Phy Data'].min())
print('Min T_PHY with One ReTx = ', df_withOneReTx['Phy Data'].min())





##########################################
# Figure 13 # Impact of ReTxs on T_Ctrl_PHY and T_Data_PHY
#########################################
df = pd.read_csv('plot-section5.2-Fig13.csv')

fig = plt.figure(figsize=(3.6, 1.6))
gs1 = gridspec.GridSpec(1, 1, wspace=0.15, hspace=0.15, top=.98, bottom=0.15, left=0.1, right=0.96, figure=fig)
ax0 = plt.subplot(gs1[0])

palette = {'$T_{Phy\_Ctrl}$': colors['tphyCtrl'], '$T_{Phy\_Data}$': colors['tphyData']}

sns.barplot(x='Num ReTx', y='Delay [ms]', hue='delayType', palette=palette, data=df, ci=None, ax=ax0)

mdf = pd.melt(df, id_vars=['Num ReTx'], var_name=['delayType'])
num_locations = len(mdf['Num ReTx'].unique())
hatches = itertools.cycle(['\\', '*'])
for i, bar in enumerate(ax0.patches):
    if i % num_locations == 0:
        hatch = next(hatches)
    bar.set_hatch(hatch)

ax0.tick_params(axis='x', labelsize=12)
ax0.tick_params(axis='y', labelsize=12)
ax0.set_yticks([0, 0.5, 1, 1.5, 2])
ax0.set_ylabel('Time (in ms)', fontsize=12)
ax0.set_xlabel('Num. of ReTx', fontsize=12)

# ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.legend(ncol=3, loc='upper center', fontsize=12, handlelength=1.2, columnspacing=1, bbox_to_anchor=(0.53, 1.23),
           borderpad=.24,
           bbox_transform=plt.gcf().transFigure)
for bar in ax0.patches:
    print(bar)

plotme(plt, '5.2', 'Fig13', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)


##########################################
# Figure 14 # Impact of CQI and Num. ReTx on T_PHY
#########################################
df1 = pd.read_csv('plot-section5.2-Fig14a.csv')
df2 = pd.read_csv('plot-section5.2-Fig14b.csv')

par = 'WB CQI'
fig = plt.figure(figsize=(3.6, 1.6))
gs1 = gridspec.GridSpec(1, 2, width_ratios=[1.5, 1.5], wspace=0.05, hspace=0.08, top=.99, bottom=0.23, left=0.2,
                        right=0.99, figure=fig)

# Plotting BLER Zero
ax0 = plt.subplot(gs1[0])

ax0 = sns.boxplot(x="CQI_Range", y='Phy Layer Delay', data=df1, ax=ax0, showfliers=False, medianprops={'visible': False},
                  showmeans=True,
                  meanprops={"marker": "o",
                             "markerfacecolor": "white",
                             "markeredgecolor": "black",
                             "markersize": "5"}, width=0.3)


medians = df1.groupby(par + '_bin range')['Phy Layer Delay'].mean()
medians = medians.dropna()

for xtick in ax0.get_xticks():
    if xtick == 1:
        ax0.text(xtick-1, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))
    elif xtick == 0:
        ax0.text(xtick+2, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))


ax0.set_ylabel('$T_{Phy}$ (in ms)', fontsize=13)

ax0.set_yticks([0, 2, 4, 6, 8, 10])
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.tick_params(axis='x', labelsize=11, rotation=30)
ax0.tick_params(axis='y', labelsize=11)
ax0.set_xlabel('CQI Range', fontsize=11)
ax0.set(xticklabels=['$CQI_{low}$', '$CQI_{mediun}$', '$CQI_{high}$'])

ax1 = plt.subplot(gs1[1])
sns.boxplot(x="CQI_Range", y='Phy Layer Delay', data=df2, ax=ax1, showfliers=False, medianprops={'visible': False},
                  showmeans=True,
                  meanprops={"marker": "o",
                             "markerfacecolor": "white",
                             "markeredgecolor": "black",
                             "markersize": "5"}, width=0.3)
medians = df2.groupby([par + '_bin range'])['Phy Layer Delay'].mean()
medians = medians.dropna()

for xtick in ax1.get_xticks():
    if xtick == 1:
        ax1.text(xtick-1, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))
    elif xtick == 0:
        ax1.text(xtick+2, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))

ax1.set_ylabel('')
ax1.set_yticklabels('')
ax1.set_yticks([0, 2, 4, 6, 8, 10])

ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')
ax1.tick_params(axis='x', labelsize=11, rotation=30)
ax1.tick_params(axis='y', labelsize=11)
ax1.set_xlabel('CQI Range', fontsize=11)

ax1.set(xticklabels=['$CQI_{low}$', '$CQI_{mediun}$', '$CQI_{high}$'])

plotme(plt, '5.2', 'Fig14', show_flag=SHOW_PLOT_FLAG)
plt.close(fig)


##########################################
# Figure 15 # Impact of CQI and Num. ReTx on T_UL
#########################################
df1 = pd.read_csv('plot-section5.2-Fig15a.csv')
df2 = pd.read_csv('plot-section5.2-Fig15b.csv')

fig = plt.figure(figsize=(3.6, 1.8))
gs1 = gridspec.GridSpec(1, 2, width_ratios=[1.5, 1.5], wspace=0.05, hspace=0.08, top=.99, bottom=0.23, left=0.2,
                        right=0.99, figure=fig)

ax0 = plt.subplot(gs1[0])

ax0 = sns.boxplot(x="CQI_Range", y='T_UL Total [ms]', data=df1, showfliers=False, medianprops={'visible': False},
                  showmeans=True,
                  meanprops={"marker": "o",
                             "markerfacecolor": "white",
                             "markeredgecolor": "black",
                             "markersize": "5"}, width=0.3)
medians = df1.groupby([par + '_bin range'])['T_UL Total [ms]'].mean()
medians = medians.dropna()

for xtick in ax0.get_xticks():
    print(xtick, medians[xtick])
    if xtick == 0:
        ax0.text(xtick+2, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))
    elif xtick == 1:
        ax0.text(xtick-1, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))

ax0.set_ylabel('$T_{UL}$ (in ms)', fontsize=11)
ax0.set_yticks([0, 2, 4, 6, 8, 10])
ax0.set_ylim([0, 10])
ax0.xaxis.grid(True, which='major')
ax0.yaxis.grid(True, which='major')
ax0.tick_params(axis='x', labelsize=11, rotation=30)
ax0.tick_params(axis='y', labelsize=11)
ax0.set_xlabel('CQI Range', fontsize=11)
ax0.set(xticklabels=['$CQI_{low}$', '$CQI_{mediun}$', '$CQI_{high}$'])


ax1 = plt.subplot(gs1[1])

ax1 = sns.boxplot(x="CQI_Range", y='T_UL Total [ms]', data=df2, showfliers=False, medianprops={'visible': False},
                  showmeans=True,
                  meanprops={"marker": "o",
                             "markerfacecolor": "white",
                             "markeredgecolor": "black",
                             "markersize": "5"}, width=0.3)
medians = df2.groupby([par + '_bin range'])['T_UL Total [ms]'].mean()
medians = medians.dropna()

for xtick in ax1.get_xticks():
    print(xtick, medians[xtick])
    if xtick == 0:
        ax1.text(xtick+2, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))
    elif xtick == 1:
        ax1.text(xtick-1, medians[xtick] + 0.7, np.round(medians[xtick], decimals=2),
                 horizontalalignment='center', size='12', color='k', weight='bold',
                 bbox=dict(fc='w', ec='k', pad=2))

ax1.set_ylabel('')
ax1.set_yticklabels('')
ax1.xaxis.grid(True, which='major')
ax1.yaxis.grid(True, which='major')
ax1.tick_params(axis='x', labelsize=11, rotation=30)
ax1.tick_params(axis='y', labelsize=11)
ax1.set_xlabel('CQI Range', fontsize=11)

ax1.set_yticks([0, 2, 4, 6, 8, 10])
ax1.set_ylim([0, 10])

ax1.set(xticklabels=['$CQI_{low}$', '$CQI_{mediun}$', '$CQI_{high}$'])

plotme(plt, '5.2', 'Fig15', show_flag=SHOW_PLOT_FLAG)