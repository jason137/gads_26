#!/usr/bin/env python
import pandas as pd
from sklearn.cross_validation import cross_val_score
from sklearn.linear_model import LogisticRegression

INPUT_FILE = '../datasets/beer.tsv'
NUM_FOLDS = 10

def stouter(k):
    """cast target variable to integer binary value"""

    try:
        return int('Stout' in k)

    except TypeError:   # this chokes on blanks
        return 0

def load_data(input_file):
    """load data, preprocess"""

    data = pd.read_csv(input_file, sep='\t')
    print('shape before dropping NAs:', data.shape)
    data = data.dropna()
    print('shape after dropping NAs:', data.shape)

    data['is_Stout'] = data['Type'].apply(stouter)
    return data

def fit_model(data):
    """perform CV'd fit & output results"""

    model = LogisticRegression()
    features = data[['ABV', 'WR']]  # only numerics!
    target = data['is_Stout']       # 1/0

    scores = cross_val_score(model, features, target,
        cv=NUM_FOLDS)

    print('\nCVd genlzn acc: ', '\n', scores)
    print('\navg genlzn acc: ', scores.mean())

def main(input_file=INPUT_FILE):
    data = load_data(input_file)
    fit_model(data)

if __name__ == '__main__':
    main()
