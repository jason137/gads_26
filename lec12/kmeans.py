#!/usr/bin/env python3
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

INPUT_FILE = '../datasets/iris.csv'

K_VECTOR = range(2, 11)

def main(input_file=INPUT_FILE):

    data = pd.read_csv(input_file)
    features = data.drop('species', axis=1)

    for k in K_VECTOR:

        kmeans = KMeans(n_clusters=k)
        kmeans.fit(features)

        labels = kmeans.labels_
        sc = silhouette_score(features, labels)

        print(k, sc)

if __name__ == '__main__':
    main()
