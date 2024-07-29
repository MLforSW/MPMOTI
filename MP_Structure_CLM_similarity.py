import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors, DataStructs
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

# 加载数据
data = pd.read_csv('./data2/Data_2/MP/GDASC in MP_DATA_positive.csv')

# 将SMILES转换为分子对象
def smiles_to_mol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return mol

# 生成拓扑扭转指纹
def mol_to_torsion_fingerprint(mol):
    return rdMolDescriptors.GetHashedTopologicalTorsionFingerprint(mol)

# 转换所有SMILES为指纹
mols = [smiles_to_mol(smile) for smile in data['smiles']]
fingerprints = [mol_to_torsion_fingerprint(mol) for mol in mols if mol is not None]

# 创建网络
G = nx.Graph()

# 添加节点
for index, mol in enumerate(mols):
    if mol is not None:
        G.add_node(index, label=data['smiles'][index])

# 设置相似性阈值
threshold = 0.5

# 添加边
for i in range(len(fingerprints)):
    for j in range(i + 1, len(fingerprints)):
        if fingerprints[i] is not None and fingerprints[j] is not None:
            similarity = DataStructs.DiceSimilarity(fingerprints[i], fingerprints[j])
            if similarity >= threshold:
                G.add_edge(i, j, weight=similarity)

# 绘制网络图
pos = nx.spring_layout(G)  # 节点的布局
plt.figure(figsize=(12, 12))
nx.draw(G, pos, node_size=700, with_labels=True, node_color='skyblue', edge_color='#FF5733', linewidths=1, font_size=10)
plt.title('Chemical Similarity Network')
plt.savefig('chemical_network.png')  # 保存为PNG
plt.show()
