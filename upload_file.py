import boto3

s3 = boto3.client('s3')
response = s3.put_object(
    Body='mercedes-slc.jpeg',
    Bucket='sesac-sample',
    Key='mercedes/slc.jpeg'
)
print(response)