from sklearn.datasets import load_iris

# 1. Import data set
# 2. Train a classifier.
# 3. Predict label(class).

iris = load_iris()

print(iris.feature_names)  # features
print(iris.target_names)  # labels
print(iris.data[0])
