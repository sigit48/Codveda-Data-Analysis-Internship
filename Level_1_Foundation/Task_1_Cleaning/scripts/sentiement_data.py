import pandas as pd
import numpy as np
from typing import Tuple

INPUT_PATH = r"C:\Users\LENOVO\Documents\DATA ANALYST\Codveda\Level_1_Foundation\Data\Raw\sentiment_dataset.csv"
OUTPUT_PATH = r"C:\Users\LENOVO\Documents\DATA ANALYST\Codveda\Level_1_Foundation\Data\Processed\sentiment_cleaned_final.csv"


def load_data(path: str) -> pd.DataFrame:
    """
    Load dataset with basic validation.
    """
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Dataset is empty. Aborting pipeline.")
    return df


def data_quality_report(df: pd.DataFrame, stage: str) -> None:
    """
    Print structured data quality metrics.
    """
    print(f"\n===== DATA QUALITY REPORT ({stage}) =====")
    print(f"Shape: {df.shape}")
    print(f"Total Missing Values: {df.isnull().sum().sum()}")
    print("Missing per Column:")
    print(df.isnull().sum())
    print(f"Duplicate Rows: {df.duplicated().sum()}")
    print("=========================================\n")


def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    """
    Enforce expected data types and structure.
    """
    expected_columns = ["Text", "Likes", "Timestamp"]
    missing_columns = [col for col in expected_columns if col not in df.columns]

    if missing_columns:
        print(f"Warning: Missing expected columns: {missing_columns}")

    if "Likes" in df.columns:
        df["Likes"] = pd.to_numeric(df["Likes"], errors="coerce")

    if "Timestamp" in df.columns:
        df["Timestamp"] = pd.to_datetime(df["Timestamp"], errors="coerce")

    return df


def handle_missing_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handle missing values with controlled imputation logic.
    """
    if "Text" in df.columns:
        df["Text"] = df["Text"].fillna("No Content")

    if "Likes" in df.columns:
        median_likes = df["Likes"].median()
        df["Likes"] = df["Likes"].fillna(median_likes)

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove duplicate rows with reporting.
    """
    duplicate_count = df.duplicated().sum()
    if duplicate_count > 0:
        print(f"Removing {duplicate_count} duplicate rows.")
        df = df.drop_duplicates().reset_index(drop=True)
    else:
        print("No duplicate rows detected.")
    return df


def standardize_categorical_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardize text formatting for categorical columns.
    """
    categorical_cols = df.select_dtypes(include=["object"]).columns
    for col in categorical_cols:
        df[col] = df[col].astype(str).str.strip()
    return df


def validate_ranges(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic logical validation checks.
    """
    if "Likes" in df.columns:
        negative_likes = (df["Likes"] < 0).sum()
        if negative_likes > 0:
            print(f"Warning: {negative_likes} rows with negative Likes detected.")
    return df


def preprocess_pipeline(path: str) -> pd.DataFrame:
    """
    End-to-end preprocessing pipeline.
    """
    df = load_data(path)

    data_quality_report(df, stage="RAW")

    df = enforce_schema(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)
    df = standardize_categorical_columns(df)
    df = validate_ranges(df)

    data_quality_report(df, stage="CLEANED")

    return df


if __name__ == "__main__":
    df_cleaned = preprocess_pipeline(INPUT_PATH)
    df_cleaned.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned dataset saved to '{OUTPUT_PATH}'")