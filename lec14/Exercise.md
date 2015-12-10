https://console.aws.amazon.com/machinelearning/home?region=us-east-1#/
## Exercise
1) Follow the steps we saw in class to create a ML model and evaluation:  
- In AWS console, click on AmazonML and click on “get started” 
	and lunch standard setup.
- Use AmzaonML Tutorial as reference - http://docs.aws.amazon.com/machine-learning/latest/dg/tutorial.html
- Input Data: 
  in s3 location put: aml-sample-data/banking.csv

2) Create a Real Time Prediction Endpoint (API):
- Setup the endpoint: 
  http://docs.aws.amazon.com/machine-learning/latest/dg/requesting-real-time-predictions.html
- Create Access Keys:  
  In the right corner select "Your Name", and then "Security Credentials"
  Now on the left hand side select Users
  Here you can create a user by selecting Create User. Create a user with your name. When prompted 
  download the credentials.csv file
  Click on the User you just created, and click on 'Attach Policy'. From the list of policies select AdministratorAccess  
  and click attach policy on the bottom right.
- Configure the Access Keys:   
  Create your credentials file at ~/.aws/credentials with the following text:
    
  [default]  
  aws_access_key_id = YOUR_ACCESS_KEY_ID  
  aws_secret_access_key = YOUR_SECRET_ACCESS_KEY  
  
- pip install boto3
- Download and run ml_sample.py, try to add new fields to the Record
