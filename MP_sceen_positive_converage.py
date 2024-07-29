import os
import pandas as pd

# Define the base directory containing the folders
base_dir = f'./data2/Data_2'

# Define the list of folder names to process
folders = ['HTPE', 'nylon 11', 'nylon 12',  'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

# # Store all the DataFrames that match the criteria
# data_frames = []
#
# # Iterate over each folder
# for folder in folders:
#     # folder_path = os.path.join(base_dir, folder)
#     folder_path = f'./data2/Data_2/{folder}'
#     # Iterate over all files in the current folder
#     for filename in os.listdir(folder_path):
#         if filename.endswith('_positive.csv'):
#             # Construct the full file path
#             file_path = os.path.join(folder_path, filename)
#             # Read the Excel file
#             df = pd.read_csv(file_path)
#             # Append the DataFrame to the list
#             data_frames.append(df)
#
#         # Check if there are any DataFrames to concatenate
#         # Iterate over all files in the current folder
#         for filename in os.listdir(folder_path):
#             if filename.endswith('_positive.csv'):
#                 # Construct the full file path
#                 file_path = os.path.join(folder_path, filename)
#                 # Read the CSV file
#                 df = pd.read_csv(file_path)
#                 # Append the DataFrame to the list
#                 data_frames.append(df)
#
#
#         if data_frames:
#             # Concatenate all DataFrames for the current folder
#             merged_data = pd.concat(data_frames, ignore_index=True)
#
#             # Write the merged data to a sheet in the Excel file
#             sheet_name = folder.replace(' ', '_')  # Replace spaces with underscores for sheet names
#             merged_data.to_excel(writer, sheet_name=sheet_name, index=False)
#
#             print(f"合并后的数据已保存到 Excel 文件中的 sheet: {sheet_name}")
#         else:
#             print(f"在文件夹 {folder_path} 中没有找到符合条件的文件，无法进行合并操作。")

# Define the base directory containing the folders
base_dir = './data2/Data_2'

# 定义包含文件夹的基目录
base_dir = './data2/Data_2'

# 遍历每个文件夹
for folder in folders:
    folder_path = f'./data2/Data_2/{folder}'
    if not os.path.isdir(folder_path):
        print(f"Folder {folder_path} does not exist. Skipping.")
        continue

    # 存储所有符合条件的 DataFrame
    data_frames = []

    # 遍历当前文件夹中的所有文件
    for filename in os.listdir(folder_path):
        if filename.endswith('_positive.csv'):
            # 构建文件的完整路径
            file_path = os.path.join(folder_path, filename)
            # 读取 CSV 文件
            df = pd.read_csv(file_path)
            # 将 DataFrame 添加到列表中
            data_frames.append(df)

    # 检查是否有任何 DataFrame 需要合并
    if data_frames:
        # 合并当前文件夹的所有 DataFrame
        merged_data = pd.concat(data_frames, ignore_index=True)

        # 定义输出 Excel 文件路径
        output_excel_path = os.path.join(base_dir, f'{folder}_merged_positive_data.xlsx')

        # 将合并的数据写入 Excel 文件
        with pd.ExcelWriter(output_excel_path, engine='xlsxwriter') as writer:
            sheet_name = folder.replace(' ', '_')  # 将空格替换为下划线以用作 sheet 名称
            merged_data.to_excel(writer, sheet_name=sheet_name, index=False)

        print(f"合并后的数据已保存到 Excel 文件: {output_excel_path}")
    else:
        print(f"在文件夹 {folder_path} 中没有找到符合条件的文件，无法进行合并操作。")

print("所有文件夹的处理已完成。")