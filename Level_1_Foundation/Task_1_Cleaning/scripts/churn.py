import pandas as pd
import numpy as np

file_path = 'churn-bigml-80.csv'
df = pd.read_csv(file_path)

def preprocess_churn_data(df):
    print("--- Starting Preprocessing for Churn Dataset ---")
    print(f"Initial Missing values:\n{df.isnull().sum().sum()} found.\n")

    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Removing {duplicates} duplicates...")
        df = df.drop_duplicates()
    else:
        print("No duplicates detected.")
    
    df.columns = [col.lower().replace(' ', '_') for col in df.columns]
    print("Column names standardized to snake_case.")

    binary_cols = ['international_plan', 'voice_mail_plan']
    for col in binary_cols:
        if col in df.columns:
            df[col] = df[col].map({'Yes': 1, 'No': 0, 'yes': 1, 'no': 0})

    if 'churn' in df.columns:
        df['churn'] = df['churn'].astype(int)

    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        df = df[df[col] >= 0]

    print("--- Preprocessing Completed ---")
    return df

df_churn_cleaned = preprocess_churn_data(df)

output_name = 'churn_cleaned_final.csv'
df_churn_cleaned.to_csv(output_name, index=False)

print(f"\nCleaned dataset saved as: {output_name}")
print("\nFirst 5 rows of cleaned data:")
print(df_churn_cleaned.head())
print("\nData Types Summary:")
print(df_churn_cleaned.dtypes)