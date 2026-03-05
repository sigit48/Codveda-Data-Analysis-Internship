import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_squared_error

# ==========================================================
# CONFIGURATION
# ==========================================================

TEST_SIZE = 0.2
RANDOM_STATE = 42

BASE_OUTPUT = "outputs"
PLOT_DIR = os.path.join(BASE_OUTPUT, "plots")
METRIC_DIR = os.path.join(BASE_OUTPUT, "metrics")

sns.set_style("whitegrid")

# ==========================================================
# OUTPUT DIRECTORY SETUP
# ==========================================================

def create_output_folders():

    os.makedirs(PLOT_DIR, exist_ok=True)
    os.makedirs(METRIC_DIR, exist_ok=True)

# ==========================================================
# DATA LOADING
# ==========================================================

def load_data(path: str) -> pd.DataFrame:

    df = pd.read_csv(path)

    # Remove unwanted unnamed columns
    df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

    if df.empty:
        raise ValueError("Dataset is empty.")

    print(f"\nDataset loaded: {path}")
    print(f"Shape after cleaning: {df.shape}")

    return df


# ==========================================================
# REGRESSION ENGINE
# ==========================================================

def run_simple_linear_regression(df: pd.DataFrame, feature: str, target: str, dataset_name: str):

    print(f"\n>>> Running Simple Linear Regression: {target} ~ {feature}")

    if feature not in df.columns or target not in df.columns:
        raise ValueError("Selected feature or target not found in dataset.")

    X = df[[feature]]
    y = df[target]

    # Train-Test Split
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=TEST_SIZE,
        random_state=RANDOM_STATE
    )

    # Model Training
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    r2 = r2_score(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)

    print(f"Coefficient (Slope): {model.coef_[0]:.4f}")
    print(f"Intercept: {model.intercept_:.4f}")
    print(f"R-squared: {r2:.4f}")
    print(f"Mean Squared Error: {mse:.4f}")

    # Save metrics
    metrics_df = pd.DataFrame({
        "dataset": [dataset_name],
        "feature": [feature],
        "target": [target],
        "coefficient": [model.coef_[0]],
        "intercept": [model.intercept_],
        "r2_score": [r2],
        "mse": [mse]
    })

    metrics_path = os.path.join(METRIC_DIR, f"{dataset_name}_regression_metrics.csv")
    metrics_df.to_csv(metrics_path, index=False)

    # ======================================================
    # PLOT REGRESSION RESULT
    # ======================================================

    plt.figure(figsize=(8,6))

    sns.scatterplot(x=X_test[feature], y=y_test)

    plt.plot(
        X_test[feature],
        y_pred,
        color="red",
        linewidth=2
    )

    plt.title(f"{dataset_name.upper()} Regression: {target} vs {feature}")
    plt.xlabel(feature)
    plt.ylabel(target)

    plot_path = os.path.join(PLOT_DIR, f"{dataset_name}_regression_plot.png")

    plt.tight_layout()
    plt.savefig(plot_path, dpi=300)
    plt.close()

    print(f"Plot saved to: {plot_path}")

# ==========================================================
# MAIN EXECUTION
# ==========================================================

if __name__ == "__main__":

    create_output_folders()

    # ---------------------------
    # CHURN DATASET
    # ---------------------------

    churn_path = r"churn_cleaned_final.csv"
    churn_df = load_data(churn_path)

    run_simple_linear_regression(
        churn_df,
        feature="total_day_minutes",
        target="total_day_charge",
        dataset_name="churn"
    )

    # ---------------------------
    # SENTIMENT DATASET
    # ---------------------------

    sentiment_path = r"sentiment_cleaned_final.csv"
    sentiment_df = load_data(sentiment_path)

    run_simple_linear_regression(
        sentiment_df,
        feature="Retweets",
        target="Likes",
        dataset_name="sentiment"
    )

    print("\n[ALL REGRESSION ANALYSES COMPLETED SUCCESSFULLY]")