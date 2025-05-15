def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df2 = pd.read_csv("Suicide_Rates_Overview_1985_to_2016.csv")

    # Drop rows where suicide_no or population is missing or zero
    df2 = df2.dropna(subset=['suicides_no', 'population'])
    df2 = df2[(df2['population'] != 0)]

    # Convert to numeric (in case they are not)
    df2['suicides_no'] = pd.to_numeric(df2['suicides_no'], errors='coerce')
    df2['population'] = pd.to_numeric(df2['population'], errors='coerce')

    # Calculate suicide rate
    df2['suicide_rate'] = (df2['suicides_no'] / df2['population']) * 100000

    rates = df2['suicide_rate'].dropna().values

    print("Global Mean:", np.mean(rates))
    print("Max Rate:", np.max(rates))
    print("Standard Deviation:", np.std(rates))

