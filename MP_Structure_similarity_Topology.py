import pandas as pd
from rdkit import Chem
from rdkit.Chem import rdMolDescriptors, DataStructs
import numpy as np
import matplotlib.pyplot as plt

# 加载数据
# data = pd.read_excel('/content/drive/MyDrive/MP_common_smiles_27_files.xlsx')
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

# 采样
sample_size = 1000  # 选择一个合理的采样大小，例如1000
np.random.seed(42)
sample_indices = np.random.choice(len(fingerprints), sample_size, replace=False)
sampled_fingerprints = [fingerprints[i] for i in sample_indices]

# 计算相似性分数
similarity_scores = []
num_compounds = len(sampled_fingerprints)

for i in range(num_compounds):
    for j in range(i + 1, num_compounds):
        similarity = DataStructs.DiceSimilarity(sampled_fingerprints[i], sampled_fingerprints[j])
        similarity_scores.append(similarity)

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(similarity_scores, bins=50, color='#89CFF0',edgecolor='black')
plt.title('GDASC properties in MP\n(Topological Torsion Fingerprints)', fontsize=16, fontweight='bold', fontname='Arial')
plt.xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
plt.ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
plt.xticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.yticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.show()