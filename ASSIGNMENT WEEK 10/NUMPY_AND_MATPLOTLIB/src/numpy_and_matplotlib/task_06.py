def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")  
 
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
    yearly_adds = df['date_added'].dt.year.value_counts().sort_index()

    plt.plot(yearly_adds.index, yearly_adds.values, marker='o')
    plt.title("Total Shows Added Per Year")
    plt.xlabel("Year")
    plt.ylabel("Total Shows")
    plt.grid(True)
    plt.show()
