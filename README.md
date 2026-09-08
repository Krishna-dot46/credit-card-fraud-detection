# credit-card-fraud-detection
# Credit Card Fraud Detection

## 📌 Project Overview

This project focuses on detecting fraudulent credit card transactions using Python and Machine Learning.

The dataset contains transaction information with several numerical features (`V1` to `V28`), transaction `Amount`, and a `Class` column that identifies whether a transaction is normal or fraudulent.

* `Class = 0` → Normal transaction
* `Class = 1` → Fraudulent transaction

The project includes data loading, data inspection, fraud-count analysis, and visualization of transaction data.

## 🎯 Objectives

* Analyze credit card transaction data.
* Identify normal and fraudulent transactions.
* Understand the distribution of fraud and normal transactions.
* Visualize transaction amounts.
* Prepare the dataset for Machine Learning-based fraud detection.

## 📂 Project Structure

```text
fraud-detection/
│
├── fraud_detection.py
├── README.md
├── requirements.txt
└── .gitignore
```

## 🛠️ Technologies Used

* Python
* Pandas
* Matplotlib
* Machine Learning
* Jupyter/Python environment

## 📊 Dataset

The original dataset is approximately 325 MB, so it is not included directly in this GitHub repository.

The dataset contains:

* `id` – Transaction identifier
* `V1` to `V28` – Numerical transaction features
* `Amount` – Transaction amount
* `Class` – Fraud classification label

You can download the dataset from the original dataset source and place it in the project folder as:

```text
creditcard_2023.csv
```

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd fraud-detection
```

### 3. Install required libraries

```bash
pip install pandas matplotlib
```

### 4. Add the dataset

Place:

```text
creditcard_2023.csv
```

inside the project directory.

### 5. Run the Python program

```bash
python fraud_detection.py
```

## 📈 Current Analysis

The Python program performs:

1. Dataset loading
2. Display of the first five records
3. Dataset information and data types
4. Fraud vs. normal transaction count
5. Fraud/normal transaction visualization
6. Transaction amount distribution visualization

## 🔮 Future Improvements

The project can be extended by implementing:

* Logistic Regression
* Random Forest
* Decision Tree
* XGBoost
* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC
* Feature Importance
* Explainable AI (XAI)

## 👩‍💻 Author

**Krishna Ramani**

MCA Student

## ⭐ Project Status

🚧 Currently under development. Machine Learning model comparison and performance evaluation can be added in future versions.
