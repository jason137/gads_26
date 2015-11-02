from __future__ import print_function

import pandas as pd
import pickle
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

def train_model():
    train = pd.read_csv('sentiment_training.txt', sep='\t')
    vectorizer = CountVectorizer()
    X_train = vectorizer.fit_transform(train.Phrase)

    model = MultinomialNB().fit(X_train, list(train.Sentiment))
    # save the classifier
    with open('model.pkl', 'wb') as fid:
        pickle.dump(model, fid)
    with open('vectorizer.pkl', 'wb') as fid:
        pickle.dump(vectorizer, fid)  

def load_model():
    model = pickle.load(open('model.pkl', 'rb'))
    vec = pickle.load(open('vectorizer.pkl', 'rb'))
    return model, vec

model, vec = load_model()
def is_positive(text):
    test = vec.transform([text])
    return model.predict_proba(test)[0][1]


if __name__ == '__main__':
    sentences_to_eval = [
        "The weather is beautiful today!",
        "The weather is terrible today!"
    ]
    for sentence in sentences_to_eval:
        score = is_positive(sentence)
        print("Sentence: {}, Sentiment Sccore: {}".format(sentence, score))
