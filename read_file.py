import os
import boto3

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = os.environ['BUCKET_NAME']
remote_model_path = os.environ['REMOTE_MODEL_PATH']
local_model_dir = os.environ['LOCAL_MODEL_DIR']
local_model_name = os.environ['LOCAL_MODEL_NAME']

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

