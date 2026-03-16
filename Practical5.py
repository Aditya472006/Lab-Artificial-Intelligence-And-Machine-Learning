# Import libraries import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split from sklearn.neighbors import KNeighborsClassifier from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score
# Load dataset data = load_iris()
X = data.data y = data.target

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# KNN Model
knn = KNeighborsClassifier(n_neighbors=5) knn.fit(X_train, y_train)
pred_knn = knn.predict(X_test)

# Naive Bayes Model nb = GaussianNB() nb.fit(X_train, y_train)
pred_nb = nb.predict(X_test)

# Evaluation for KNN print("KNN Results")
print("Accuracy:", accuracy_score(y_test, pred_knn)) print("Precision:", precision_score(y_test, pred_knn, average='macro'))
print("Recall:", recall_score(y_test, pred_knn, average='macro'))

# Evaluation for Naive Bayes print("\nNaive Bayes Results")
print("Accuracy:", accuracy_score(y_test, pred_nb))
print("Precision:", precision_score(y_test, pred_nb,
average='macro'))
print("Recall:", recall_score(y_test, pred_nb, average='macro'))
