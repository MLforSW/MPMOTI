import pandas as pd
import matplotlib.pyplot as plt

# Define the list of folder names to process
folders = ['HTPE', 'MP_DATA','nylon 11', 'nylon 12', 'Nylon 66', 'Other', 'PEG', 'PET', 'PLBH', 'PTMG']

# Define the colors for the pie charts
colors = ['#f78fa7', '#ffea00', '#e3d7ff', '#c7e0d0']  # Pink, light blue, light purple, light green

# Loop through each folder and execute the analysis
for folder in folders:
    # Paths to the datasets
    qm7_path = f'./data2/Data_2/{folder}/qm7.csv'
    lipo_path = f'./data2/Data_2/{folder}/Lipo.csv'
    esol_path = f'./data2/Data_2/{folder}/ESOL.csv'

    # Load the datasets
    qm7_df = pd.read_csv(qm7_path)
    lipo_df = pd.read_csv(lipo_path)
    esol_df = pd.read_csv(esol_path)

    # Define a function to calculate the required statistics
    def calculate_statistics(df, column):
        stats = {
            'Max': df[column].max(),
            'Min': df[column].min(),
            'Mean': df[column].mean(),
            'Median': df[column].median(),
            '25th Percentile': df[column].quantile(0.25),
            '75th Percentile': df[column].quantile(0.75)
        }
        return stats

    # Calculate statistics for the second column of each dataset
    qm7_stats = calculate_statistics(qm7_df, qm7_df.columns[1])
    lipo_stats = calculate_statistics(lipo_df, lipo_df.columns[1])
    esol_stats = calculate_statistics(esol_df, esol_df.columns[1])

    # Combine the statistics into a single DataFrame
    stats_df = pd.DataFrame({
        'QM7': qm7_stats,
        'LIPO': lipo_stats,
        'ESOL': esol_stats
    })

    # Define the output file path to save inside the corresponding folder
    output_file_path = f'./data2/Data_2/{folder}/Statistics_Summary.csv'
    stats_df.to_csv(output_file_path)