from __future__ import print_function

import twitter

if __name__ == '__main__':
    results = twitter.retrieve_tweets(topic='weather')
    # The dictionary key we are interested in 'text', 
    # to access it we can use our dictionary syntax d['text']
    for result in results:
        print(result)
        # For each tweet, evaluate whether it is POSITIVE
        # (by applying the model) and then if it is above
        # some threshold, print it out, i.e. 
        # if is_positive(tweet) > 0.1 print it
