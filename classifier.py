from sklearn import tree

# This is an example of a simple classifier using supervised learning.

# features = inputs, labels = outputs
# 1 - smooth, 0 - bumpy
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = ["apple", "apple", "orange", "orange"]

# decision Tree
# classifier, collection of rules

classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(features, labels)

print(classifier.predict([[150, 0]]))
