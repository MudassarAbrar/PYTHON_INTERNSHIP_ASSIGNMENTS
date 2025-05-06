def main():
    import pandas as pd
    df = pd.read_csv(r"dataB/housing.csv")
    missing_values = df.isnull().sum()
    print("Missing values in each column:")
    print(missing_values)