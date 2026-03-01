import pandas as pd
import numpy as np
from typing import List

INPUT_PATH = r"C:\Users\LENOVO\Documents\DATA ANALYST\Codveda\Level_1_Foundation\Data\Raw\churn-bigml-80.csv"
OUTPUT_PATH = r"C:\Users\LENOVO\Documents\DATA ANALYST\Codveda\Level_1_Foundation\Data\Processed\churn_cleaned_final.csv"


def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    if df.empty:
        raise ValueError("Dataset is empty. Pipeline aborted.")
    return df


def data_quality_report(df: pd.DataFrame, stage: str) -> None:
    print(f"\n===== DATA QUALITY REPORT ({stage}) =====")
    print(f"Shape: {df.shape}")
    print(f"Total Missing Values: {df.isnull().sum().sum()}")
    print("Missing by Column:")
    print(df.isnull().sum())
    print(f"Duplicate Rows: {df.duplicated().sum()}")
    print("=========================================\n")


def standardize_columns(df: pd.DataFrame) -> pd.DataFrame:
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df


def enforce_schema(df: pd.DataFrame) -> pd.DataFrame:
    expected_binary = ["international_plan", "voice_mail_plan"]
    for col in expected_binary:
        if col not in df.columns:
            print(f"Warning: Expected column '{col}' not found.")

    if "churn" in df.columns:
        df["churn"] = pd.to_numeric(df["churn"], errors="coerce")

    return df


def handle_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"Removing {duplicates} duplicate rows.")
        df = df.drop_duplicates().reset_index(drop=True)
    else:
        print("No duplicate rows detected.")
    return df


def map_binary_columns(df: pd.DataFrame, binary_cols: List[str]) -> pd.DataFrame:
    for col in binary_cols:
        if col in df.columns:
            df[col] = (
                df[col]
                .astype(str)
                .str.strip()
                .str.lower()
            )

            unexpected_values = set(df[col].unique()) - {"yes", "no"}
            if unexpected_values:
                print(f"Warning: Unexpected values in '{col}': {unexpected_values}")

            df[col] = df[col].map({"yes": 1, "no": 0})

    return df


def validate_numeric_ranges(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        negative_count = (df[col] < 0).sum()
        if negative_count > 0:
            print(f"Warning: {negative_count} negative values detected in '{col}'.")
            # Instead of dropping silently, we flag or set to NaN
            df.loc[df[col] < 0, col] = np.nan

    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    numeric_cols = df.select_dtypes(include=[np.number]).columns

    for col in numeric_cols:
        missing_count = df[col].isnull().sum()
        if missing_count > 0:
            median_value = df[col].median()
            print(f"Imputing {missing_count} missing values in '{col}' with median.")
            df[col] = df[col].fillna(median_value)

    return df


def preprocess_pipeline(path: str) -> pd.DataFrame:
    df = load_data(path)

    data_quality_report(df, stage="RAW")

    df = standardize_columns(df)
    df = enforce_schema(df)
    df = handle_duplicates(df)
    df = map_binary_columns(df, ["international_plan", "voice_mail_plan"])
    df = validate_numeric_ranges(df)
    df = handle_missing(df)

    data_quality_report(df, stage="CLEANED")

    return df


if __name__ == "__main__":
    df_cleaned = preprocess_pipeline(INPUT_PATH)
    df_cleaned.to_csv(OUTPUT_PATH, index=False)
    print(f"Cleaned dataset saved to '{OUTPUT_PATH}'")

    print("\nPreview:")
    print(df_cleaned.head())

    print("\nData Types Summary:")
    print(df_cleaned.dtypes)