import boto3

rekognition = boto3.client('rekognition')

response = rekognition.delete_collection(
    CollectionId='test-collection'
)

print response


response = rekognition.list_collections(
    MaxResults=123
)

print response