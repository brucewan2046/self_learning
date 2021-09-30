import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

sns.set_style('white')
#显示中文
plt.rcParams['font.sans-serif'] = ['SimHei'] 
#设置图标标题
ax.set_title(f'{p_class}平台{product}产品激活趋势')
#设置坐标间隔数
tick_spacing=4
ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
#plt.figure(figsize=(15,10))
#将x轴刻度放置在top位置的几种方法
#ax.xaxis.set_ticks_position('top')  
#设置坐标轴刻度的字体大小
ax.tick_params(axis='y',labelsize=8) 
# 旋转轴刻度上文字方向的两种方法
#ax.set_yticklabels(ax.get_yticklabels(), rotation=60)


g = sns.lineplot(
data = gra_data[(gra_data['class'].isin(p_class)) & (gra_data['level4']==product)],
x = "7D_G", y="user_qty", hue="user_type", style="user_type",
markers = True, dashes=False,ax=ax)
g.set_xlabel('周数', fontweight ='bold')
g.set_ylabel('用户数', fontweight ='bold')
#设置横轴与纵轴显示
#g.set_xticklabels(labels=gra_data['7D_G'].unique(),rotation=90,horizontalalignment='center')
#g.set_yticklabels(labels=[100,500,1000,10000])
plt.subplots_adjust(wspace=0.6, hspace=0.6, left=0.1, bottom=0.22, right=0.96, top=0.96)
plt.subplot_tool()

#消除报错glyph 8722 missing
plt.rc('axes', unicode_minus=False)
#设置x轴从0开始
#plt.minorticks_on()
plt.margins(x=0)
#调整组合图上下间距
plt.tight_layout(pad=2)
#Y轴初始为0


plt.gca().set_ylim(bottom=0)
plt.xticks(rotation=90)
figpath = file_path + '/' + f'各平台{product_list[i]}产品用户激活趋势对比图'
plt.savefig(figpath,dpi=400)

#增加顶部坐标轴
ax_top = ax.twiny()
ax.axvline(6, linestyle='--', color='red')
xticks = ax.get_xticks()
ax.set_xticks(xticks)

xlim = ax.get_xlim()
ax_top.set_xlim(xlim)

top_tick = [6,10,15]
top_label = ['key','best','lowest']
ax_top.set_xticks(top_tick)
ax_top.set_xticklabels(top_label,rotation=90)




#整合多个subplots
import matplotlib.pyplot as plt

fig, axs = plt.subplots(ncols=3, nrows=3)
gs = axs[1, 2].get_gridspec()
# remove the underlying axes
for ax in axs[1:, -1]:
    ax.remove()
axbig = fig.add_subplot(gs[1:, -1])
axbig.annotate('Big Axes \nGridSpec[1:, -1]', (0.1, 0.5),
               xycoords='axes fraction', va='center')

fig.tight_layout()

plt.show()
