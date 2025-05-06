def main():
    import pandas as pd
    df = pd.read_csv(r"dataB/housing.csv")
    df.duplicated =df[ df.duplicated()]
    # df.duplicated finds duplicate in form of true and false df[df.duplicated()] will give the duplicate rows
    
    print("Duplicate values in the dataset:")
    print(df.duplicated)