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
    type_counts = df['Type'].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(type_counts, labels=type_counts.index.str.title(), autopct='%1.1f%%', colors=['lightgreen', 'orange'], startangle=140)
    plt.title('Free vs Paid Apps')
    plt.show()
