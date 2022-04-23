import boto3
from botocore.client import Config

s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
response = s3.list_objects_v2(
    Bucket='sesac-sample'
)

# generate_presigned_url
url = s3.generate_presigned_url('get_object', Params={
    'Bucket': 'sesac-sample',
    'Key': 'porche/porche_718.jpg'
})
print(f'{url}')
