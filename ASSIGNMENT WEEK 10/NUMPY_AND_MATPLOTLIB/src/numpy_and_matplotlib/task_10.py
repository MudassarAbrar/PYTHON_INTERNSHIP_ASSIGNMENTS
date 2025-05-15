def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df2 = pd.read_csv("Suicide_Rates_Overview_1985_to_2016.csv")  
    year = 2010  # Change as needed
    year_data = df2[df2['year'] == year]

    gender_sums = year_data.groupby('sex')['suicides_no'].sum()
    gender_sums.plot(kind='pie', autopct='%1.1f%%', startangle=90)
    plt.title(f"Suicide Gender Distribution ({year})")
    plt.ylabel("")
    plt.show()
