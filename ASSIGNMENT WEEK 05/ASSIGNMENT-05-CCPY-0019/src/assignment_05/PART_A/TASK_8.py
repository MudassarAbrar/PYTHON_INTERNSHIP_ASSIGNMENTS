def main():
    import pandas as pd
    
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    
    # calculate the average score for each student
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)

    #  group by 'parental level of education' and calculate the mean of the average_score
    grouped_avg_scores = df.groupby('parental level of education')['average_score'].mean()

    # Display the result
    print(grouped_avg_scores)