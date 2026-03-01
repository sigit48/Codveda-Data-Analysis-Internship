import pandas as pd
import numpy as np
df = pd.read_csv('sentiment_dataset.csv')
def preprocess_data(df):
    print("--- Starting Preprocessing ---")
    print(f"Missing values before:\n{df.isnull().sum()}\n")

    if 'Text' in df.columns:
        df['Text'] = df['Text'].fillna('No Content')
    
    if 'Likes' in df.columns:
        df['Likes'] = df['Likes'].fillna(df['Likes'].median())

    duplicate_count = df.duplicated().sum()
    print(f"Removing {duplicate_count} duplicate rows...")
    
    df = df.drop_duplicates().reset_index(drop=True)

    if 'Timestamp' in df.columns:
        df['Timestamp'] = pd.to_datetime(df['Timestamp'], errors='coerce')
    categorical_cols = df.select_dtypes(include=['object']).columns
    for col in categorical_cols:
        df[col] = df[col].str.strip().str.title() 
        
    print("--- Preprocessing Completed ---")
    return df

df_cleaned = preprocess_data(df)

df_cleaned.to_csv('sentiment_cleaned_final.csv', index=False)
print("Cleaned dataset saved as 'sentiment_cleaned_final.csv'")

print(df_cleaned.head())