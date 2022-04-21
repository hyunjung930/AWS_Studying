import boto3

s3 = boto3.client('s3')
response = s3.list_objects_v2(
    Bucket='sesac-sample'
)

for object in response['Contents']:
    print(f'{object["Key"]}, {object["Size"]}')
