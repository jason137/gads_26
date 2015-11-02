from TwitterAPI import TwitterAPI
import urllib
import json

access_token_key = "18370977-aELuTTJ4aGnN51IBMINvD9OM53cvzsBCGsrgXPeh6"
access_token_secret = "mYLFfnnQuqz8sE50mlCCoWjZ1XPlmy2KYeC89p14gxMRU"

api_key = "gc2A4l4WF1pNFHkcTEzKsChRq"
api_secret = "6qp7ZUHESRhuvNUbm8NloEKFpbwNaR9UzD1iVBQFKTVq7UjeVS"

_debug = 0


api = TwitterAPI(api_key, api_secret, access_token_key, access_token_secret)

'''
Construct, sign, and open a twitter request
using the hard-coded credentials above.
'''

def retrieve_tweets(topic):
                    
                    
    """

    Params:
    topic - must be in this format "#topic" or '@handle"
    Returns
    """
    response = api.request('statuses/filter', {'track': topic})
    print(response.status_code)
    for x in response:
        try:
            yield x
        # except JSONParseException as json_error:
        #     raise ValueError("Unable to retrieve valid JSON, please check your API credentials")
        except UnicodeError as unicode_error:
            continue
