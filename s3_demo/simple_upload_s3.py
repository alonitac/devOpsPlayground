import boto3
s3_client = boto3.client('s3')
s3_client.upload_file('../changeMe.txt', 'testbuckeralonit3', 'changeMe.txt')