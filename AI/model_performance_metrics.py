# precision, recall metrics

def calculate_accuracy(y_true, y_pred):
    correct = 0
    total = len(y_true)
    
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == pred_label:
            correct += 1
    
    accuracy = correct / total
    return accuracy

def calculate_precision(y_true, y_pred, positive_label):
    true_positive = 0
    predicted_positive = 0
    
    for true_label, pred_label in zip(y_true, y_pred):
        if pred_label == positive_label:
            predicted_positive += 1
            if true_label == positive_label:
                true_positive += 1
    
    precision = true_positive / predicted_positive
    return precision

def calculate_recall(y_true, y_pred, positive_label):
    true_positive = 0
    actual_positive = 0
    
    for true_label, pred_label in zip(y_true, y_pred):
        if true_label == positive_label:
            actual_positive += 1
            if pred_label == positive_label:
                true_positive += 1
    
    recall = true_positive / actual_positive
    return recall

def calculate_f1_score(y_true, y_pred, positive_label):
    precision = calculate_precision(y_true, y_pred, positive_label)
    recall = calculate_recall(y_true, y_pred, positive_label)
    
    f1_score = 2  *(precision*  recall) / (precision + recall)
    return f1_score

# Example usage
y_true = [0, 1, 0, 1, 1, 0]
y_pred = [0, 1, 1, 1, 0, 0]

accuracy = calculate_accuracy(y_true, y_pred)
precision = calculate_precision(y_true, y_pred, positive_label=1)
recall = calculate_recall(y_true, y_pred, positive_label=1)
f1_score = calculate_f1_score(y_true, y_pred, positive_label=1)

print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1_score)