import boto3
import uuid

# Instantiate a new client for Amazon Simple Storage Service (S3). With no
# parameters or configuration, the AWS SDK for Python (Boto) will look for
# access keys in these environment variables:
#
#    AWS_ACCESS_KEY_ID='...'
#    AWS_SECRET_ACCESS_KEY='...'
#
# For more information about this interface to Amazon S3, see:
# http://boto.readthedocs.org/en/latest/s3_tut.html


client = boto3.client('machinelearning', region_name='us-east-1')

response = client.predict(
    ## TODO: change to your modelId. Try to add additional fields to Record
    MLModelId='ml-1MHS3Nc5AZW', 
    Record={
        'age': '44'
    },
    
    ## TODO: change to your endpoint
    PredictEndpoint='https://realtime.machinelearning.us-east-1.amazonaws.com'
)

print (response)
