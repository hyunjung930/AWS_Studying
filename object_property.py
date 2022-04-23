import boto3

s3 = boto3.client('s3')

response = s3.get_object_attributes(
    Bucket='sesac-sample',
    Key='ev6_1.jpeg',
    ObjectAttributes=[
        'ObjectSize', 'ETag', ''
    ]
)
print(f' object property : {response}')
