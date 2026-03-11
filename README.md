# Codveda Data Analysis Internship 🚀

Welcome to my professional repository for the **Data Analysis Internship at Codveda Technologies**.

This repository documents a structured analytical workflow, progressing from **data preparation and exploratory analysis** toward **statistical modeling and predictive insights**.

The goal of this repository is to demonstrate disciplined analytical practices, including:

- Data quality validation  
- Reproducible analysis pipelines  
- Structured statistical exploration  
- Interpretable modeling outputs  

All tasks are organized into levels reflecting increasing analytical depth.

---

# 📌 Program Overview

During this internship, tasks are structured into progressive analytical stages:

| Level | Focus |
|------|------|
| **Level 1** | Data Preparation & Exploratory Analysis |
| **Level 2** | Statistical Modeling & Pattern Discovery |
| **Level 3** | Machine Learning & Predictive Analytics |

Each level builds analytical depth while emphasizing **clean implementation, reproducibility, and clear interpretation of results.**

---

# 🛠️ Level 1 – Foundation

Level 1 focuses on establishing strong analytical fundamentals through **data cleaning and structured exploratory analysis.**

---

## ✅ Task 1: Data Cleaning & Preprocessing

This task focused on transforming raw datasets into structured, analysis-ready formats while maintaining data integrity.

### Key Implementations

- Identification and verification of missing values
- Duplicate detection and removal
- Data type validation and correction
- Logical sanity checks for numerical features
- Standardization of column naming (`snake_case`)
- Categorical normalization for consistency

### Datasets Processed

**Customer Churn Dataset**

- Binary encoding for categorical variables
- Numeric validation for call and charge features

**Sentiment Dataset**

- Cleaning social media metadata
- Structuring temporal variables (Year, Month, Day, Hour)

### Tools Used

`Python` · `Pandas` · `NumPy`

---

## ✅ Task 2: Exploratory Data Analysis (EDA)

This task focused on conducting structured exploratory analysis to understand statistical distributions and relationships between variables.

### Objectives Achieved

- Calculated summary statistics:
  - Mean
  - Median
  - Mode
  - Standard Deviation

- Visualized distributions using:
  - Histograms with KDE
  - Boxplots for outlier detection

- Explored feature relationships through:
  - Scatter plots

- Identified correlations using:
  - Correlation matrix
  - Heatmap visualization

### Implementation Highlights

- Modular Python analysis pipeline
- Automated chart export into structured output folders
- Reproducible analysis workflow applicable to multiple datasets

Generated outputs include:

- Distribution charts
- Scatter plots
- Correlation heatmaps

### Tools Used

`Python` · `Pandas` · `Matplotlib` · `Seaborn`

---

# 📊 Level 2 – Statistical Analysis

Level 2 introduces statistical modeling techniques used to evaluate relationships between variables and discover patterns in data.

---

## ✅ Task 1: Simple Linear Regression

This task implements **Simple Linear Regression** to analyze linear relationships between numerical variables and evaluate model performance using standard regression metrics.

### Objectives Achieved

- Split datasets into **training and testing sets**
- Trained regression models using **scikit-learn**
- Evaluated model performance using:
  - **R-squared**
  - **Mean Squared Error (MSE)**

### Regression Experiments

Two regression analyses were conducted:

#### Customer Churn Dataset

Feature:  
`total_day_minutes`

Target:  
`total_day_charge`

Purpose:

To validate the expected linear relationship between call duration and call charges.

---

#### Sentiment Dataset

Feature:  
`Retweets`

Target:  
`Likes`

Purpose:

To evaluate engagement correlation between user interaction metrics on social media posts.

---

### Tools Used

`Python` · `Pandas` · `Scikit-learn` · `Matplotlib` · `Seaborn`

---

## ✅ Task 3: Customer Churn Clustering (K-Means)

This task applies **unsupervised machine learning** to identify hidden patterns in customer behavior using clustering techniques.

### Objectives Achieved

- Selected behavioral features related to telecom usage
- Standardized numerical features using **StandardScaler**
- Determined the optimal number of clusters using the **Elbow Method**
- Applied **K-Means clustering** to segment customers
- Visualized clusters using scatter plots

### Features Used for Clustering

- `total_day_minutes`
- `total_eve_minutes`
- `total_night_minutes`
- `total_intl_minutes`

These features represent **customer communication behavior across different time periods**, enabling meaningful segmentation.

### Implementation Highlights

- Automated clustering pipeline using **scikit-learn**
- Feature scaling for distance-based algorithms
- Elbow Method visualization for optimal cluster selection
- Cluster visualization for interpretability

### Generated Outputs

- Elbow Method Plot
- Customer Cluster Visualization
- Clustered Dataset

### Tools Used

`Python` · `Pandas` · `Scikit-learn` · `Matplotlib` · `Seaborn`

---

# 🧠 Level 3 – Machine Learning & Predictive Analytics

Level 3 introduces predictive machine learning models designed to support **data-driven decision making**.

---

## ✅ Task 1: Customer Churn Classification

This task builds **classification models to predict whether a customer is likely to churn** based on behavioral and service features.

### Objectives Achieved

- Preprocessed data for machine learning
- Encoded categorical variables using **One-Hot Encoding**
- Applied **feature scaling** using StandardScaler
- Split dataset into **training and testing sets**
- Trained and compared multiple classification models
- Evaluated model performance using standard metrics
- Performed **hyperparameter tuning using GridSearchCV**

---

### Models Implemented

**Logistic Regression**

Baseline classification model for churn prediction.

**Decision Tree**

Captures non-linear relationships between features.

**Random Forest**

Ensemble learning model improving prediction robustness and accuracy.

---

### Evaluation Metrics

Models were evaluated using:

- **Accuracy**
- **Precision**
- **Recall**
- **F1-score**

These metrics help evaluate performance for **imbalanced classification problems such as churn prediction.**

---

### Generated Outputs

- Model performance report
- Confusion matrix visualization
- Model comparison chart

---

### Tools Used

`Python` · `Pandas` · `Scikit-learn` · `Matplotlib` · `Seaborn`

---

# 📂 Repository Structure
Codveda-Data-Analysis-Internship
│
├── Level_1_Foundation
│ ├── Data
│ │ ├── Raw
│ │ └── Processed
│ │
│ ├── Task_1_Cleaning
│ │ └── scripts
│ │
│ └── Task_2_EDA
│ ├── scripts
│ └── eda_outputs
│
├── Level_2_Intermediate
│ ├── Task_1_Regression
│ │ ├── scripts
│ │ └── outputs
│ │
│ └── Task_3_Clustering
│ ├── scripts
│ └── outputs
│
├── Level_3_Advanced
│ └── Task_1_Classification
│ ├── scripts
│ └── outputs
│
└── README.md

---

# 📈 Current Progress

| Level | Task | Status |
|------|------|------|
| Level 1 | Data Cleaning & Preprocessing | ✅ Completed |
| Level 1 | Exploratory Data Analysis | ✅ Completed |
| Level 2 | Regression Analysis | ✅ Completed |
| Level 2 | Customer Churn Clustering | ✅ Completed |
| Level 3 | Customer Churn Classification | ✅ Completed |
| Level 3 | Advanced Analytics Extensions | 🔜 Upcoming |

---

# 📎 About This Repository

This repository documents my internship journey at **Codveda Technologies**, highlighting the development of structured analytical workflows using real-world style datasets.

The project demonstrates a progression from:

**Data Preparation → Exploratory Analysis → Statistical Modeling → Machine Learning → Predictive Analytics**
