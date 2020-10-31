import os
import boto3

aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
bucket_name = os.environ['bucket_name']
s3_file_path = os.environ['s3_file_path']
local_dir = os.environ['local_dir']
local_file_name = os.environ['local_file_name']

local_file_path = '%s/%s' % (local_dir, local_file_name)

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

os.makedirs(local_dir, exist_ok=True)


s3.Bucket(bucket_name) \
    .Object(s3_file_path) \
    .download_file(local_file_path)

