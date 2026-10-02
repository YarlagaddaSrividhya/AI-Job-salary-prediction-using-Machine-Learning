# AI-Job-salary-prediction
Project Overview
This project focuses on predicting job salaries using machine learning regression techniques. The dataset contains job-related information such as job title, experience level, employment type, company size, company location, education requirements, years of experience, industry, remote work ratio, benefits, and other features.

The goal is to build and compare multiple regression models and identify a model that can provide reliable salary predictions.

Key Features
Exploratory Data Analysis (EDA)
Salary distribution and outlier analysis
Categorical feature encoding
Numerical feature preprocessing
Feature engineering
Machine learning pipelines using Pipeline and ColumnTransformer
5-fold cross-validation
Hyperparameter tuning using GridSearchCV and RandomizedSearchCV
Comparison of multiple regression algorithms
Model evaluation using MAE, RMSE, and R²
Machine Learning Models
The following regression models were evaluated:

Linear Regression
Ridge Regression
K-Nearest Neighbors (KNN)
Decision Tree
Support Vector Regression (SVR)
AdaBoost Regressor
Gradient Boosting Regressor
XGBoost Regressor
Model Evaluation
The models were evaluated using:

MAE (Mean Absolute Error): Measures the average difference between predicted and actual salary.
RMSE (Root Mean Squared Error): Gives greater importance to larger prediction errors.
R² Score: Measures the proportion of salary variation explained by the model.
Five-fold cross-validation was used during model selection to obtain more reliable performance estimates and reduce dependence on a single data split.

Hyperparameter optimization was performed using GridSearchCV and RandomizedSearchCV.

Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-learn
XGBoost
Jupyter Notebook
Project Workflow
Data Collection
      ↓
Data Cleaning
      ↓
Exploratory Data Analysis
      ↓
Feature Engineering
      ↓
Outlier Handling
      ↓
Train/Test Split
      ↓
Data Preprocessing
      ↓
Model Training
      ↓
5-Fold Cross-Validation
      ↓
Hyperparameter Tuning
      ↓
Model Evaluation
      ↓
Model Comparison
      ↓
Final Model Selection
Outcome
The project demonstrates an end-to-end machine learning workflow for a regression problem, from data exploration and preprocessing through model development, cross-validation, hyperparameter optimization, and final evaluation.
