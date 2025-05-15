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
    plt.figure(figsize=(8, 5))
    plt.hist(df['Rating'].dropna(), bins=20, color='skyblue', edgecolor='black')
    plt.title('Distribution of App Ratings')
    plt.xlabel('Rating')
    plt.ylabel('Number of Apps')
    plt.grid(True)
    plt.show()
