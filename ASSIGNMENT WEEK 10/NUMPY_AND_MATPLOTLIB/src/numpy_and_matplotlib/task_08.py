def main():
    import pandas as pd
    import numpy as np
    import matplotlib.pyplot as plt

    # Load the dataset
    df2 = pd.read_csv("Suicide_Rates_Overview_1985_to_2016.csv")

    # Ensure 'suicides_no' and 'population' are numeric
    df2['suicides_no'] = pd.to_numeric(df2['suicides_no'], errors='coerce')
    df2['population'] = pd.to_numeric(df2['population'], errors='coerce')

    # Drop rows with missing or zero population
    df2 = df2.dropna(subset=['suicides_no', 'population'])
    df2 = df2[df2['population'] != 0]

    # Calculate suicide rate
    df2['suicide_rate'] = (df2['suicides_no'] / df2['population']) * 100000

    # Filter by country
    country = "Pakistan"
    country_data = df2[df2['country'] == country]

    # Calculate average suicide rates for male and female
    male_rates = country_data[country_data['sex'] == 'male']['suicide_rate'].dropna().values
    female_rates = country_data[country_data['sex'] == 'female']['suicide_rate'].dropna().values

    print("Male Avg Suicide Rate:", np.mean(male_rates))
    print("Female Avg Suicide Rate:", np.mean(female_rates))
