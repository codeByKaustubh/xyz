#K-Nearest Neighbors (K-NN)
#Step 1: Import Libraries
import numpy as np 
import pandas as pd 
from sklearn.model_selection import train_test_split 
from sklearn.preprocessing import StandardScaler 
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor 
from sklearn.metrics import accuracy_score, mean_squared_error

# Step 2: Example Dataset (I’ll use Iris for classification and Boston Housing for regression) 
from sklearn.datasets import load_iris, fetch_california_housing 
#Classification dataset 
iris = load_iris() 
X_cls, y_cls = iris.data, iris.target 
# Regression dataset 
housing = fetch_california_housing() 
X_reg, y_reg = housing.data, housing.target

# Step 3: Train-Test Split + Scaling 
# # For classification 
X_train_cls, X_test_cls, y_train_cls, y_test_cls = train_test_split(X_cls, y_cls, test_size=0.2, random_state=42) 
# For regression 
X_train_reg, X_test_reg, y_train_reg, y_test_reg = train_test_split(X_reg, y_reg, test_size=0.2, random_state=42) 
# Feature scaling 
scaler = StandardScaler() 
X_train_cls = scaler.fit_transform(X_train_cls) 
X_test_cls = scaler.transform(X_test_cls)
X_train_reg = scaler.fit_transform(X_train_reg) 
X_test_reg = scaler.transform(X_test_reg)

# Step 4: KNN for Classification 
knn_cls = KNeighborsClassifier(n_neighbors=5) # k=5 
knn_cls.fit(X_train_cls, y_train_cls)
y_pred_cls = knn_cls.predict(X_test_cls) 

# Accuracy 
acc = accuracy_score(y_test_cls, y_pred_cls) 
print("Classification Accuracy:", acc)

# Step 5: KNN for Regression 
knn_reg = KNeighborsRegressor(n_neighbors=5) # k=5 
knn_reg.fit(X_train_reg, y_train_reg) 
y_pred_reg = knn_reg.predict(X_test_reg) 

# Error (MSE) 
mse = mean_squared_error(y_test_reg, y_pred_reg) 
print("Regression MSE:", mse)