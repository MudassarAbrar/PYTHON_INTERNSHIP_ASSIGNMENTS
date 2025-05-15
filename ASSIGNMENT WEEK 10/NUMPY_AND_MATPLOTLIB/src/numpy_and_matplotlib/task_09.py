def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df2 = pd.read_csv("Suicide_Rates_Overview_1985_to_2016.csv")

    # Convert to numeric
    df2['suicides_no'] = pd.to_numeric(df2['suicides_no'], errors='coerce')
    df2['population'] = pd.to_numeric(df2['population'], errors='coerce')

    # Drop missing and invalid data
    df2 = df2.dropna(subset=['suicides_no', 'population'])
    df2 = df2[df2['population'] != 0]

    # Calculate suicide rate
    df2['suicide_rate'] = (df2['suicides_no'] / df2['population']) * 100000

    # Compute average suicide rate by country and sort
    country_avg_rates = df2.groupby('country')['suicide_rate'].mean().sort_values(ascending=False).head(10)

    # Plotting
    country_avg_rates.plot(kind='bar', color='tomato')
    plt.title("Top 10 Countries by Average Suicide Rate")
    plt.ylabel("Average Suicide Rate (per 100,000)")
    plt.xlabel("Country")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
