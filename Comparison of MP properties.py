import pandas as pd

# 定义要处理的文件夹名称列表
folders = ['HTPE', 'MP', 'nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

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


# 初始化一个字典来存储结果
results_dict = {folder: {name: 0 for _, name, _ in predictions} for folder in folders}

# 遍历每个文件夹和预测组合并执行分析
for folder in folders:
    for source, name, column in predictions:
        file_path = f'./data2/Data_2/{folder}/{source}.csv'

        try:
            data = pd.read_csv(file_path)
        except FileNotFoundError:
            continue

        categories = ['Positive' if x > 0.5 else 'Negative' for x in data[column]]
        category_counts = pd.Series(categories).value_counts()

        # 计算正向比例
        positive_proportion = category_counts.get('Positive', 0) / category_counts.sum()

        # 将结果存储在字典中
        results_dict[folder][name] = round(positive_proportion * 100, 1)  # 转换为百分比

# 将结果字典转换为DataFrame
results_df = pd.DataFrame(results_dict).T

# 保存DataFrame到Excel文件
output_path = './results_3.xlsx'
results_df.to_excel(output_path, sheet_name='MP_Properties_Comparison')

print(f"结果已保存到 {output_path}")
