#Naive Bayes' Classifier
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# 1. Load Dataset
iris = load_iris()
X, y = iris.data, iris.target

# Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# 2. Train Naive Bayes Model
nb = GaussianNB()
nb.fit(X_train, y_train)

# 3. Predictions & Probabilities
y_pred = nb.predict(X_test)
y_prob = nb.predict_proba(X_test)  # class probabilities

# 4. Evaluate
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nClassification Report:\n", classification_report(y_test, y_pred, target_names=iris.target_names))
print("\nConfusion Matrix:\n", confusion_matrix(y_test, y_pred))

# 5. Show some probabilities
for i in range(5):
    print(f"Sample {i+1} True={iris.target_names[y_test[i]]}, Pred={iris.target_names[y_pred[i]]}")
    print("Probabilities:", y_prob[i])
    print("-" * 40)