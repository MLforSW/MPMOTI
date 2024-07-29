import os
import zipfile
import pandas as pd

# # 解压文件
# zip_file_path = './data2/Data_2/predict_Monomer.zip'
# extract_dir = './data2/Data_2/predict_Monomer'
#
# with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
#     zip_ref.extractall(extract_dir)
#
# # 定义要处理的目录和预测列名
# predictions = ['pred_2', 'pred_7', 'pred_6', 'pred_14', 'pred_19', 'pred_21', 'pred_24', 'pred_26',
#                'pred_3', 'pred_8', 'pred_11', 'pred_16', 'pred_25', 'pred_1', 'pred_18', 'pred_24',
#                'pred_5', 'pred_499', 'pred_500', 'pred_367', 'pred_467', 'pred_343', 'pred_363', 'pred_364',
#                'pred_377', 'pred_378', 'pred_450', 'pred_414', 'pred_474', 'pred_411', 'pred_0']
#
# # 遍历文件夹，处理每个CSV文件
# for root, dirs, files in os.walk(extract_dir):
#     for file in files:
#         if file.endswith('.csv'):
#             file_path = os.path.join(root, file)
#             data = pd.read_csv(file_path)
#             unique_smiles = data.iloc[:, 0].unique()
#
#             for idx, smile in enumerate(unique_smiles):
#                 smile_data = data[data.iloc[:, 0] == smile]
#
#                 # 创建文件夹
#                 output_folder = os.path.join(extract_dir, str(idx + 1))
#                 os.makedirs(output_folder, exist_ok=True)
#
#                 # 保存原始数据到对应的文件夹
#                 for column in smile_data.columns[1:]:
#                     output_file = os.path.join(output_folder, f"{column}.csv")
#                     smile_data[[data.columns[0], column]].to_csv(output_file, index=False)
#
# print("处理完成")


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import matplotlib.patches as mpatches
'''
# 读取Excel文件中的数据
file_path = './data2/Data_2/PAES.xlsx'
data = pd.read_excel(file_path)

# 根据实际列名生成数据透视表
pivot_data = data.set_index('smiles')

# 准备分子式的下标格式函数
def format_smiles(smiles):
    formatted_smiles = ""
    for char in smiles:
        if char.isdigit():
            formatted_smiles += f"$_{{\mathbf{{{char}}}}}$"
        else:
            formatted_smiles += f"$\mathbf{{{char}}}$"
    return formatted_smiles

# 定义颜色映射函数
def get_color(value):
    if value > 0.9:
        return '#ff9999'  # 马卡龙粉色
    elif value > 0.8:
        return '#99ccff'  # 马卡龙蓝色
    elif value > 0.6:
        return '#99ff99'  # 马卡龙绿色
    else:
        return '#ffff99'  # 马卡龙黄色

# 绘制空白图
fig, ax = plt.subplots(figsize=(20, 15))

# 获取最大和最小值以便标准化
vmax = pivot_data.max().max()
vmin = pivot_data.min().min()

# 添加灰色格栅线
ax.set_xticks(np.arange(pivot_data.shape[1]) + 0.5)
ax.set_yticks(np.arange(pivot_data.shape[0]) + 0.5)
ax.set_xticklabels(pivot_data.columns, rotation=90, fontsize=20, fontweight='bold')
ax.set_yticklabels([format_smiles(smile) for smile in pivot_data.index], fontsize=20, fontweight='bold')

# # 添加网格线
# ax.grid(which='both', color='gray', linestyle='-', linewidth=0.5)

# 在图上绘制球形填充
for y in range(pivot_data.shape[0]):
    for x in range(pivot_data.shape[1]):
        value = pivot_data.iloc[y, x]
        size = np.abs((value - vmin) / (vmax - vmin)) * 0.4  # 标准化球形大小
        circle_color = get_color(value)  # 根据值获取颜色
        circle = plt.Circle((x + 0.5, y + 0.5), size, color=circle_color, alpha=0.7, ec='black')
        ax.add_patch(circle)

# 去掉背景
ax.set_xlim(0, pivot_data.shape[1])
ax.set_ylim(0, pivot_data.shape[0])
ax.invert_yaxis()
ax.set_aspect('equal')

# 调整图形布局，腾出空间放置图例
plt.subplots_adjust(bottom=0.3)

# 添加自定义图例
colors = ['#ff9999', '#99ccff', '#99ff99', '#ffff99']
labels = ['> 0.9', '0.8 ~ 0.9', '0.6 ~ 0.8', '< 0.6']
patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(colors))]
legend=plt.legend(handles=patches, title='Probability value', loc='upper center', bbox_to_anchor=(0.5, -0.25), fontsize=22, title_fontsize=32, ncol=4, prop={'weight': 'bold'})
# 设置图例标题和标签的字体加粗
plt.setp(legend.get_title(), fontsize=22, fontweight='bold')
plt.setp(legend.get_texts(), fontsize=20, fontweight='bold')

plt.title('Prediction of CHO compound', fontsize=26, fontweight='bold')
plt.show()
'''




#比较不同的微塑料
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as mpatches

# 读取Excel文件中的数据
file_path = './results_3.xlsx'
data = pd.read_excel(file_path)

# 根据实际列名生成数据透视表
pivot_data = data.set_index('Items')

# 准备分子式的下标格式函数
def format_smiles(smiles):
    formatted_smiles = ""
    for char in smiles:
        if char.isdigit():
            formatted_smiles += f"$_{{\mathbf{{{char}}}}}$"
        else:
            formatted_smiles += f"$\mathbf{{{char}}}$"
    return formatted_smiles

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

# 绘制空白图
fig, ax = plt.subplots(figsize=(20, 15))

# 获取最大和最小值以便标准化
vmax = pivot_data.max().max()
vmin = pivot_data.min().min()

# 添加灰色格栅线
ax.set_xticks(np.arange(pivot_data.shape[1]) + 0.5)
ax.set_yticks(np.arange(pivot_data.shape[0]) + 0.5)
ax.set_xticklabels(pivot_data.columns, rotation=90, fontsize=15, fontweight='bold')

# ax.set_yticklabels([format_smiles(Items) for Items in pivot_data.index], fontsize=15, fontweight='bold')
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

# 去掉背景
ax.set_xlim(0, pivot_data.shape[1])
ax.set_ylim(0, pivot_data.shape[0])
ax.invert_yaxis()
ax.set_aspect('equal')

# # 调整图形布局，腾出空间放置图例
# plt.subplots_adjust(bottom=0.35)
#
# # 添加自定义图例
# colors = ['#ffff99', '#cc99ff', '#99ccff', '#99ff99', '#ffcc99', '#ff9999']
# labels = ['< 0.05', '0.05 ~ 0.3', '0.3 ~ 0.6', '0.6 ~ 0.8', '0.8 ~ 0.9', '0.9 ~ 1.0']
# patches = [mpatches.Patch(color=colors[i], label=labels[i]) for i in range(len(colors))]
# legend = plt.legend(handles=patches, title='Probability value', loc='upper center', bbox_to_anchor=(0.5, -0.3), fontsize=22, title_fontsize=32, ncol=6, prop={'weight': 'bold'})
#
# # 设置图例标题和标签的字体加粗
# plt.setp(legend.get_title(), fontsize=22, fontweight='bold')
# plt.setp(legend.get_texts(), fontsize=20, fontweight='bold')

plt.title('Comparison of MP properties', fontsize=18, fontweight='bold')
plt.show()
