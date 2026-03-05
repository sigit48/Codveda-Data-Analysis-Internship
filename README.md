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
| **Level 2** | Statistical Modeling & Analytical Interpretation |
| **Level 3** | Advanced Analytics & Decision Support |

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

- Modular Python analysis pipeline (`EDA.py`)
- Automated chart export into structured output folders
- Reproducible analysis workflow applicable to multiple datasets
- Separation between data loading, analysis logic, and visualization

Generated outputs include:

- Distribution charts
- Scatter plots
- Correlation heatmaps

### Tools Used

`Python` · `Pandas` · `Matplotlib` · `Seaborn`

---

# 📊 Level 2 – Statistical Analysis

Level 2 introduces statistical modeling techniques used to evaluate relationships between variables.

---

## ✅ Task 1: Simple Linear Regression

This task implements **Simple Linear Regression** to analyze linear relationships between numerical variables and evaluate model performance using standard regression metrics.

### Objectives Achieved

- Split datasets into **training and testing sets**
- Trained regression models using **scikit-learn**
- Evaluated model performance using:
  - **R-squared**
  - **Mean Squared Error (MSE)**
- Interpreted regression coefficients

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

### Implementation Highlights

- Structured regression analysis pipeline
- Train-test split for evaluation
- Model performance metrics reported clearly
- Visualization outputs exported as PNG charts
- Organized output artifacts for reproducibility

Generated artifacts include:

- Regression plots
- Model evaluation metrics

### Tools Used

`Python` · `Pandas` · `Scikit-learn` · `Matplotlib` · `Seaborn`

---

# 📂 Repository Structure

```text
Codveda-Data-Analysis-Internship
│
├── Level_1_Foundation
│   ├── Data
│   │   ├── Raw
│   │   └── Processed
│   │
│   ├── Task_1_Cleaning
│   │   └── scripts
│   │
│   └── Task_2_EDA
│       ├── scripts
│       └── eda_outputs
│
├── Level_2_Intermediate
│   └── Task_1_Regression
│       ├── scripts
│       └── outputs
│           ├── plots
│           └── metrics
│
└── Level_3_Advanced
    (Upcoming)
```

---

# 📈 Current Progress

| Level | Task | Status |
|------|------|------|
| Level 1 | Data Cleaning & Preprocessing | ✅ Completed |
| Level 1 | Exploratory Data Analysis | ✅ Completed |
| Level 2 | Regression Analysis | ✅ Completed |
| Level 2 | Customer Churn Classification | ⏳ In Progress |
| Level 3 | Advanced Analytics | 🔜 Upcoming |

---

# 📎 About This Repository

This repository documents my internship journey at **Codveda Technologies**, highlighting the development of structured analytical workflows using real-world style datasets.

The focus is on building **clear, reproducible, and interpretable data analysis pipelines** that mirror professional analytical practices.
