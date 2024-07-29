import pandas as pd

# Define the list of folder names to process
folders = ['HTPE', 'MP_DATA','nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

# Define the colors for the pie charts
colors = ['#f78fa7', '#ffea00', '#e3d7ff', '#c7e0d0']  # Pink, light blue, light purple, light green

# Loop through each folder and execute the analysis
for folder in folders:
    # Load the datasets using proper string formatting
    qm7_path = f'./data2/Data_2/{folder}/qm7.csv'
    lipo_path = f'./data2/Data_2/{folder}/Lipo.csv'
    esol_path = f'./data2/Data_2/{folder}/ESOL.csv'

    qm7_df = pd.read_csv(qm7_path)
    lipo_df = pd.read_csv(lipo_path)
    esol_df = pd.read_csv(esol_path)

    print(qm7_df.head())