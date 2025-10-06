#Decision Tree Learning
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

iris = load_iris()
x = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target, name='species')

print("First 5 rows of x: ")
print(x.head())
print("\nFirst 5 rows of y: ")
print(y.head())

x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.3, random_state=42, stratify=y)

dtree = DecisionTreeClassifier(criterion="entropy", max_depth=3, random_state=42)
dtree.fit(x_train, y_train)

y_pred = dtree.predict(x_test)

print("\nAccuracy: ", accuracy_score(y_test, y_pred))
print("\nClassification Report: \n", classification_report(y_test, y_pred))

cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt="d", cmap="Blues", xticklabels=iris.target_names, yticklabels=iris.target_names)
plt.xlabel('Predicted')
plt.ylabel('Actual')
plt.title('Confusion Matrix')
plt.show()

plt.figure(figsize=(12,8))
plot_tree(dtree, feature_names=iris.feature_names, class_names=iris.target_names, filled=True, rounded=True, fontsize=10)
plt.show()