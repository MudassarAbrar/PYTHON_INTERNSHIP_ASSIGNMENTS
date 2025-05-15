def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    df = pd.read_csv("Neflix_Movies_and_TVShows.csv")
    tv_shows = df[df['type'] == 'TV Show'].copy()
    tv_shows['date_added'] = pd.to_datetime(tv_shows['date_added'], errors='coerce')
    years = tv_shows['date_added'].dt.year
    filtered_years = years[(years >= 2015) & (years <= 2020)]
    print("TV Shows added (2015–2020):", filtered_years.count())
