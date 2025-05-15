def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load dataset
    df = pd.read_csv("Goggle_PlayStore_Apps.csv")  # Adjust filename if needed

    # Convert columns to appropriate types
    df['Rating'] = pd.to_numeric(df['Rating'], errors='coerce')
    df['Installs'] = df['Installs'].str.replace(r'[+,]', '', regex=True)
    df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')
    df['Type'] = df['Type'].str.strip().str.lower()  # 'Free' or 'Paid'
    free_apps = df[df['Type'] == 'free']
    free_installs = free_apps['Installs'].dropna().values
    avg_free_installs = np.mean(free_installs)
    print("Average installs for free apps:", int(avg_free_installs))

