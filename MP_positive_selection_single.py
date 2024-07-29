import pandas as pd
import matplotlib.pyplot as plt

# Define the list of folder names to process
folders = ['HTPE', 'MP_DATA','nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

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
    data = pd.read_csv(tox21_path)

    # 1 NR-AHR
    filtered_data = data[data['pred_2'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_2']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NR-AHR in {folder}_positive.csv', index=False)


    # 2 SR-ARE
    filtered_data = data[data['pred_7'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_7']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/SR-ARE in {folder}_positive.csv', index=False)



    # Load SIDER data for gastrointestinal disorders
    data_1 = pd.read_csv(sider_path)
    #3 GD
    filtered_data = data_1[data_1['pred_6'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_6']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/GD in {folder}_positive.csv', index=False)


    #4 vd
    filtered_data = data_1[data_1['pred_14'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_14']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/VD in {folder}_positive.csv', index=False)


    # 5 Respiratory, Thoracic and Mediastinal Disorders
    filtered_data = data_1[data_1['pred_19'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_19']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/RTMD in {folder}_positive.csv', index=False)

    # 6 Renal and Urinary Disorders
    filtered_data = data_1[data_1['pred_21'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_21']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/RUD in {folder}_positive.csv', index=False)


    # 7 Cardiac Disorders
    filtered_data = data_1[data_1['pred_24'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_24']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/CD in {folder}_positive.csv', index=False)


    # 8 Injury, Poisoning and Procedural Complications
    filtered_data = data_1[data_1['pred_26'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_26']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/IPPC in {folder}_positive.csv', index=False)

    #9 ED
    filtered_data = data_1[data_1['pred_3'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_3']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/ED in {folder}_positive.csv', index=False)


    #10 ISD
    filtered_data = data_1[data_1['pred_8'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_8']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/ISD in {folder}_positive.csv', index=False)

    # 11 GDASC
    filtered_data = data_1[data_1['pred_11'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_11']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/GDASC in {folder}_positive.csv', index=False)

    # 12 SSTD
    filtered_data = data_1[data_1['pred_16'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_16']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/SSTD in {folder}_positive.csv', index=False)


    #13  NSD
    filtered_data = data_1[data_1['pred_25'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_25']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NSD in {folder}_positive.csv', index=False)

    #14 MND
    filtered_data = data_1[data_1['pred_1'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_1']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/MND in {folder}_positive.csv', index=False)

    # 15 II
    filtered_data = data_1[data_1['pred_18'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_18']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/II in {folder}_positive.csv', index=False)


    # Load TOXCAST data for various analyses
    #16 AHGO_U
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_24'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_24']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/AHGO_U in {folder}_positive.csv', index=False)

    # 17 APR_HepG2_CellLoss_24h_dn
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_5'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_5']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/AHGC_D in {folder}_positive.csv', index=False)

    # 18 TOX21_ARE_BLA_Agonist_ch1
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_499'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_499']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/ABA_ch1 in {folder}_positive.csv', index=False)


    # 19 TOX21_ARE_BLA_Agonist_ch2 (ABA_ch2)
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_500'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_500']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/ABA_ch2 in {folder}_positive.csv', index=False)



    # 20 NEHMP1
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_367'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_367']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NEHMP1 in {folder}_positive.csv', index=False)

    # 21 NNHPR
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_467'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_467']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NNHPR in {folder}_positive.csv', index=False)


    # 22 NTG_D
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_343'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_343']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NTG_D in {folder}_positive.csv', index=False)

    # 23 NEHES
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_363'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_363']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NEHES in {folder}_positive.csv', index=False)

    # 24 NEHEL
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_364'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_364']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NEHEL in {folder}_positive.csv', index=False)


    # 25 NEHPTE
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_377'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_377']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NEHPTE in {folder}_positive.csv', index=False)



    # 26 NEHPTP
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_378'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_378']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NEHPTP in {folder}_positive.csv', index=False)


    # 27 NLH5
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_450'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_450']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NLH5 in {folder}_positive.csv', index=False)

    # 28 NGHA
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_414'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_414']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NGHA in {folder}_positive.csv', index=False)

    # 29 NNR
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_474'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_474']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NNR in {folder}_positive.csv', index=False)


    # 30 NGPHA
    data_3 = pd.read_csv(toxcast_path)
    filtered_data = data_3[data_3['pred_411'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_411']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/NGPHA in {folder}_positive.csv', index=False)



    # 31 Load TOX21 data for various analyses BBBP
    data_2 = pd.read_csv(BBBP_path)
    filtered_data = data_2[data_2['pred_0'] > 0.5]
    filtered_data = filtered_data[['smiles', 'pred_0']]
    filtered_data.to_csv(f'./data2/Data_2/{folder}/PER in {folder}_positive.csv', index=False)






