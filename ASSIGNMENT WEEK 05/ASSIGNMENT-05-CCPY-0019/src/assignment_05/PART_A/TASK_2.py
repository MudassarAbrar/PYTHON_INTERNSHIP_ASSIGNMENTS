def main(): 
    import pandas as pd
#absolute path
#df = pd.read_csv(r"C:\Users\Mudassir\OneDrive\Desktop\ASSIGNMENT-05-CCPY-0019\Assignment_05\src\assignment_05\data\StudentsPerformance.csv")
#relative path
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    missing_values = df.isnull().sum()
    print("Missing values in each column:")
    print(missing_values)
