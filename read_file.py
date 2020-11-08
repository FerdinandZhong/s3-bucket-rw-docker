import os
import boto3

aws_access_key_id = os.environ['AWS_ACCESS_KEY_ID']
aws_secret_access_key = os.environ['AWS_SECRET_ACCESS_KEY']
bucket_name = os.environ['BUCKET_NAME']
remote_model_path = os.environ['REMOTE_MODEL_PATH']
local_model_dir = os.environ['LOCAL_MODEL_DIR']
local_model_name = os.environ['LOCAL_MODEL_NAME']

local_model_path = '%s/%s' % (local_model_dir, local_model_name)

s3_resource = boto3.resource(
    service_name='s3',
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

model_path = '%s/%s' % (local_model_dir, local_model_name)
os.makedirs(model_path, exist_ok=True)

def downloadDirectoryFroms3(s3_resource, bucket_name, remote_model_path):
    bucket = s3_resource.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix = remote_model_path):
        if not obj.key.endswith('/'):
            print('downloading %s to %s/%s' % (obj.key, model_path, os.path.basename(obj.key)))
            bucket.Object(obj.key) \
                .download_file('%s/%s' % (model_path, os.path.basename(obj.key)))

downloadDirectoryFroms3(s3_resource, bucket_name, remote_model_path)

