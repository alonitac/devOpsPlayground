import boto3
s3_client = boto3.client('C:\Users\lets_\s3')
s3_client.upload_file('main.py', 'abeerbucket', 'main.py')



