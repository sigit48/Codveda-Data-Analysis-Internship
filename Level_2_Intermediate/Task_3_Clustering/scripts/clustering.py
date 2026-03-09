import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# =========================================
# CONFIGURATION
# =========================================

DATA_PATH = r"churn_cleaned_final.csv"

OUTPUT_DIR = "outputs"
ELBOW_PLOT = os.path.join(OUTPUT_DIR, "elbow_plot.png")
CLUSTER_PLOT = os.path.join(OUTPUT_DIR, "clusters_visualization.png")
CLUSTER_DATA = os.path.join(OUTPUT_DIR, "clustered_dataset.csv")

FEATURES = [
    "total_day_minutes",
    "total_eve_minutes",
    "total_night_minutes",
    "total_intl_minutes"
]

sns.set_style("whitegrid")

# =========================================
# CREATE OUTPUT FOLDER
# =========================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================================
# LOAD DATA
# =========================================

df = pd.read_csv(DATA_PATH)

df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

print("Dataset loaded:", df.shape)

# =========================================
# FEATURE SELECTION
# =========================================

X = df[FEATURES]

# =========================================
# STANDARDIZATION
# =========================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# =========================================
# ELBOW METHOD
# =========================================

inertia = []

K_range = range(1, 11)

for k in K_range:

    kmeans = KMeans(n_clusters=k, random_state=42)

    kmeans.fit(X_scaled)

    inertia.append(kmeans.inertia_)

# Plot Elbow

plt.figure(figsize=(8,5))

plt.plot(K_range, inertia, marker="o")

plt.title("Elbow Method for Optimal Clusters")
plt.xlabel("Number of Clusters")
plt.ylabel("Inertia")

plt.savefig(ELBOW_PLOT, dpi=300)

plt.close()

print("Elbow plot saved")

# =========================================
# FINAL KMEANS MODEL
# =========================================

optimal_k = 3

kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42
)

clusters = kmeans.fit_predict(X_scaled)

df["cluster"] = clusters

# =========================================
# CLUSTER VISUALIZATION
# =========================================

plt.figure(figsize=(8,6))

sns.scatterplot(
    x=df["total_day_minutes"],
    y=df["total_eve_minutes"],
    hue=df["cluster"],
    palette="Set2"
)

plt.title("Customer Segmentation via K-Means")
plt.xlabel("Day Minutes")
plt.ylabel("Evening Minutes")

plt.savefig(CLUSTER_PLOT, dpi=300)

plt.close()

print("Cluster visualization saved")

# =========================================
# SAVE DATASET
# =========================================

df.to_csv(CLUSTER_DATA, index=False)

print("Clustered dataset exported")

print("\n[CLUSTERING ANALYSIS COMPLETED]")