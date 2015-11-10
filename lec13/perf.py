#!/usr/bin/env python
from collections import Counter
import pandas as pd

from sklearn.cross_validation import cross_val_score
from sklearn.ensemble import RandomForestClassifier as RF

INPUT_FILE = '../datasets/abalone.csv'
N_FOLDS = 5

def load_data(input_file=INPUT_FILE):

    data = pd.read_csv(input_file)

    # encode categorical feature
    data['gender_F'] = data.gender == 'F'
    data['gender_M'] = data.gender == 'M'

    data = data.drop('gender', axis=1)
    return data

def fit_models(data):

    features = data.drop('rings', axis=1)
    target = data.rings == 23

    print(features.head())
    print(Counter(target))

    model = RF(n_estimators=300, n_jobs=-1)
    cv_acc = cross_val_score(model, features, target, cv=N_FOLDS)
    
    print('\ncv results (acc)\n', cv_acc)
    print('\nmean score =', cv_acc.mean())
    print('std score = ', cv_acc.std())

    cv_roc = cross_val_score(model, features, target, cv=N_FOLDS,
        scoring='roc_auc')

    print('\ncv results (ROC AUC)\n', cv_roc)
    print('\nmean score =', cv_roc.mean())
    print('std score = ', cv_roc.std())

def main():
    data = load_data()
    fit_models(data)

if __name__ == '__main__':
    main()
