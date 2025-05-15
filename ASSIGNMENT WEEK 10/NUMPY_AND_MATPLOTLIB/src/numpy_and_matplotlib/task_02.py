def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")  

    movies = df[df['type'] == 'Movie']
    durations = movies['duration'].str.extract(r'(\d+)').dropna().astype(int).values.flatten()


    long_movies_count = np.sum(durations > 90)
    print("Movies longer than 90 minutes:", long_movies_count)
