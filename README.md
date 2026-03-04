# Codveda Data Analysis Internship 🚀

Welcome to my professional repository for the **Data Analysis Internship** at **Codveda Technologies**.  

This repository documents my structured progression from foundational data preparation to more advanced analytical tasks, with a focus on clarity, reproducibility, and disciplined analytical workflow.

---

## 📌 Program Overview

As a Data Analysis Intern, my objective is to strengthen practical data analysis skills by working through progressively structured tasks:

- Preparing raw datasets for analysis
- Conducting structured exploratory analysis
- Building analytical reasoning through statistical interpretation
- Developing clean and reproducible code practices

The repository is organized by levels, reflecting increasing analytical depth.

---

# 🛠️ Level 1 – Foundation

Level 1 focuses on establishing strong analytical fundamentals: data preparation and structured exploration.

---

## ✅ Task 1: Data Cleaning & Preprocessing

This task focused on transforming raw datasets into structured, analysis-ready formats.

### Key Implementations

- Systematic identification of missing values and duplicates
- Data type validation and correction
- Logical sanity checks (e.g., preventing negative numerical values)
- Feature standardization using consistent naming conventions (`snake_case`)
- Categorical normalization for consistency

### Datasets Processed

- **Customer Churn Dataset**
  - Encoding categorical variables
  - Ensuring numerical consistency
- **Sentiment Dataset**
  - Handling structured social media metadata
  - Formatting temporal features

### Tools Used

`Python` · `Pandas` · `NumPy`

---

## ✅ Task 2: Exploratory Data Analysis (EDA)

This task focused on conducting structured exploratory analysis to understand statistical patterns, distributions, and relationships between numerical variables.

### Objectives Achieved

- Calculated summary statistics:
  - Mean
  - Median
  - Mode
  - Standard Deviation
- Visualized distributions using:
  - Histograms (with KDE)
  - Boxplots for outlier detection
- Explored feature relationships through:
  - Scatter plots
- Identified correlations using:
  - Correlation matrix
  - Heatmap visualization

### Implementation Highlights

- Modular Python script (`EDA.py`)
- Automated chart export into structured folders
- Reproducible pipeline for multiple datasets
- Clear separation between data loading, analysis, and visualization logic

All visual outputs are automatically saved into organized directories for easier review and comparison.

### Tools Used

`Python` · `Pandas` · `Matplotlib` · `Seaborn`

---

# 📂 Repository Structure

```text
├── Level_1_Foundation/
│   ├── Data/
│   │   ├── Raw/
│   │   └── Processed/
│   ├── Task_1_Cleaning/
│   └── Task_2_EDA/
│       ├── scripts/
│       └── eda_outputs/
├── Level_2_Intermediate/      # Upcoming
└── Level_3_Advanced/          # Upcoming
