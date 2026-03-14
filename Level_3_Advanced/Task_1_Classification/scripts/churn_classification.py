import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    classification_report,
    accuracy_score,
    confusion_matrix
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# =========================================
# 1. CONFIGURATION
# =========================================
DATA_PATH = r"C:\Users\LENOVO\Documents\DATA ANALYST\Codveda\Level_1_Foundation\Data\Processed\churn_cleaned_final.csv"
OUTPUT_DIR = "outputs"

os.makedirs(OUTPUT_DIR, exist_ok=True)
sns.set_theme(style="whitegrid")

# =========================================
# 2. LOAD & INITIAL CLEANING
# =========================================
df = pd.read_csv(DATA_PATH)

# Buang kolom 'Unnamed' (sampah index)
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print(f">>> Dataset Loaded: {df.shape}")
print(f">>> Unique values in 'churn' before encoding: {df['churn'].unique()}")

# =========================================
# 3. ROBUST TARGET ENCODING
# =========================================
# Kita pastikan target menjadi integer 0 atau 1 tanpa menghapus data
if df["churn"].dtype == 'object' or df["churn"].dtype == 'bool':
    # Standarisasi teks: "yes" -> "Yes", True -> "True"
    df["churn"] = df["churn"].astype(str).str.strip().str.capitalize()
    mapping = {"Yes": 1, "No": 0, "True": 1, "False": 0, "1": 1, "0": 0}
    df["churn"] = df["churn"].map(mapping)

# Jika ada baris yang beneran kosong (NaN asli), baru kita hapus
df = df.dropna(subset=["churn"])
df["churn"] = df["churn"].astype(int)

print(f">>> Data remaining after encoding: {len(df)} rows")

# =========================================
# 4. FEATURE ENGINEERING
# =========================================
X = df.drop(columns=["churn"])
y = df["churn"]

# One-Hot Encoding untuk kolom kategorikal
X = pd.get_dummies(X, drop_first=True)

# =========================================
# 5. DATA SPLITTING & SCALING
# =========================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# =========================================
# 6. MODEL EVALUATION PIPELINE
# =========================================
models = {
    "Logistic Regression": LogisticRegression(max_iter=1000),
    "Decision Tree": DecisionTreeClassifier(random_state=42),
    "Random Forest": RandomForestClassifier(random_state=42)
}

results = {}

for name, model in models.items():
    print(f"\n--- Training {name} ---")
    
    # Scaling hanya wajib untuk Logistic Regression
    if name == "Logistic Regression":
        model.fit(X_train_scaled, y_train)
        preds = model.predict(X_test_scaled)
    else:
        model.fit(X_train, y_train)
        preds = model.predict(X_test)

    acc = accuracy_score(y_test, preds)
    results[name] = acc
    print(f"Accuracy: {acc:.4f}")
    print(classification_report(y_test, preds))

# =========================================
# 7. HYPERPARAMETER TUNING (RANDOM FOREST)
# =========================================
print("\n>>> Tuning Random Forest for Best Performance...")
param_grid = {
    "n_estimators": [100, 150],
    "max_depth": [10, None],
    "min_samples_split": [2, 5]
}

grid = GridSearchCV(
    RandomForestClassifier(random_state=42),
    param_grid, cv=3, scoring="accuracy", n_jobs=-1
)
grid.fit(X_train, y_train)

best_model = grid.best_estimator_
best_preds = best_model.predict(X_test)

# =========================================
# 8. EXPORTING RESULTS & VISUALS
# =========================================

# A. Save Text Report
report_path = os.path.join(OUTPUT_DIR, "classification_results.txt")
with open(report_path, "w") as f:
    f.write("FINAL CLASSIFICATION REPORT\n" + "="*30 + "\n")
    for m, a in results.items():
        f.write(f"{m}: {a:.4f}\n")
    f.write(f"\nBest RF Params: {grid.best_params_}\n")

# B. Save Confusion Matrix
plt.figure(figsize=(7, 5))
cm = confusion_matrix(y_test, best_preds)
sns.heatmap(cm, annot=True, fmt="d", cmap="Greens", 
            xticklabels=["Stay", "Churn"], yticklabels=["Stay", "Churn"])
plt.title("Confusion Matrix: Optimized Random Forest")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.savefig(os.path.join(OUTPUT_DIR, "confusion_matrix.png"), dpi=300)
plt.close()

# C. Save Comparison Chart
plt.figure(figsize=(9, 6))
sns.barplot(x=list(results.keys()), y=list(results.values()), palette="magma")
plt.title("Model Accuracy Comparison")
plt.ylabel("Accuracy Score")
plt.ylim(0, 1.0)
plt.savefig(os.path.join(OUTPUT_DIR, "model_comparison.png"), dpi=300)
plt.close()

print(f"\n[ALL TASKS COMPLETED]")
print(f"Check your results in: {os.path.abspath(OUTPUT_DIR)}")