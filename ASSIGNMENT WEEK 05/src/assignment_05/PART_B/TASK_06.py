def main():
    import pandas as pd
    df = pd.read_csv(r"datab/housing.csv") 
    cleaned_df = pd.read_csv(r"dataB/housing_cleaned.csv")
    
    print("Original DataFrame:")    
    print(df)
    print("\nCleaned DataFrame:")
    print(cleaned_df)    
  