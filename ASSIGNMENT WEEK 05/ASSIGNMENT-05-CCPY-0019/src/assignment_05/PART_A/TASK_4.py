def main():
    import pandas as pd
    df = pd.read_csv(r"data/StudentsPerformance.csv")

    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

    df.to_csv("data/UpdatedPerformance.csv", index=False)


    print("Average score for each student:")
    print(df['average_score'])
    
    