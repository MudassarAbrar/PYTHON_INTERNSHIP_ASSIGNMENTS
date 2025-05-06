import pandas as pd

def main():
    # Load the dataset
    df = pd.read_csv(r"data/UpdatedPerformance.csv")
    
    # Create a new DataFrame with student_id and sports_participation
    sports_data = pd.DataFrame({
        'student_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],  # Add student IDs as an example
        'sports_participation': ['yes', 'no', 'yes', 'no', 'yes', 'yes', 'no', 'yes', 'no', 'yes']
    })
    
    df['student_id'] = range(1, len(df) + 1)  # Add student_id to the original df
    
    merged_df = pd.merge(df, sports_data, on='student_id', how='inner')
    
    # Display the merged DataFrame
    print("Merged DataFrame:")
    print(merged_df)

