def main(): 
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")  

    release_years = df['release_year'].dropna().astype(int).values
    earliest = np.min(release_years)
    latest = np.max(release_years)
    most_frequent = np.bincount(release_years).argmax()

    print("Earliest Year:", earliest)
    print("Latest Year:", latest)
    print("Most Frequent Year:", most_frequent)
