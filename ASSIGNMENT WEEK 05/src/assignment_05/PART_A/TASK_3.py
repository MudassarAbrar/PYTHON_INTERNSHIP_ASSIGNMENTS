def main():
    import pandas as pd
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

  
    print("Updated column names:")
    print(df)