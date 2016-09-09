from sklearn.datasets import load_iris
import numpy
from sklearn import tree

# 1. Import data set
# 2. Train a classifier.
# 3. Predict label(class).
# 4. visualize the tree.
iris = load_iris()

print(iris.feature_names)  # features
print(iris.target_names)  # labels
print(iris.data[0])

# Train a classifier


print(iris.target[0])
print(type(iris.target[0]))


# Convert label from int to readable string
def convert_label(target):
    if target[i] == 0:
        feature = str(iris.target_names[0])
    elif target[i] == 1:
        feature = str(iris.target_names[1])
    else:
        feature = str(iris.target_names[1])
    return feature


for i in range(len(iris.target)):
    print("Example %d: label %s, features %s" % (i, convert_label(iris.target), iris.data[i]))

# Separate data, training - testing
# testing data, test classifiers accuracy

# label 1, 2,  3
test_index = [0, 50, 100]

# testing data, test target contains 3 labels at 0, 50, 100
# test data contain inputs at 0, 50, 100
test_target = iris.target[test_index]
test_data = iris.data[test_index]

# training data, with testing data removed
train_target = numpy.delete(iris.target, test_index)
train_data = numpy.delete(iris.data, test_index, axis=0)

# create classifier and train it
classifier = tree.DecisionTreeClassifier()
classifier.fit(train_data, train_target)

print(test_target)
print(classifier.predict(test_data))
print("Predicted labels match testing data: " + str(numpy.array_equiv(test_target, classifier.predict(test_data))))
