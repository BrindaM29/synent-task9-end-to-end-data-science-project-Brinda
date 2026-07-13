# Customer Churn Prediction System

# Problem Statement

Customer churn is one of the biggest challenges faced by subscription-based businesses such as telecom, banking, insurance, and internet service providers. Acquiring a new customer is significantly more expensive than retaining an existing one.

The objective of this project is to build a Machine Learning model that predicts whether a customer is likely to churn, allowing businesses to take proactive measures to improve customer retention.

---

# Objectives

* Collect and preprocess a real-world dataset.
* Perform Exploratory Data Analysis (EDA) to understand customer behavior.
* Build an accurate Machine Learning model for churn prediction.
* Evaluate the model using classification metrics.
* Deploy the trained model using Streamlit.
* Provide an interactive web interface for user predictions.

---

# Dataset

**Dataset Name:** Telco Customer Churn Dataset

**Source:** Kaggle

The dataset contains customer information such as:

* Gender
* Senior Citizen
* Partner
* Dependents
* Tenure
* Phone Service
* Internet Service
* Contract Type
* Payment Method
* Monthly Charges
* Total Charges
* Churn Status

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Joblib
* Streamlit

---

# Project Workflow

## 1. Data Collection

* Downloaded the Telco Customer Churn dataset from Kaggle.
* Imported the dataset using Pandas.

## 2. Data Cleaning

* Removed unnecessary columns.
* Converted categorical values into numerical format.
* Converted TotalCharges to numeric datatype.
* Handled missing values.
* Checked duplicate records.

## 3. Exploratory Data Analysis (EDA)

The following visualizations were created:

* Churn Distribution
* Gender Distribution
* Contract Type Analysis
* Internet Service Analysis
* Payment Method Distribution
* Monthly Charges Histogram
* Tenure Histogram
* Monthly Charges vs Churn (Box Plot)
* Scatter Plot (Tenure vs Monthly Charges)
* Correlation Heatmap
* Feature Importance Graph

These visualizations help understand customer behavior and identify factors influencing churn.

---

# Machine Learning Models

The following algorithms were implemented:

* Random Forest Classifier
* Logistic Regression
* Decision Tree Classifier

The best-performing model was selected for deployment.

---

# Model Evaluation

The model was evaluated using:

* Accuracy Score
* Precision
* Recall
* F1-Score
* Confusion Matrix
* ROC Curve

The trained model achieved an accuracy of approximately **80%** (may vary depending on preprocessing and train-test split).

---

# Deployment

The trained model was deployed using **Streamlit**.

The application allows users to:

* Enter customer details.
* Predict customer churn.
* Display prediction results instantly.
* Provide a simple and interactive user interface.

---

# Project Structure

```text
Customer_Churn_Project/
│
├── churn.csv
├── eda.py
├── train_model.py
├── app.py
├── model.pkl
├── requirements.txt
├── README.md
│
├── images/
│   ├── churn_distribution.png
│   ├── histogram.png
│   ├── scatter_plot.png
│   ├── heatmap.png
│   └── feature_importance.png
│
└── screenshots/
    ├── home_page.png
    ├── prediction_page.png
    └── output.png
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/Customer_Churn_Project.git
```

Navigate to the project folder:

```bash
cd Customer_Churn_Project
```

Install the required libraries:

```bash
pip install -r requirements.txt
```

---

# Run the Project

Train the model:

```bash
python train_model.py
```

Run Exploratory Data Analysis:

```bash
python eda.py
```

Launch the Streamlit application:

```bash
streamlit run app.py
```

---

# Features

* Real-world dataset from Kaggle
* Data Cleaning
* Exploratory Data Analysis
* Machine Learning Model Training
* Model Evaluation
* Customer Churn Prediction
* Interactive Streamlit Web Application
* Easy-to-use User Interface

---

# Future Enhancements

* Hyperparameter tuning using GridSearchCV
* XGBoost and LightGBM implementation
* Real-time database integration
* User authentication system
* Cloud deployment
* Interactive dashboard using Plotly
* Prediction history storage
* Model monitoring and retraining

---

# Results

* Successfully cleaned and preprocessed the dataset.
* Generated meaningful visualizations through EDA.
* Built a Machine Learning model capable of predicting customer churn.
* Achieved good prediction accuracy.
* Successfully deployed the model using Streamlit with an interactive web interface.

---

# Learning Outcomes

Through this project, the following concepts were learned:

* Data Preprocessing
* Data Visualization
* Feature Engineering
* Machine Learning
* Model Evaluation
* Classification Algorithms
* Streamlit Deployment
* End-to-End Data Science Workflow

---
