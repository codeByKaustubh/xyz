# Feed Forward Backpropagation Neural Network
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Load data
iris = load_iris()
X, y = iris.data, iris.target.reshape(-1, 1)

# One-hot encode labels
encoder = OneHotEncoder(sparse_output=False)  # ✅ FIXED: use sparse_output instead of sparse
y = encoder.fit_transform(y)

# Scale features
scaler = StandardScaler()
X = scaler.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Network architecture
input_size = X_train.shape[1]   # 4 features
hidden_size = 8
output_size = y_train.shape[1]  # 3 classes
lr = 0.1
epochs = 500

# Initialize weights
np.random.seed(42)
W1 = np.random.randn(input_size, hidden_size)
b1 = np.zeros((1, hidden_size))
W2 = np.random.randn(hidden_size, output_size)
b2 = np.zeros((1, output_size))

# Activation functions
def sigmoid(x): return 1 / (1 + np.exp(-x))
def sigmoid_deriv(x): return x * (1 - x)
def softmax(x): return np.exp(x) / np.sum(np.exp(x), axis=1, keepdims=True)

# Training
for epoch in range(epochs):
    # Forward pass
    z1 = np.dot(X_train, W1) + b1
    a1 = sigmoid(z1)
    z2 = np.dot(a1, W2) + b2
    a2 = softmax(z2)

    # Loss (Cross-Entropy)
    loss = -np.mean(np.sum(y_train * np.log(a2 + 1e-9), axis=1))

    # Backpropagation
    dz2 = a2 - y_train
    dW2 = np.dot(a1.T, dz2) / X_train.shape[0]
    db2 = np.sum(dz2, axis=0, keepdims=True) / X_train.shape[0]

    dz1 = np.dot(dz2, W2.T) * sigmoid_deriv(a1)
    dW1 = np.dot(X_train.T, dz1) / X_train.shape[0]
    db1 = np.sum(dz1, axis=0, keepdims=True) / X_train.shape[0]

    # Update weights
    W1 -= lr * dW1
    b1 -= lr * db1
    W2 -= lr * dW2
    b2 -= lr * db2

    if epoch % 100 == 0:
        print(f"Epoch {epoch}, Loss: {loss:.4f}")

# Prediction
z1 = np.dot(X_test, W1) + b1
a1 = sigmoid(z1)
z2 = np.dot(a1, W2) + b2
a2 = softmax(z2)

y_pred = np.argmax(a2, axis=1)
y_true = np.argmax(y_test, axis=1)
accuracy = np.mean(y_pred == y_true)
print("Test Accuracy:", accuracy)