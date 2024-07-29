
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# # Load the new Excel file to check its contents
# new_file_path = 'final_merged_data.csv'
# new_data = pd.read_csv(new_file_path)
#
# # Display the first few rows and the structure of the dataset
# new_data.head(), new_data.info()
# # Count the occurrences of each class
# class_counts = new_data['Class_y'].value_counts()
# # Plotting the bar chart
# plt.figure(figsize=(10, 6))
# bars = class_counts.plot(kind='bar', color='skyblue')
# plt.title('Count of Labels in the Class Column of MP dataset')
# plt.xlabel('Class')
# plt.ylabel('Counts')
# plt.xticks(rotation=45)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
#
# # Adding text labels on top of the bars
# for bar in bars.patches:
#     plt.annotate(format(bar.get_height(), '.0f'),
#                  (bar.get_x() + bar.get_width() / 2,
#                   bar.get_height()), ha='center', va='center',
#                  size=10, xytext=(0, 8),
#                  textcoords='offset points')
#
# plt.tight_layout()
# plt.show()
# # Creating a box plot for molecular weights by class again
# plt.figure(figsize=(12, 8))
# sns.boxplot(x='Class_y', y='MolecularWeight', data=new_data)
# plt.title('Distribution of Molecular Weights by Class of MP dataset')
# plt.xlabel('Class')
# plt.ylabel('Molecular Weight')
# plt.xticks(rotation=20)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.show()

import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem
#import umap
import matplotlib.pyplot as plt
import numpy as np

# # 载入数据
# data = pd.read_csv('final_merged_data.csv')
#
# # 从 SMILES 生成指纹
# def smiles_to_fingerprints(smiles, radius=2, n_bits=1024):
#     mol = Chem.MolFromSmiles(smiles)
#     if mol:
#         return AllChem.GetMorganFingerprintAsBitVect(mol, radius, n_bits)
#     else:
#         return np.zeros((n_bits,))
#
# # 应用函数
# data['fingerprints'] = data['smiles'].apply(lambda x: smiles_to_fingerprints(x))
#
# # 转换为适合 UMAP 的格式
# fp_matrix = np.array(list(data['fingerprints']))
#
# # 运行 UMAP
# reducer = umap.UMAP()
# embedding = reducer.fit_transform(fp_matrix)
#
# # 可视化
# plt.figure(figsize=(10, 8))
# scatter = plt.scatter(embedding[:, 0], embedding[:, 1], c=data['Class_y'].astype('category').cat.codes, cmap='viridis')
# plt.colorbar(scatter)
# plt.title('UMAP projection of Molecular Fingerprints from MP dataset')
# plt.xlabel('UMAP 1')
# plt.ylabel('UMAP 2')
# plt.show()
# Clean up the mp_data dataframe by removing unnecessary columns

# mp_data_path = 'predict_Q9_HTPE.csv'
# data = pd.read_csv(mp_data_path)

import matplotlib.pyplot as plt

# # Count the number of occurrences of each class
# class_counts = data['Class'].value_counts()
# print(class_counts)
#
# # Visualizing the counts using a bar plot
# plt.figure(figsize=(10, 6))
# class_counts.plot(kind='bar')
# plt.title('Number of Entries per Class')
# plt.xlabel('Class')
# plt.ylabel('Count')
# plt.xticks(rotation=45)
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.show()
import seaborn as sns
import matplotlib.pyplot as plt
'''
# Set the aesthetic style of the plots
sns.set(style="whitegrid")

# Create a figure to hold the plots
plt.figure(figsize=(12, 8))

# Iterate over each column to create a violin plot
for i, column in enumerate(data.columns):
    plt.subplot(1, len(data.columns), i + 1)
    sns.violinplot(y=data[column])
    plt.title(column)

# Set the aesthetic style of the plots with bold font settings for all text
sns.set(style="whitegrid", rc={"axes.edgecolor": "pink", "axes.linewidth": 2.5,
                              "axes.labelweight": "bold", "axes.titleweight": "bold",
                              "font.family": "Arial", "axes.labelsize": "x-large",
                              "xtick.labelsize": "large", "ytick.labelsize": "large",
                              "xtick.major.size": 5, "xtick.minor.size": 3,
                              "ytick.major.size": 5, "ytick.minor.size": 3,
                              "xtick.major.width": 1.5, "ytick.minor.width": 1,
                              "ytick.major.width": 1.5, "ytick.minor.width": 1})

# Create a new figure to hold the updated plots with bold text for all elements
plt.figure(figsize=(12, 8))

# Iterate over each column to create an updated violin plot
for i, column in enumerate(data.columns):
    plt.subplot(1, len(data.columns), i + 1)
    sns.violinplot(y=data[column], color="pink")
    plt.title(column, fontsize=25)
    plt.ylabel("Distribution of Value")

# Adjust layout to prevent overlap
plt.tight_layout()

# # Show the updated plot
plt.show()

#直方图

# Load the newly uploaded data from 'predict.csv'
predict_data_path = 'predict_PTMG.csv'
predict_data = pd.read_csv(predict_data_path)

# Display the first few rows of the dataset to understand its structure
predict_data.head()
# Set the aesthetic style of the plots
# sns.set(style="whitegrid", rc={"font.family": "Arial"})
# Set the aesthetic style of the plots with bold font settings for all text
sns.set(style="whitegrid", rc={"axes.edgecolor": "pink", "axes.linewidth": 2.5,
                              "axes.labelweight": "bold", "axes.titleweight": "bold",
                              "font.family": "Arial", "axes.labelsize": "x-large",
                              "xtick.labelsize": "large", "ytick.labelsize": "large",
                              "xtick.major.size": 5, "xtick.minor.size": 3,
                              "ytick.major.size": 5, "ytick.minor.size": 3,
                              "xtick.major.width": 1.5, "ytick.minor.width": 1,
                              "ytick.major.width": 1.5, "ytick.minor.width": 1})
# Create the histogram for the second column 'Nylon_66_QM7'

# Adjust the histogram to display counts and rename axis labels accordingly
plt.figure(figsize=(10, 6))
sns.histplot(predict_data['pred_0'], kde=True, color="#aaf0d1", stat="count")
plt.title('PTMG_QM7')  # Setting the title as the column name
plt.ylabel('Count')  # Setting the Y-axis label to 'Count'
plt.xlabel('Distribution of Value')  # Setting the X-axis label to 'Distribution of Value'
plt.show()

'''
'''
import pandas as pd
import matplotlib.pyplot as plt

# 加载数据
file_path = 'predict_8_66.csv'  # 更新为正确的文件路径
data = pd.read_csv(file_path)

# 设置图形和轴
fig, axes = plt.subplots(nrows=3, ncols=4, figsize=(15, 20))
axes = axes.flatten()

# 绘制每个数值列的直方图
for i, column in enumerate(data.columns[1:]):  # 从1开始以跳过'smiles'列
    data[column].hist(ax=axes[i], bins=30, color='#8fd9a8', alpha=0.7)
    axes[i].set_title(column, fontweight='bold', fontsize=24)
    axes[i].set_xlabel('Value', fontsize=20)
    axes[i].set_ylabel('Frequency', fontsize=20)
    for label in (axes[i].get_xticklabels() + axes[i].get_yticklabels()):
        label.set_fontsize(15)
        label.set_fontweight('bold')

# 调整布局防止重叠
plt.tight_layout()
plt.show()
'''

import pandas as pd

# Load the CSV file
file_path = 'predict_MP.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
data.head(), data.columns

import matplotlib.pyplot as plt

# Categorize data based on the 'pred_1' column
categories = ['Positive' if x > 0.5 else 'Negative' for x in data['pred_1']]
category_counts = pd.Series(categories).value_counts()

# Define pastel colors typically associated with macarons
colors = ['#f78fa7', '#ffea00', '#e3d7ff', '#c7e0d0']  # Pink, light blue, light purple, light green

# Plot pie chart with macaron colors
plt.figure(figsize=(8, 6))
plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%', startangle=140, colors=colors,
        textprops={'fontsize': 14, 'fontweight': 'bold'})
plt.title('Proportion of toxicity in MP', fontsize=16, fontweight='bold' )
plt.show()

