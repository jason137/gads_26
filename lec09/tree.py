#!/usr/bin/env python
import pandas as pd
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.cross_validation import cross_val_score
from pprint import pprint

INPUT_FILE = '../datasets/abalone.csv'
N_FOLDS = 10

def load_data(input_file=INPUT_FILE):

    data = pd.read_csv(input_file)

    # encode categorical feature
    data['gender_M'] = data.gender.apply(lambda k: k == 'M')
    data['gender_F'] = data.gender.apply(lambda k: k == 'F')
    data = data.drop('gender', axis=1)

    return data

def fit_model(data):

    # label = data.rings

    # coarsen prediction task
    median_rings = data.rings.median()
    label = data.rings.apply(lambda k: k >= median_rings)

    features = data.drop('rings', axis=1)

    clf = DTC(max_depth=4)
    scores = cross_val_score(clf, features, label, cv=N_FOLDS)

    print(clf)
    print('cv scores =')
    print(scores)
    print('mean score =', scores.mean())
    print('std score = ', scores.std())

    fitted_tree = clf.fit(features, label)
    print('\nfeature importances:')
    pprint(list(zip(features.columns, fitted_tree.feature_importances_)))

def main():
    data = load_data()
    fit_model(data)

if __name__ == '__main__':
    main()
