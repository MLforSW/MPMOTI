import pandas as pd
import os
import glob
from collections import defaultdict
'''
# 获取所有以 _positive.csv 结尾的文件路径
csv_files = glob.glob('./data2/Data_2/HTPE/*_positive.csv')

# 创建一个字典来存储每个文件中的 SMILES 集合
smiles_dict = defaultdict(set)

# 读取每个 CSV 文件并填充 smiles_dict
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    filename = os.path.basename(csv_file).split('.')[0]  # 获取文件名作为属性标签
    smiles_dict[filename] = set(df['smiles'])

# 计算每个文件的 SMILES 数量
smiles_counts = {filename: len(smiles) for filename, smiles in smiles_dict.items()}
print("每个文件的SMILES数量:", smiles_counts)

# 创建一个字典来存储每个文件中的 SMILES 集合
smiles_dict = defaultdict(set)

# 读取每个 CSV 文件并填充 smiles_dict
for csv_file in csv_files:
    df = pd.read_csv(csv_file)
    filename = os.path.basename(csv_file).split(' ')[0]  # 获取文件名作为属性标签
    smiles_dict[filename] = set(df['smiles'])

# 计算每个文件的 SMILES 数量
smiles_counts = {filename: len(smiles) for filename, smiles in smiles_dict.items()}
print("每个文件的SMILES数量:", smiles_counts)

# 计算每对文件之间的交集
intersection_counts = pd.DataFrame(index=smiles_dict.keys(), columns=smiles_dict.keys())

for file1 in smiles_dict.keys():
    for file2 in smiles_dict.keys():
        if file1 != file2:
            intersection = smiles_dict[file1] & smiles_dict[file2]
            intersection_counts.loc[file1, file2] = len(intersection)
        else:
            intersection_counts.loc[file1, file2] = smiles_counts[file1]

# 将结果保存到 Excel 文件中
output_file = 'HTPE_smiles_intersections.xlsx'
intersection_counts.to_excel(output_file)

print(f"交集结果已保存到 {output_file}")
'''
# 获取所有以 _positive.csv 结尾的文件路径
csv_files = glob.glob('./data2/Data_2/HTPE/*_positive.csv')

import pandas as pd
import os
import glob
from collections import defaultdict
import pandas as pd
import os
import glob
from collections import defaultdict

# # 获取所有以 _positive.csv 结尾的文件路径
# csv_files = glob.glob('./data2/Data_2/HTPE/*_positive.csv')
#
# # 创建一个字典来存储每个文件中的 SMILES 集合
# smiles_dict = defaultdict(set)
#
# # 读取每个 CSV 文件并填充 smiles_dict
# for csv_file in csv_files:
#     df = pd.read_csv(csv_file)
#     filename = os.path.basename(csv_file).split(' ')[0]  # 获取文件名作为属性标签
#     smiles_dict[filename] = set(df['smiles'])
#
# # 计算每个文件的 SMILES 数量
# smiles_counts = {filename: len(smiles) for filename, smiles in smiles_dict.items()}
# print("每个文件的SMILES数量:", smiles_counts)
#
# # 创建一个字典来存储 SMILES 出现的文件数和文件列表
# smiles_file_info = defaultdict(lambda: {"count": 0, "files": []})
#
# # 计算每个 SMILES 出现的文件数和文件列表
# for filename, smiles_set in smiles_dict.items():
#     for smiles in smiles_set:
#         smiles_file_info[smiles]["count"] += 1
#         smiles_file_info[smiles]["files"].append(filename)
#
# # 创建一个反向字典来按出现文件数存储 SMILES
# file_count_smiles = defaultdict(list)
# for smiles, info in smiles_file_info.items():
#     file_count_smiles[info["count"]].append((smiles, info["files"]))
#
# # 从拥有所有文件的 SMILES 开始，依次向下推
# for file_count in range(len(csv_files), 0, -1):
#     if file_count in file_count_smiles:
#         smiles_list = file_count_smiles[file_count]
#         print(f"共有{file_count}个文件的SMILES数量: {len(smiles_list)}")
#
#         # 创建 DataFrame 保存 SMILES 和对应的文件列表
#         common_smiles_df = pd.DataFrame(smiles_list, columns=['smiles', 'files'])
#         common_smiles_df['files'] = common_smiles_df['files'].apply(lambda x: ', '.join(x))  # 将文件列表转换为字符串
#
#         # 保存到 Excel 文件中
#         output_file = f'HTPE_common_smiles_{file_count}_files.xlsx'
#         common_smiles_df.to_excel(output_file, index=False)
#         print(f"共有{file_count}个文件的SMILES已保存到 {output_file}")

import pandas as pd
import os
import glob
from collections import defaultdict
import matplotlib.pyplot as plt
# Set the font to Arial

plt.rcParams['font.sans-serif'] = ['Arial']
# 定义文件夹名称
# Define the list of folder names to process
folders = ['HTPE', 'MP', 'nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

for folder in folders:
    # 获取所有以 _positive.csv 结尾的文件路径
    csv_files = glob.glob(f'./data2/Data_2/{folder}/*_positive.csv')

    # 创建一个字典来存储每个文件中的 SMILES 集合
    smiles_dict = defaultdict(set)

    # 读取每个 CSV 文件并填充 smiles_dict
    for csv_file in csv_files:
        df = pd.read_csv(csv_file)
        filename = os.path.basename(csv_file).split(' ')[0]  # 获取文件名作为属性标签
        smiles_dict[filename] = set(df['smiles'])

    # 计算每个文件的 SMILES 数量
    smiles_counts = {filename: len(smiles) for filename, smiles in smiles_dict.items()}
    print("每个文件的SMILES数量:", smiles_counts)

    # 创建一个字典来存储 SMILES 出现的文件数和文件列表
    smiles_file_info = defaultdict(lambda: {"count": 0, "files": []})

    # 计算每个 SMILES 出现的文件数和文件列表
    for filename, smiles_set in smiles_dict.items():
        for smiles in smiles_set:
            smiles_file_info[smiles]["count"] += 1
            smiles_file_info[smiles]["files"].append(filename)

    # 创建一个反向字典来按出现文件数存储 SMILES
    file_count_smiles = defaultdict(list)
    for smiles, info in smiles_file_info.items():
        file_count_smiles[info["count"]].append((smiles, info["files"]))

    # 准备绘制柱状图的数据
    file_counts = []
    smiles_numbers = []

    for file_count in range(len(csv_files), 0, -1):
        if file_count in file_count_smiles:
            smiles_list = file_count_smiles[file_count]
            file_counts.append(file_count)
            smiles_numbers.append(len(smiles_list))
            print(f"共有{file_count}个文件的SMILES数量: {len(smiles_list)}")

            # 创建 DataFrame 保存 SMILES 和对应的文件列表
            common_smiles_df = pd.DataFrame(smiles_list, columns=['smiles', 'files'])
            common_smiles_df['files'] = common_smiles_df['files'].apply(lambda x: ', '.join(x))  # 将文件列表转换为字符串

            # 保存到 Excel 文件中
            output_file = f'./data2/Data_2/{folder}/{folder}_common_smiles_{file_count}_files.xlsx'
            common_smiles_df.to_excel(output_file, index=False)
            print(f"共有{file_count}个文件的SMILES已保存到 {output_file}")

    # 创建柱状图
    fig, ax = plt.subplots(figsize=(12, 8))
    bars = ax.bar(file_counts, smiles_numbers, color='#99CCFF')

    # 设置字体大小和加粗
    ax.set_title(f'Common SMILES Counts in {folder}', fontsize=22, fontweight='bold',fontname='Arial')
    ax.set_xlabel('Number of Files', fontsize=15, fontweight='bold',fontname='Arial')
    ax.set_ylabel('Number of SMILES', fontsize=15, fontweight='bold',fontname='Arial')
    ax.tick_params(axis='both', which='major', labelsize=12)

    # 在每个柱子上方显示数字
    for bar in bars:
        yval = bar.get_height()
        ax.text(bar.get_x() + bar.get_width() / 2, yval + 1, int(yval), ha='center', fontsize=12, fontweight='bold',fontname='Arial')

    # 显示图形
    plt.xticks(ha='right', fontsize=12, fontweight='bold',fontname='Arial')
    plt.yticks(fontsize=12, fontweight='bold',fontname='Arial')
    plt.tight_layout()
    plt.savefig(f'./data2/Data_2/{folder}/Common_SMILES_Counts_{folder}.png')
    plt.show()
