#Adaboost Ensemble Learning
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier

# 1. Create a toy dataset
X, y = make_classification(
    n_samples=500, n_features=2, n_informative=2, n_redundant=0,
    n_clusters_per_class=1, flip_y=0.1, class_sep=1.5, random_state=42
)

# Convert labels from {0,1} to {-1,1} for AdaBoost from scratch
y_mod = np.where(y == 0, -1, 1)

# Split train/test
X_train, X_test, y_train, y_test = train_test_split(X, y_mod, test_size=0.3, random_state=42)


# 2. Implement AdaBoost from Scratch
class AdaBoostScratch:
    def __init__(self, n_estimators=50):
        self.n_estimators = n_estimators
        self.alphas = []
        self.models = []

    def fit(self, X, y):
        n_samples, _ = X.shape
        # Initialize weights
        w = np.ones(n_samples) / n_samples

        for _ in range(self.n_estimators):
            # Train weak classifier (Decision stump)
            stump = DecisionTreeClassifier(max_depth=1, random_state=42)
            stump.fit(X, y, sample_weight=w)
            y_pred = stump.predict(X)

            # Compute weighted error
            err = np.sum(w * (y_pred != y)) / np.sum(w)
            if err > 0.5:  # If weak learner worse than random, stop early
                break

            # Compute alpha
            alpha = 0.5 * np.log((1 - err) / (err + 1e-10))

            # Update weights
            w *= np.exp(-alpha * y * y_pred)
            w /= np.sum(w)

            # Save
            self.models.append(stump)
            self.alphas.append(alpha)

    def predict(self, X):
        # Weighted vote
        final_pred = np.zeros(X.shape[0])
        for alpha, model in zip(self.alphas, self.models):
            final_pred += alpha * model.predict(X)
        return np.sign(final_pred)


# 3. Train AdaBoost (Scratch)
ada_scratch = AdaBoostScratch(n_estimators=50)
ada_scratch.fit(X_train, y_train)
y_pred_scratch = ada_scratch.predict(X_test)
acc_scratch = accuracy_score(y_test, y_pred_scratch)
print("AdaBoost (Scratch) Accuracy:", acc_scratch)

# 4. Train AdaBoost (Sklearn)
ada_sklearn = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)
ada_sklearn.fit(X_train, y_train)
y_pred_sklearn = ada_sklearn.predict(X_test)
acc_sklearn = accuracy_score(y_test, y_pred_sklearn)
print("AdaBoost (Sklearn) Accuracy:", acc_sklearn)

# 5. Compare with Weak Classifier Alone
weak_clf = DecisionTreeClassifier(max_depth=1)
weak_clf.fit(X_train, y_train)
y_pred_weak = weak_clf.predict(X_test)
acc_weak = accuracy_score(y_test, y_pred_weak)
print("Weak Classifier Accuracy:", acc_weak)


# 6. Visualization (Decision Boundaries)
def plot_decision_boundary(model, X, y, title):
    x_min, x_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    y_min, y_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx, yy = np.meshgrid(
        np.linspace(x_min, x_max, 200),
        np.linspace(y_min, y_max, 200)
    )
    Z = model.predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3, cmap='coolwarm')
    plt.scatter(X[:, 0], X[:, 1], c=y, edgecolors='k', cmap='coolwarm')
    plt.title(title)
    plt.show()


# Plot decision boundaries
plot_decision_boundary(weak_clf, X_test, y_test, "Weak Classifier")
plot_decision_boundary(ada_sklearn, X_test, y_test, "AdaBoost (Sklearn)")