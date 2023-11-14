import numpy as np

def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2)**2))

def knn(X_train, y_train, X_test, k):
    y_pred = []
    
    for test_point in X_test:
        distances = []
        
        for train_point in X_train:
            distance = euclidean_distance(test_point, train_point)
            distances.append(distance)
        
        # Get the indices of the k nearest neighbors
        indices = np.argsort(distances)[:k]
        
        # Get the labels of the k nearest neighbors
        k_nearest_labels = [y_train[i] for i in indices]
        
        # Predict the label based on majority voting
        pred_label = max(set(k_nearest_labels), key=k_nearest_labels.count)
        y_pred.append(pred_label)
    
    return y_pred

X_train = np.random.rand(100, 2)
y_train = np.random.randint(0, 2, 100)
X_test = np.random.rand(20, 2)

k = 2  # Number of neighbors to consider

# Run the KNN algorithm
y_pred = knn(X_train, y_train, X_test, k)

print("Predicted labels:", y_pred)