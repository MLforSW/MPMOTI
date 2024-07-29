import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
import math

# 读取Excel文件中的数据
file_path = './results_3.xlsx'
data = pd.read_excel(file_path)

# 根据实际列名生成数据透视表
pivot_data = data.set_index('Items')




# 定义颜色映射函数
def get_color(value):
    if value > 0.9:
        return '#ff9999'  # 马卡龙粉色
    elif value > 0.8:
        return '#ffcc99'  # 马卡龙橙色
    elif value > 0.6:
        return '#99ff99'  # 马卡龙绿色
    elif value > 0.3:
        return '#99ccff'  # 马卡龙蓝色
    elif value > 0.05:
        return '#cc99ff'  # 马卡龙紫色
    else:
        return '#ffff99'  # 马卡龙黄色


# 定义饼图的颜色
colors = {'Positive': '#f78fa7', 'Negative': '#66ccff'}

# 定义要处理的预测列表
predictions = [
    ('TOX21', 'NR-AHR', 'pred_2'), ('TOX21', 'SR-ARE', 'pred_7'),
    ('SIDER', 'GD', 'pred_6'), ('SIDER', 'VD', 'pred_14'),
    ('SIDER', 'RTMD', 'pred_19'), ('SIDER', 'RUD', 'pred_21'),
    ('SIDER', 'CD', 'pred_24'), ('SIDER', 'IPPC', 'pred_26'),
    ('SIDER', 'ED', 'pred_3'), ('SIDER', 'ISD', 'pred_8'),
    ('SIDER', 'GDASC', 'pred_11'), ('SIDER', 'SSTD', 'pred_16'),
    ('SIDER', 'NSD', 'pred_25'), ('SIDER', 'MND', 'pred_1'),
    ('SIDER', 'II', 'pred_18'), ('TOXCAST', 'AHGO_U', 'pred_24'),
    ('TOXCAST', 'AHGC_D', 'pred_5'), ('TOXCAST', 'ABA_ch1', 'pred_499'),
    ('TOXCAST', 'ABA_ch2', 'pred_500'), ('TOXCAST', 'NEHMP1', 'pred_367'),
    ('TOXCAST', 'NNHPR', 'pred_467'), ('TOXCAST', 'NTG_D', 'pred_343'),
    ('TOXCAST', 'NEHES', 'pred_363'), ('TOXCAST', 'NEHEL', 'pred_364'),
    ('TOXCAST', 'NEHPTE', 'pred_377'), ('TOXCAST', 'NEHPTP', 'pred_378'),
    ('TOXCAST', 'NLH5', 'pred_450'), ('TOXCAST', 'NGHA', 'pred_414'),
    ('TOXCAST', 'NNR', 'pred_474'), ('TOXCAST', 'NGPHA', 'pred_411'),
    ('BBBP', 'PER', 'pred_0')
]

# 创建空白图
fig, ax = plt.subplots(figsize=(20, 15))

# 获取最大和最小值以便标准化
vmax = pivot_data.max().max()
vmin = pivot_data.min().min()

# 添加灰色格栅线
ax.set_xticks(np.arange(pivot_data.shape[1]) + 0.5)
ax.set_yticks(np.arange(pivot_data.shape[0]) + 0.5)
ax.set_xticklabels(pivot_data.columns, rotation=90, fontsize=15, fontweight='bold')
ax.set_yticklabels([Items for Items in pivot_data.index], fontsize=15, fontweight='bold')

# 在图上绘制球形填充
for y in range(pivot_data.shape[0]):
    for x in range(pivot_data.shape[1]):
        value = pivot_data.iloc[y, x]
        size = np.abs((value - vmin) / (vmax - vmin)) * 0.4  # 标准化球形大小
        circle_color = get_color(value)  # 根据值获取颜色
        circle = plt.Circle((x + 0.5, y + 0.5), size, color=circle_color, alpha=0.7, edgecolor=None)
        ax.add_patch(circle)
        # 显示数值，保留两位小数
        ax.text(x + 0.5, y + 0.5, f'{value:.2f}', ha='center', va='center', fontsize=10, fontweight='bold')

# 计算并绘制每个指标的饼状图
for i, (source, name, column) in enumerate(predictions):
    file_path = f'./data2/Data_2/MP/{source}.csv'

    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        continue

    if column not in data.columns:
        continue

    categories = ['Positive' if x > 0.5 else 'Negative' for x in data[column]]
    category_counts = pd.Series(categories).value_counts()

    # 计算饼图的位置
    col_idx = pivot_data.columns.get_loc(name)
    ax_pie = fig.add_axes(
        [0.125 + col_idx * 0.775 / len(pivot_data.columns), 0.9, 0.775 / len(pivot_data.columns), 0.1], aspect='equal')
    ax_pie.pie(category_counts, labels=['Positive', 'Negative'], colors=[colors['Positive'], colors['Negative']],
               autopct='%1.1f%%', startangle=140, textprops={'fontsize': 10, 'fontweight': 'bold'})
    ax_pie.set_title(f'({name})', fontsize=10, fontweight='bold')

# 去掉背景
ax.set_xlim(0, pivot_data.shape[1])
ax.set_ylim(-2, pivot_data.shape[0])
ax.invert_yaxis()
ax.set_aspect('equal')

plt.title('Comparison of MP properties', fontsize=18, fontweight='bold')
plt.show()
