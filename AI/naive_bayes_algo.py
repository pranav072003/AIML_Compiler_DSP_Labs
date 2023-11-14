import numpy as np

# Define the Naïve Bayes algorithm
def naive_bayes(X_train, y_train, X_test):
    # Calculate class probabilities
    classes, class_counts = np.unique(y_train, return_counts=True)
    class_probs = class_counts / len(y_train)
    
    # Calculate feature probabilities
    feature_probs = []
    for i in range(X_train.shape[1]):
        feature_values = np.unique(X_train[:, i])
        feature_prob = []
        for c in classes:
            X_c = X_train[y_train == c]
            feature_prob_c = []
            for v in feature_values:
                feature_prob_c.append(np.sum(X_c[:, i] == v) / len(X_c))
            feature_prob.append(feature_prob_c)
        feature_probs.append(feature_prob)
    
    # Make predictions
    y_pred = []
    for x in X_test:
        class_scores = []
        for c in classes:
            class_score = np.log(class_probs[c])
            for i, v in enumerate(x):
                feature_prob = feature_probs[i][c]
                if v in feature_values:
                    class_score += np.log(feature_prob[feature_values == v][0])
            class_scores.append(class_score)
        y_pred.append(classes[np.argmax(class_scores)])
    
    return y_pred

# Generate random data
np.random.seed(42)
X_train = np.random.rand(100, 2)  # Training data
y_train = np.random.randint(0, 2, 100)  # Training labels
X_test = np.random.rand(20, 2)  # Test data

# Run the Naïve Bayes algorithm
y_pred = naive_bayes(X_train, y_train, X_test)

print("Predicted labels:", y_pred)