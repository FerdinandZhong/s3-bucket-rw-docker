import os
import boto3

aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
bucket_name = os.environ['bucket_name']
s3_file_path = os.environ['s3_file_path']
local_file_path = os.environ['local_file_path']

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

s3.Bucket(bucket_name).download_file(Key=s3_file_path, Filename=local_file_path)
