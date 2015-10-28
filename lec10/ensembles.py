#!/usr/bin/env python
from collections import Counter
import pandas as pd

from sklearn.cross_validation import cross_val_score
from sklearn.tree import DecisionTreeClassifier as DT
from sklearn.ensemble import (RandomForestClassifier as RF,
    GradientBoostingClassifier as GB)

INPUT_FILE = '../datasets/abalone.csv'
N_FOLDS = 10

def load_data(input_file=INPUT_FILE):

    data = pd.read_csv(input_file)

    # encode categorical feature
    data['gender_F'] = data.gender.apply(lambda k: k == 'F')
    data['gender_M'] = data.gender.apply(lambda k: k == 'M')

    data = data.drop(['gender'], axis=1)
    return data

def fit_models(data):

    features = data.drop('rings', axis=1)
    target = data.rings

    models = DT(), RF(), GB(max_depth=1)

    for model in models:
        cv_results = cross_val_score(model, features, target, cv=N_FOLDS)

        print('\n==========\n', model)
        print('\ncv results\n', cv_results)
        print('\nmean cv accuracy =', cv_results.mean())
        print('std cv accuracy = ', cv_results.std())

def main():
    data = load_data()
    fit_models(data)

if __name__ == '__main__':
    main()
