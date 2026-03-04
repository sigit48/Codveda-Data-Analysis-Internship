import os
import pandas as pd
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns


matplotlib.use('Agg')

# ==========================================================
# CONFIGURATION
# ==========================================================
sns.set_theme(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)
OUTPUT_BASE_DIR = "eda_outputs"

# ==========================================================
# UTILITY FUNCTIONS
# ==========================================s================

def create_output_folder(dataset_name: str) -> str:
    path = os.path.join(OUTPUT_BASE_DIR, dataset_name)
    os.makedirs(path, exist_ok=True)
    return path

def save_plot(path: str, filename: str):
    """
    Clean special character in Windows.
    """
    
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, "_")
        
    full_path = os.path.join(path, filename)
    plt.tight_layout()
    plt.savefig(full_path, dpi=300)
    plt.close() 

# ==========================================================
# DATA LOADING
# ==========================================================

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    
    
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    
    if df.empty:
        raise ValueError("Loaded dataset is empty.")
    return df

# ==========================================================
# ANALYSIS FUNCTIONS
# ==========================================================

def summary_statistics(df: pd.DataFrame, dataset_name: str):
    numeric_df = df.select_dtypes(include=[np.number])
    print(f"\n===== SUMMARY STATISTICS ({dataset_name.upper()}) =====")
    stats = numeric_df.describe()
    print(stats)
    return stats

def distribution_analysis(df: pd.DataFrame, output_path: str):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        plt.figure()
        sns.histplot(df[col], kde=True, color='teal')
        plt.title(f"Distribution of {col}")
        save_plot(output_path, f"histogram_{col}.png")

def boxplot_analysis(df: pd.DataFrame, output_path: str):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        plt.figure()
        sns.boxplot(x=df[col], color='coral')
        plt.title(f"Boxplot of {col}")
        save_plot(output_path, f"boxplot_{col}.png")

def scatter_analysis(df: pd.DataFrame, output_path: str):
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    
    for i in range(min(3, len(numeric_cols)-1)):
        x_col = numeric_cols[i]
        y_col = numeric_cols[i+1]
        plt.figure()
        sns.scatterplot(x=df[x_col], y=df[y_col], alpha=0.6)
        plt.title(f"{x_col} vs {y_col}")
        save_plot(output_path, f"scatter_{x_col}_vs_{y_col}.png")

def correlation_analysis(df: pd.DataFrame, output_path: str):
    numeric_df = df.select_dtypes(include=[np.number])
    if numeric_df.empty: return
    
    corr_matrix = numeric_df.corr()
    plt.figure(figsize=(12, 10))
    sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap="coolwarm", square=True)
    plt.title("Correlation Heatmap")
    save_plot(output_path, "correlation_heatmap.png")

# ==========================================================
# EXECUTION PIPELINE
# ==========================================================

def run_eda_pipeline(dataset_path: str, dataset_name: str):
    print(f"\n>>> Starting Pipeline for: {dataset_name.upper()}")
    
    try:
        df = load_data(dataset_path)
        output_path = create_output_folder(dataset_name)
        
        
        summary_statistics(df, dataset_name)
        distribution_analysis(df, output_path)
        boxplot_analysis(df, output_path)
        scatter_analysis(df, output_path)
        correlation_analysis(df, output_path)
        
        print(f"✓ Success! All charts saved in: {output_path}")
    except Exception as e:
        print(f"✗ Failed to process {dataset_name}: {e}")

# ==========================================================
# MAIN EXECUTION
# ==========================================================

if __name__ == "__main__":
    # Path dataset 
    CHURN_PATH = "churn_cleaned_final.csv"
    SENTIMENT_PATH = "sentiment_cleaned_final.csv"

    run_eda_pipeline(CHURN_PATH, "churn")
    run_eda_pipeline(SENTIMENT_PATH, "sentiment")
    
    print("\n[ALL TASKS COMPLETED SUCCESSFULLY]")