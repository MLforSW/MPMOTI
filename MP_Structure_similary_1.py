import pandas as pd
import os
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import numpy as np
import matplotlib.pyplot as plt

# #Morgan Fingerprints 为csv文档
# # 设定文件夹路径
# folder_path = './data2/Data_2/PTMG-1/'
#
# # 获取所有Excel文件
# file_names = [f for f in os.listdir(folder_path) if f.endswith('.csv')]
#
# # 计算行数和列数
# num_files = len(file_names)
# num_cols = 5
# num_rows = (num_files + num_cols - 1) // num_cols  # 向上取整
#
# # 创建一个大的图表
# fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 6*num_rows))
#
# # 将 axs 扁平化为1D数组，便于迭代
# axs = axs.flatten()
#
# # 遍历每个文件
# for idx, file_name in enumerate(file_names):
#     file_path = os.path.join(folder_path, file_name)
#     data = pd.read_csv(file_path)
#
#     # 将 SMILES 转换为分子指纹的函数
#     def smiles_to_fingerprint(smiles):
#         mol = Chem.MolFromSmiles(smiles)
#         if mol is not None:
#             return AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
#         else:
#             return None
#
#     # 转换所有的 SMILES 为指纹
#     fingerprints = [smiles_to_fingerprint(smile) for smile in data['smiles']]
#
#     # 移除 None 值 (无效的 SMILES)
#     valid_fingerprints = [fp for fp in fingerprints if fp is not None]
#
#     # 判断 SMILES 个数并设置采样大小
#     if len(valid_fingerprints) > 1000:
#         sample_size = 1000
#     else:
#         sample_size = 1
#
#     # 采样
#     np.random.seed(42)
#     sample_indices = np.random.choice(len(valid_fingerprints), sample_size, replace=False)
#     sampled_fingerprints = [valid_fingerprints[i] for i in sample_indices]
#
#     # 计算相似性分数
#     similarity_scores = []
#     num_compounds = len(sampled_fingerprints)
#
#     for i in range(num_compounds):
#         for j in range(i + 1, num_compounds):
#             similarity = DataStructs.FingerprintSimilarity(sampled_fingerprints[i], sampled_fingerprints[j])
#             similarity_scores.append(similarity)
#
#     # 绘制直方图
#     ax = axs[idx]
#     ax.hist(similarity_scores, bins=50, color='#ff9999', edgecolor='black')
#     title = file_name.split(' ')[0]
#     ax.set_title(f' {title} in PTMG\n(Morgan Fingerprints)', fontsize=15, fontweight='bold', fontname='Arial')
#     ax.set_xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
#     ax.set_ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
#     ax.tick_params(axis='both', which='major', labelsize=12)
#
# # 移除多余的子图
# for i in range(num_files, len(axs)):
#     fig.delaxes(axs[i])
#
# # 调整子图间距
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# plt.show()

# #Morgan Fingerprints 为xlsx文档
# # 设定文件夹路径
# import pandas as pd
# import os
# import re  # 导入正则表达式模块
# from rdkit import Chem
# from rdkit.Chem import rdMolDescriptors, DataStructs
# import numpy as np
# import matplotlib.pyplot as plt
#
# # 设定文件夹路径
# folder_path = './data2/Data_2/HTPE-2/'
#
# # 获取所有Excel文件
# file_names = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]
#
# # 计算行数和列数
# num_files = len(file_names)
# num_cols = 5
# num_rows = (num_files + num_cols - 1) // num_cols  # 向上取整
#
# # 创建一个大的图表
# fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 6 * num_rows))
#
# # 将 axs 扁平化为1D数组，便于迭代
# axs = axs.flatten()
#
#
# # 将 SMILES 转换为分子对象的函数
# def smiles_to_mol(smiles):
#     mol = Chem.MolFromSmiles(smiles)
#     return mol
#
#
# # 生成拓扑扭转指纹的函数
# def mol_to_torsion_fingerprint(mol):
#     return rdMolDescriptors.GetHashedTopologicalTorsionFingerprint(mol)
#
#
# # 遍历每个文件
# for idx, file_name in enumerate(file_names):
#     file_path = os.path.join(folder_path, file_name)
#     data = pd.read_excel(file_path)
#
#     # 转换所有的 SMILES 为分子对象
#     mols = [smiles_to_mol(smile) for smile in data['smiles']]
#
#     # 转换所有分子对象为指纹
#     fingerprints = [mol_to_torsion_fingerprint(mol) for mol in mols if mol is not None]
#
#     # 判断指纹个数并设置采样大小
#     if len(fingerprints) > 1000:
#         sample_size = 1000
#     else:
#         sample_size = 1
#
#     # 采样
#     np.random.seed(42)
#     sample_indices = np.random.choice(len(fingerprints), sample_size, replace=False)
#     sampled_fingerprints = [fingerprints[i] for i in sample_indices]
#
#     # 计算相似性分数
#     similarity_scores = []
#     num_compounds = len(sampled_fingerprints)
#
#     for i in range(num_compounds):
#         for j in range(i + 1, num_compounds):
#             similarity = DataStructs.DiceSimilarity(sampled_fingerprints[i], sampled_fingerprints[j])
#             similarity_scores.append(similarity)
#
#     # 绘制直方图
#     ax = axs[idx]
#     ax.hist(similarity_scores, bins=50, color='#89CFF0', edgecolor='black')
#
#     # 使用正则表达式提取smiles和files之间的数字
#     match = re.search(r'smiles_(\d+)_files', file_name)
#     if match:
#         title_number = match.group(1)
#     else:
#         title_number = 'Unknown'  # 如果没有匹配到，使用默认值
#
#     ax.text(0.5, 1.2, f'{title_number} common properties in HTPE', fontsize=15, fontweight='bold', fontname='Arial', ha='center',
#             va='bottom', transform=ax.transAxes)
#     ax.text(0.5, 1.1, '(Topological Torsion Fingerprints)', fontsize=12, fontweight='bold', fontname='Arial',
#             ha='center', va='bottom', transform=ax.transAxes)
#     ax.set_xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
#     ax.set_ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
#     ax.tick_params(axis='both', which='major', labelsize=12)
#
# # 移除多余的子图
# for i in range(num_files, len(axs)):
#     fig.delaxes(axs[i])
#
# # 调整子图间距
# plt.subplots_adjust(hspace=0.5, wspace=0.5)
# plt.show()


import pandas as pd
import os
import re  # 导入正则表达式模块
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import numpy as np
import matplotlib.pyplot as plt

# 设定文件夹路径
folder_path = './data2/Data_2/HTPE-2/'

# 获取所有CSV文件
file_names = [f for f in os.listdir(folder_path) if f.endswith('.xlsx')]

# 计算行数和列数
num_files = len(file_names)
num_cols = 5
num_rows = (num_files + num_cols - 1) // num_cols  # 向上取整

# 创建一个大的图表
fig, axs = plt.subplots(num_rows, num_cols, figsize=(20, 6 * num_rows))

# 将 axs 扁平化为1D数组，便于迭代
axs = axs.flatten()

# 遍历每个文件
for idx, file_name in enumerate(file_names):
    file_path = os.path.join(folder_path, file_name)
    data = pd.read_excel(file_path)


    # 将 SMILES 转换为分子指纹的函数
    def smiles_to_fingerprint(smiles):
        mol = Chem.MolFromSmiles(smiles)
        if mol is not None:
            return AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
        else:
            return None


    # 转换所有的 SMILES 为指纹
    fingerprints = [smiles_to_fingerprint(smile) for smile in data['smiles']]

    # 移除 None 值 (无效的 SMILES)
    valid_fingerprints = [fp for fp in fingerprints if fp is not None]

    # 判断 SMILES 个数并设置采样大小
    if len(valid_fingerprints) > 1000:
        sample_size = 1000
    else:
        sample_size = 1

    # 采样
    np.random.seed(42)
    sample_indices = np.random.choice(len(valid_fingerprints), sample_size, replace=False)
    sampled_fingerprints = [valid_fingerprints[i] for i in sample_indices]

    # 计算相似性分数
    similarity_scores = []
    num_compounds = len(sampled_fingerprints)

    for i in range(num_compounds):
        for j in range(i + 1, num_compounds):
            similarity = DataStructs.FingerprintSimilarity(sampled_fingerprints[i], sampled_fingerprints[j])
            similarity_scores.append(similarity)

    # 绘制直方图
    ax = axs[idx]
    ax.hist(similarity_scores, bins=50, color='#ff9999', edgecolor='black')

    # 使用正则表达式提取 smiles 和 files 之间的数字
    match = re.search(r'smiles_(\d+)_files', file_name)
    if match:
        title_number = match.group(1)
    else:
        title_number = 'Unknown'  # 如果没有匹配到，使用默认值

    # 设置标题并调整行间距
    ax.text(0.5, 1.2, f'{title_number} common properties in HTPE', fontsize=15, fontweight='bold', fontname='Arial', ha='center',
            va='bottom', transform=ax.transAxes)
    ax.text(0.5, 1.1, '(Morgan Fingerprints)', fontsize=12, fontweight='bold', fontname='Arial', ha='center',
            va='bottom', transform=ax.transAxes)
    ax.set_xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
    ax.set_ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
    ax.tick_params(axis='both', which='major', labelsize=12)

# 移除多余的子图
for i in range(num_files, len(axs)):
    fig.delaxes(axs[i])

# 调整子图间距
plt.subplots_adjust(hspace=0.5, wspace=0.5)
plt.show()
