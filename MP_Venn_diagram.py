import pandas as pd
import os
import glob
from matplotlib_venn import venn2, venn3, venn3_circles
import matplotlib.pyplot as plt
from collections import defaultdict
from upsetplot import UpSet

# 获取所有以 _positive.csv 结尾的文件路径
csv_files = glob.glob('./data2/Data_2/HTPE/*_positive.csv')

# 创建一个字典来存储每个文件中的 SMILES 集合
smiles_dict = defaultdict(set)

# 读取每个 CSV 文件并填充 smiles_dict
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    filename = os.path.basename(csv_file).split(' ')[0]  # 获取文件名作为属性标签
    smiles_dict[filename] = set(df['smiles'])

# 计算每个文件的 SMILES 数量
smiles_counts = {filename: len(smiles) for filename, smiles in smiles_dict.items()}
print(smiles_counts)

# 创建一个包含所有 SMILES 的集合
all_smiles = set().union(*smiles_dict.values())

# 创建一个 DataFrame 来满足 UpSet 函数的要求
upset_data = pd.DataFrame(index=all_smiles, columns=smiles_dict.keys())

# 填充 DataFrame 中的值，使用布尔值表示每个 SMILES 是否存在于每个文件中
for label, smiles_set in smiles_dict.items():
    upset_data[label] = upset_data.index.isin(smiles_set)

# 将布尔值转换为整数值（0 和 1）
upset_data = upset_data.astype(int)

# 将 DataFrame 转换为 UpSet 格式
upset_data = upset_data.astype(bool).groupby(list(smiles_dict.keys())).size().reset_index(name='size')

# 计算每个组合的文件数量
upset_data['file_count'] = upset_data.drop(columns='size').sum(axis=1)
print(upset_data)
# Save the filtered data to a new CSV file


# 按文件数量排序，并显示特定数量的组合
desired_combinations = [25]  # 定义你想要的文件数量组合
sorted_upset_data = pd.DataFrame()

for combination in desired_combinations:
    subset = upset_data[upset_data['file_count'] == combination]
    sorted_upset_data = pd.concat([sorted_upset_data, subset])

# 如果有其他组合，你也可以选择显示
remaining_data = upset_data[~upset_data.index.isin(sorted_upset_data.index)]
sorted_upset_data = pd.concat([sorted_upset_data, remaining_data])
# 限制组合数量
n = 20  # 设置要显示的最大组合数量
sorted_upset_data = sorted_upset_data.head(n).sort_values(by='size', ascending=False)

# 设置索引并绘制 UpSet 图
sorted_upset_data = sorted_upset_data.set_index(list(smiles_dict.keys()))

# 绘制 UpSet 图，使用粉红色填充
fig = plt.figure(figsize=(12, 8))  # 设置图像尺寸
upset = UpSet(sorted_upset_data['size'], subset_size='count', show_counts=True, facecolor="pink")
upset.plot(fig=fig)
plt.show()