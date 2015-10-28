#!/usr/bin/env python
import pandas as pd

from pprint import pprint
from sklearn.tree import DecisionTreeClassifier as DTC
from sklearn.cross_validation import cross_val_score

INPUT_FILE = '../datasets/abalone.csv'
N_FOLDS = 10

def load_data(input_file=INPUT_FILE):
    
    # load data
    data = pd.read_csv(input_file)

    # encode categorical feature
    data['gender_F'] = data.gender.apply(lambda k: k == 'F')
    data['gender_M'] = data.gender.apply(lambda k: k == 'M')
    data = data.drop('gender', axis=1)
    
    return data

def fit_model(data):

    # separate features & labels
    features = data.drop('rings', axis=1)

    # labels = data.rings
    med_rings = data.rings.median()
    labels = data.rings.apply(lambda k: k >= med_rings)

    # init classifier, get cross-validated accuracy results
    clf = DTC(max_depth=4)
    cv_results = cross_val_score(clf, features, labels, cv=N_FOLDS)

    # print cv results
    print(clf)
    print('\ncv results =', cv_results)
    print('\nmean cv accuracy =', cv_results.mean())
    print('std cv accuracy = ', cv_results.std())

    # print feature importances
    print('\nfeature importances =')
    fitted_clf = clf.fit(features, labels)
    pprint(list(zip(data.columns, fitted_clf.feature_importances_)))

def main():

    data = load_data()    
    fit_model(data)

if __name__ == '__main__':
    main()
