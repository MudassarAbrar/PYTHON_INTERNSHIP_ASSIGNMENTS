def main():
    import pandas as pd
    df = pd.read_csv(r"data/StudentsPerformance.csv")
    
    df['average_score'] = df[['math score', 'reading score', 'writing score']].mean(axis=1)
    
    std = df.groupby('gender')['average_score'].max()
    
    print("Maximum average score for gender groups:")
    print(std)