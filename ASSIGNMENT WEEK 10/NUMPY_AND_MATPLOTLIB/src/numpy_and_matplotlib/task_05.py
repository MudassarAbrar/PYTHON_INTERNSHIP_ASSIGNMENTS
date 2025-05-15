def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")  
    top_countries = df['country'].dropna().str.split(', ', expand=True).stack().value_counts().head(10)
    top_countries.plot(kind='bar', color='skyblue')
    plt.title("Top 10 Countries by Content")
    plt.xlabel("Country")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
