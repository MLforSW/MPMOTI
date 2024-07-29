import pandas as pd
import matplotlib.pyplot as plt

# Define the list of folder names to process
folders = ['HTPE', 'MP_DATA', 'nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

# Define the colors for the pie charts
colors = ['#f78fa7', '#ffea00', '#e3d7ff', '#c7e0d0']  # Pink, light blue, light purple, light green

# Loop through each folder and execute the analysis
for folder in folders:
    # Adjust file paths to include the current folder
    BBBP_path = f'./data2/Data_2/{folder}/BBBP.csv'
    tox21_path = f'./data2/Data_2/{folder}/TOX21.csv'
    sider_path = f'./data2/Data_2/{folder}/SIDER.csv'
    toxcast_path = f'./data2/Data_2/{folder}/TOXCAST.csv'

    # Load TOX21 data for various analyses
    data_2 = pd.read_csv(BBBP_path)
    # Filter the data based on the 'pred_8' column
    filtered_data = data_2[data_2['pred_0'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data[['smiles', 'pred_0']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/Permeability in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}")

    # Load TOX21 data for various analyses
    data = pd.read_csv(tox21_path)
    # Filter the data based on the 'pred_8' column
    filtered_data = data[data['pred_2'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data[['smiles', 'pred_2']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NR-AHR in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}")

    # SR-ARE
    filtered_data_1 = data[data['pred_7'] > 0.5]
    # Select only the 'smiles' and 'pred_8' columns
    filtered_data_1 = filtered_data_1[['smiles', 'pred_7']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/SR-ARE in {folder}_positive.csv'
    filtered_data_1.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_SR-ARE")


    # Load SIDER data for gastrointestinal disorders
    data_1 = pd.read_csv(sider_path)

    filtered_data_3 = data_1[data_1['pred_6'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_3[['smiles', 'pred_6']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/GD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_GD")
    #

    #vd
    filtered_data_4 = data_1[data_1['pred_14'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_4[['smiles', 'pred_6']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/VD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_VD")



    # 20 Respiratory, Thoracic and Mediastinal Disorders

    filtered_data_5 = data_1[data_1['pred_19'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_5[['smiles', 'pred_19']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/RTMD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_RTMD")


    # 22 Renal and Urinary Disorders
    filtered_data_6 = data_1[data_1['pred_21'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_6[['smiles', 'pred_21']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/RUD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_RUD")

    # 25 Cardiac Disorders
    filtered_data_7 = data_1[data_1['pred_24'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_7[['smiles', 'pred_24']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/CD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_CD")

    # 27 Injury, Poisoning and Procedural Complications
    filtered_data_8 = data_1[data_1['pred_26'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_26']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/IPPC in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_IPPC")

    # 3 ED
    filtered_data_8 = data_1[data_1['pred_3'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_3']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/ED in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_ED")

    # 3 ED
    filtered_data_8 = data_1[data_1['pred_3'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_3']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/ED in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_ED")

    # 3 ISD
    filtered_data_8 = data_1[data_1['pred_8'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_8']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/ISD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_ISD")

    # 3 GDASC
    filtered_data_8 = data_1[data_1['pred_11'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_11']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/GDASC in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_GDASC")

    # 6 SSTD
    filtered_data_8 = data_1[data_1['pred_16'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_16']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/SSTD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_SSTD")

    # 7 NSD
    filtered_data_8 = data_1[data_1['pred_25'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_16']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NSD in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NSD")

    # 1 MND
    filtered_data_8 = data_1[data_1['pred_1'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_1']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/MND in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_MND")

    # 1 II
    filtered_data_8 = data_1[data_1['pred_18'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_8[['smiles', 'pred_18']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/II in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_II")

    # Load TOXCAST data for various analyses
    data_3 = pd.read_csv(toxcast_path)

    filtered_data_9 = data_3[data_3['pred_24'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_9[['smiles', 'pred_24']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/AHGO_U in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_AHGO_U")


    # 2 APR_HepG2_CellLoss_24h_dn
    data_3 = pd.read_csv(toxcast_path)

    filtered_data_10 = data_3[data_3['pred_5'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_10[['smiles', 'pred_5']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/AHGO_D in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_AHGO_D")

    # 2 TOX21_ARE_BLA_Agonist_ch1
    categories = ['Positive' if x > 0.5 else 'Negative' for x in data_3['pred_499']]
    filtered_data_11 = data_3[data_3['pred_499'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_499']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/ABA_ch1 in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_ABA_ch1")



    # 2 TOX21_ARE_BLA_Agonist_ch2 (ABA_ch2)

    filtered_data_11 = data_3[data_3['pred_500'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_500']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/ABA_ch2 in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_ABA_ch2")

    # 3 NEHMP1

    filtered_data_11 = data_3[data_3['pred_347'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_347']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NEHMP1 in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NEHMP1")

    # 4 NNHPR
    filtered_data_11 = data_3[data_3['pred_467'] > 0.5]
    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_467']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NNHPR in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NNHPR")

    # 5 NTG_D

    filtered_data_11 = data_3[data_3['pred_343'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_343']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NTG_D in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NTG_D")

    # 6 NEHES

    filtered_data_11 = data_3[data_3['pred_363'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_363']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NEHES in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NEHES")

    # 7 NEHEL

    filtered_data_11 = data_3[data_3['pred_364'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_364']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NEHEL in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NEHEL")

    # 8 NEHPTE

    filtered_data_11 = data_3[data_3['pred_377'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_377']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NEHPTE in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NEHPTE")

    # 8 NEHPTE

    filtered_data_11 = data_3[data_3['pred_378'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_378']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NEHPTP in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NEHPTP")

    # 9 NLH5

    filtered_data_11 = data_3[data_3['pred_450'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_450']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NLH5 in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NLH5")

    # 11 NGHA

    filtered_data_11 = data_3[data_3['pred_414'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_414']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NGHA in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NGHA")

    # 12 NNR

    filtered_data_11 = data_3[data_3['pred_474'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_474']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NNR in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NNR")

    # 13 NNR

    filtered_data_11 = data_3[data_3['pred_411'] > 0.5]

    # Select only the 'smiles' and 'pred_8' columns
    filtered_data = filtered_data_11[['smiles', 'pred_411']]

    # Save the filtered data to a new CSV file
    output_path = f'./data2/Data_2/{folder}/NGPHA in {folder}_positive.csv'
    filtered_data.to_csv(output_path, index=False)

    print(f"Filtered data saved to {output_path}_NGPHA")










