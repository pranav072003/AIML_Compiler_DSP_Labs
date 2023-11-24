#decision tree

import numpy as np

class DecisionTreeNode:
    def __init__(self, feature=None, value=None, left=None, right=None, class_label=None):
        self.feature = feature
        self.value = value
        self.left = left
        self.right = right
        self.class_label = class_label

def calculate_gini_index(y):
    classes = np.unique(y)
    n_instances = len(y)
    gini_index = 0.0
    
    for c in classes:
        p = np.sum(y == c) / n_instances
        gini_index += p * (1 - p)
    
    return gini_index

def split_dataset(X, y, feature, value):
    left_X, left_y = X[X[:, feature] < value], y[X[:, feature] < value]
    right_X, right_y = X[X[:, feature] >= value], y[X[:, feature] >= value]
    return left_X, left_y, right_X, right_y

def find_best_split(X, y):
    best_gini_index = np.inf
    best_feature = None
    best_value = None
    
    for feature in range(X.shape[1]):
        for value in np.unique(X[:, feature]):
            left_X, left_y, right_X, right_y = split_dataset(X, y, feature, value)
            gini_index = (len(left_y)  *calculate_gini_index(left_y) + len(right_y)*  calculate_gini_index(right_y)) / len(y)
            
            if gini_index < best_gini_index:
                best_gini_index = gini_index
                best_feature = feature
                best_value = value
    
    return best_feature, best_value

def build_decision_tree(X, y, max_depth):
    if max_depth == 0 or len(np.unique(y)) == 1:
        class_label = np.argmax(np.bincount(y))
        return DecisionTreeNode(class_label=class_label)
    
    feature, value = find_best_split(X, y)
    left_X, left_y, right_X, right_y = split_dataset(X, y, feature, value)
    
    left_node = build_decision_tree(left_X, left_y, max_depth - 1)
    right_node = build_decision_tree(right_X, right_y, max_depth - 1)
    
    return DecisionTreeNode(feature=feature, value=value, left=left_node, right=right_node)

def predict(instance, node):
    if node.class_label is not None:
        return node.class_label
    
    if instance[node.feature] < node.value:
        return predict(instance, node.left)
    else:
        return predict(instance, node.right)

# Example usage
X = np.array([[2.5, 1.5], [1.5, 2.5], [3.5, 4.5], [4.5, 3.5]])
y = np.array([0, 0, 1, 1])

tree = build_decision_tree(X, y, max_depth=2)

instance = np.array([2.0, 2.0])
prediction = predict(instance, tree)
print("Prediction:", prediction)
