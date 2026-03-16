# Import libraries import numpy as np import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, MinMaxScaler from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
# Load dataset data = load_iris()
X = data.data y = data.target
# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Standardization
scaler = StandardScaler()
X_train_std = scaler.fit_transform(X_train) X_test_std = scaler.transform(X_test)
# Normalization
norm = MinMaxScaler()
X_train_norm = norm.fit_transform(X_train) X_test_norm = norm.transform(X_test)
# Model
model = LogisticRegression(max_iter=200)
# Train with standardized data model.fit(X_train_std, y_train) pred_std = model.predict(X_test_std)
# Train with normalized data model.fit(X_train_norm, y_train) pred_norm = model.predict(X_test_norm)
# Evaluation print("Standardization Results")
print("Accuracy:", accuracy_score(y_test, pred_std)) print("Precision:", precision_score(y_test, pred_std, average='macro'))
print("Recall:", recall_score(y_test, pred_std, average='macro')) print("F1 Score:", f1_score(y_test, pred_std, average='macro'))
print("\nNormalization Results")
print("Accuracy:", accuracy_score(y_test, pred_norm)) print("Precision:", precision_score(y_test, pred_norm, average='macro'))
print("Recall:", recall_score(y_test, pred_norm, average='macro'))
print("F1 Score:", f1_score(y_test, pred_norm, average='macro'))
