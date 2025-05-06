def main():
    import pandas as pd
    df = pd.read_csv(r"dataB/housing.csv")
    df_cleaned = df.drop_duplicates()
    df_cleaned.to_csv(r"dataB/housing_cleaned.csv", index=False)
    print("Duplicate values removed and saved to housing_cleaned.csv")
    print("Cleaned DataFrame:")
    print(df_cleaned)