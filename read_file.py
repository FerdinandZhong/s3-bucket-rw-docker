import os
import boto3

aws_access_key_id = os.environ['aws_access_key_id']
aws_secret_access_key = os.environ['aws_secret_access_key']
bucket_name = os.environ['bucket_name']
remote_model_path = os.environ['remote_model_path']
local_model_dir = os.environ['local_model_dir']
local_model_name = os.environ['local_model_name']

local_model_path = '%s/%s' % (local_model_dir, local_model_name)

s3 = boto3.resource(
    service_name='s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

os.makedirs(local_model_dir, exist_ok=True)


s3.Bucket(bucket_name) \
    .Object(remote_model_path) \
    .download_file(local_model_path)

