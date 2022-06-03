### Helper Functions

## Functions to avoid repeating code

# a few imports

import sklearn
from sklearn.metrics import confusion_matrix, accuracy_score, precision_recall_fscore_support

def calculate_results(y_true, y_pred):
    """
    Calculates model accuracy, precision, recall and f1-score of binary classification model.
    
    Args:
        y_true: true labels in the form of a 1D array
        y_pred: predicted labels in the form of a 1D array
    """
    
    # Calculate model accuracy
    model_accuracy = accuracy_score(y_true, y_pred)*100
    
    # calculate model precision, recall and f1-score using 'weighted average'
    model_precision, model_recall, model_f1, _ = precision_recall_fscore_support(y_true, y_pred, average='weighted')
    model_results = {'accuracy': model_accuracy,
                    'precision': model_precision,
                    'recall': model_recall,
                    'f1': model_f1}
    
    return model_results