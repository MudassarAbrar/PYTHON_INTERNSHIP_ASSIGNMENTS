def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")  
    counts = df['type'].value_counts()
    plt.pie(counts, labels=counts.index, autopct='%1.1f%%')
    plt.title("Movies vs TV Shows")
    plt.show()
