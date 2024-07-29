import pandas as pd
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import numpy as np
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

# Load your data
data = pd.read_excel('Chemical_similarity in oligomers.xlsx')
print(data)
# data = pd.read_excel('Chemical_similarity in oligomers.xlsx')
# Function to convert SMILES to molecular fingerprint


def smiles_to_fingerprint(smiles):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        return AllChem.GetMorganFingerprintAsBitVect(mol, 2, nBits=1024)
    else:
        return None

# Convert all SMILES to fingerprints
fingerprints = [smiles_to_fingerprint(smile) for smile in data['smiles']]

# Remove None values (invalid SMILES)
valid_fingerprints = [fp for fp in fingerprints if fp is not None]


#采样
sample_size = 12  # 选择一个合理的采样大小，例如1000
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
        print(f"Similarity between molecule {i} and molecule {j}: {similarity}")


# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(similarity_scores, bins=50, color='#ff9999',edgecolor='black')
plt.title('Chemical similarity for MPs oligomers\n(Morgan Fingerprints)', fontsize=15, fontweight='bold', fontname='Arial')
plt.xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
plt.ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
plt.xticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.yticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.show()
print("================================================")
import pandas as pd
import numpy as np
from rdkit import Chem
from rdkit.Chem import AllChem, DataStructs
import matplotlib.pyplot as plt
from rdkit.Chem import rdMolDescriptors, DataStructs
# Load data
data = pd.read_excel('Chemical_similarity in oligomers.xlsx')
print(data)
# Function to convert SMILES to topological torsion fingerprint
def smiles_to_mol(smiles):
    mol = Chem.MolFromSmiles(smiles)
    return mol

def mol_to_torsion_fingerprint(mol):
    return rdMolDescriptors.GetHashedTopologicalTorsionFingerprint(mol)

# Convert all SMILES to topological torsion fingerprints
mols = [smiles_to_mol(smile) for smile in data['smiles']]
fingerprints = [mol_to_torsion_fingerprint(mol) for mol in mols if mol is not None]

# Remove None values (invalid SMILES)
valid_fingerprints = [fp for fp in fingerprints if fp is not None]

# Sampling
sample_size = 12  # 选择一个合理的采样大小，例如1000
np.random.seed(42)
sample_indices = np.random.choice(len(valid_fingerprints), sample_size, replace=False)
sampled_fingerprints = [valid_fingerprints[i] for i in sample_indices]

# 计算相似性分数并打印结果
similarity_scores = []
num_compounds = len(sampled_fingerprints)

for i in range(num_compounds):
    for j in range(i + 1, num_compounds):
        similarity = DataStructs.DiceSimilarity(sampled_fingerprints[i], sampled_fingerprints[j])
        similarity_scores.append(similarity)
        print(f"Similarity between molecule {i} and molecule {j}: {similarity}")

# 绘制直方图
plt.figure(figsize=(10, 6))
plt.hist(similarity_scores, bins=50, color='#89CFF0', edgecolor='black')
plt.title('Chemical similarity for MPs oligomers\n(Topological Torsion Fingerprints)', fontsize=15, fontweight='bold', fontname='Arial')
plt.xlabel('Similarity Values', fontsize=14, fontweight='bold', fontname='Arial')
plt.ylabel('Counts', fontsize=14, fontweight='bold', fontname='Arial')
plt.xticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.yticks(fontsize=12, fontweight='bold', fontname='Arial')
plt.show()
