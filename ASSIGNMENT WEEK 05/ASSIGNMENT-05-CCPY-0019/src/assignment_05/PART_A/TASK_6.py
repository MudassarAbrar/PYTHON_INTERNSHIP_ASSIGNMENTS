def main():
    import pandas as pd
   
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    std_detail =  df.loc[(df["test preparation course"]== "completed")]
    
    print("Students who completed the test preparation course:")    
    print(std_detail)