def main():
    import pandas as  pd
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    
    std = df.loc[(df.gender == "female") & (df["math score"] >85)]
    
    print("Students who are female and scored more than 85 in math:")       
    print(std)