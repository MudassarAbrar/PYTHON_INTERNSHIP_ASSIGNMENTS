def main():
    import pandas as pd
   
    df = pd.read_csv(r"data/UpdatedPerformance.csv")
    def grades_cal(row):
        if row['average_score'] >= 90:
            return 'A'
        elif row['average_score'] >= 80:
            return 'B'
        elif row['average_score'] >= 70:
            return 'C'
        elif row['average_score'] >= 60:
            return 'D'
        else:
            return 'F'
    df["grades"] = df.apply(grades_cal, axis=1)
    print("Grades for each student:")   
    print(df["grades"])