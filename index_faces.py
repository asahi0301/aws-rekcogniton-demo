import boto3
import sys
import time
import json

args = sys.argv

s3 = boto3.client('s3')
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')


# Change here!
table = dynamodb.Table('rekognition-demo-0301')

def upload_to_s3(file, bucket, key):
    s3.upload_file(file, bucket, key)
    
def index_faces(collection, bucket, key):

    response = rekognition.index_faces(
        CollectionId=collection,
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        DetectionAttributes=[
            'ALL',
        ]
    )
    return response
    
    
def put_dynamodb(table, lists, bucket, key):
    for face in lists['FaceRecords']:
         table.put_item(
            Item={
                "FaceId":  face['Face']['FaceId'],
                "ImageId":  face['Face']['ImageId'],
                "CreatedAt": int(time.time()),
                "Bucket": bucket,
                "Key": key,
                "Raw": json.dumps(face)
           }
        )
    

file = args[1]
key = args[1]

# Change here!
bucket = "rekognition-demo-0301"
collection = 'test-collection'

upload_to_s3(file, bucket, key)
results = index_faces(collection, bucket, key)
put_dynamodb(table, results, bucket, key)