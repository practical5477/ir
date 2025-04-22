from sklearn.metrics import average_precision_score, precision_recall_curve, auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score
import matplotlib.pyplot as plt
import numpy as np
def calculate_classification_metrics(y_true, y_pred_prob):
    """
    Calculate various classification metrics.

    Parameters:
    - y_true: True labels (ground truth).
    - y_pred_prob: Predicted probabilities for the positive class.

    Returns:
    - Dictionary containing different evaluation metrics.
    """
    # Convert probabilities to binary predictions
    y_pred_binary = (np.array(y_pred_prob) >= 0.5).astype(int)

    # Accuracy
    accuracy = accuracy_score(y_true, y_pred_binary)

    # Precision, Recall, F1 Score
    precision = precision_score(y_true, y_pred_binary)
    recall = recall_score(y_true, y_pred_binary)
    f1 = f1_score(y_true, y_pred_binary)

    # ROC-AUC
    roc_auc = roc_auc_score(y_true, y_pred_prob)

    # Average Precision and Precision-Recall curve
    average_precision = average_precision_score(y_true, y_pred_prob)
    precision_curve, recall_curve, _ = precision_recall_curve(y_true, y_pred_prob)
    area_under_pr_curve = auc(recall_curve, precision_curve)

    # Print metrics
    print(f'Accuracy: {accuracy}')
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 Score: {f1}')
    print(f'ROC-AUC: {roc_auc}')
    print(f'Average Precision: {average_precision}')
    print(f'Area under Precision-Recall curve: {area_under_pr_curve}')

    # Plot Precision-Recall curve
    plt.figure(figsize=(8, 6))
    plt.plot(recall_curve, precision_curve, color='blue', lw=2, label='Precision-Recall curve')
    plt.xlabel('Recall')
    plt.ylabel('Precision')
    plt.title('Precision-Recall Curve')
    plt.legend()
    plt.show()

# Example usage:
# Replace the following placeholders with your actual data

# Example for binary classification
y_true_binary = [1, 0, 1, 0, 1]  # True binary labels (1 for positive, 0 for negative)
y_pred_prob_binary = [0.8, 0.6, 0.9, 0.5, 0.7]  # Predicted probabilities for the positive class

calculate_classification_metrics(y_true_binary, y_pred_prob_binary)
