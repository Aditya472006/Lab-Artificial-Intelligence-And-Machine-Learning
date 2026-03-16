Code:
# Import libraries import pandas as pd
from sklearn.model_selection import train_test_split from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Load dataset
data = pd.read_csv("iris.csv")
# Features and target
X = data.drop("species", axis=1) y = data["species"]
# Train test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
# Create model
model = DecisionTreeClassifier()
# Train model model.fit(X_train, y_train)
# Prediction
y_pred = model.predict(X_test)
# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred)) print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))
