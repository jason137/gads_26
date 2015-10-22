#!/usr/bin/env python3
import pandas as pd
from sklearn.naive_bayes import MultinomialNB as NB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.cross_validation import cross_val_score

INPUT_FILE = '../datasets/emails.csv'
N_FOLDS = 10

def main(input_file=INPUT_FILE):

    count_vect = CountVectorizer()

    data = pd.read_csv(input_file, sep=',', names=['label', 'text'])

    # NOTE pos record = fraud
    data['bin_target'] = data.label.apply(lambda k: k == 'bad')

    # preproc
    X_train_counts = count_vect.fit_transform(data.text)
    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transformer.transform(X_train_counts)

    # train classifier
    nb = NB()
    cv_scores = cross_val_score(nb, X_train_tf, data.bin_target,
        cv=N_FOLDS) #, scoring='roc_auc')

    print(nb)
    print(cv_scores)
    print(cv_scores.mean())
    print(cv_scores.std())

if __name__ == '__main__':
    main()
