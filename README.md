# Customer Segmentation Project

[![Python](https://img.shields.io/badge/Python-3.13%2B-blue.svg)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Model-orange.svg)](https://scikit-learn.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)](https://streamlit.io/)

This repository contains an unsupervised machine learning clustering project that groups customers into distinct clusters based on their household income and spending habits[cite: 11].

---

## Dataset Notice
*Note: The dataset (`marketing_campaign.csv`) used in this project[cite: 11] can be obtained from standard customer analytics or Kaggle repositories.*

---

## Dataset Features & Engineering
* **Income**: Customer's yearly household income[cite: 11].
* **Spending Categories**: Purchase amounts across categories such as wine (`MntWines`), fruits (`MntFruits`), meat (`MntMeatProducts`), fish (`MntFishProducts`), sweets (`MntSweetProducts`), and gold products (`MntGoldProds`)[cite: 11].
* **Total_Spent**: Engineered feature computed by summing up all individual spending category columns[cite: 11].

---

## Project Workflow
1. **Feature Engineering**: Aggregating specific product expenditures to calculate `Total_Spent`[cite: 11].
2. **Preprocessing**: Filtering features (`Income` and `Total_Spent`), removing missing values[cite: 11], and standardizing data using `StandardScaler`[cite: 11].
3. **Optimal Cluster Selection**: Utilizing Yellowbrick's `KElbowVisualizer` to evaluate and find the optimal number of clusters[cite: 11].
4. **Model Training**: Fitting a `KMeans` clustering model using the determined optimal cluster count[cite: 11].
5. **Model Persistence**: Exporting the trained clustering model using `joblib` into `clustering_model.pkl`[cite: 11].
6. **Web Application**: Interactive deployment interface built with Streamlit.

---

## Getting Started & Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/YOUR_USERNAME/customer-segmentation.git](https://github.com/YOUR_USERNAME/customer-segmentation.git)
   cd customer-segmentation
