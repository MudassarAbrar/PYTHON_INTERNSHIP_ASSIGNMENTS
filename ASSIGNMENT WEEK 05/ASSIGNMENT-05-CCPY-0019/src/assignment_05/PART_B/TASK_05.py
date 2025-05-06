def main():
    import pandas as pd

    # Load your dataset
    df = pd.read_csv("data/StudentsPerformance.csv")

    # Calculate total rows
    total_rows = len(df)

    # Check for missing values
    missing_ratio = df.isnull().sum() / total_rows

    # Loop through each column
    for col in df.columns:
        if missing_ratio[col] > 0:
            if missing_ratio[col] < 0.05:
                # Drop rows with missing values in this column
                df = df[df[col].notnull()]
            else:
                # Fill missing values with mean (only for numeric columns)
                if df[col].dtype in ['int64', 'float64']:
                    df[col].fillna(df[col].mean(), inplace=True)
                else:
                    # Optional: fill with mode for non-numeric
                    df[col].fillna(df[col].mode()[0], inplace=True)

    # Show result
    print("Missing values handled.")
    print(df.info())
