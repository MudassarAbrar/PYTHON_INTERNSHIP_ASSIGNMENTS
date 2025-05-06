def main():
    import pandas as pd
    df = pd.read_csv(r"data/UpdatedPerformance.csv")
    
    
    
    top_5_scores = df.nlargest(5, 'average_score')
    
    
    print("Top 5 highest average scores:")
    print(top_5_scores)