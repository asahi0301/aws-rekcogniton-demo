import boto3

rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')


# Change here!
table = dynamodb.Table('rekognition-demo-0301')
collection = "test-collection"
bucket = "rekognition-demo-0301"
keys = ["search-pics/face1.jpeg", "search-pics/face2.jpeg"]

for key in keys:
    response = rekognition.search_faces_by_image(
        CollectionId=collection,
        Image={
            'S3Object': {
                'Bucket': bucket,
                'Name': key
            }
        },
        MaxFaces=1000,
        FaceMatchThreshold=80
    )
    lists = response['FaceMatches']
    print 'Number of matched faces: {}'.format(len(lists))
    for list in lists:
        faceid = list['Face']['FaceId']
        print 'FaceId: {}'.format(faceid)
        result = table.get_item(
            Key={
                 "FaceId": faceid
            }
        )
        item = result['Item']
        print 'ImageId: {}'.format(item['ImageId'])
        print 'Bucket: {}'.format(item['Bucket'])
        print 'Key: {}'.format(item['Key'])
        print '--------------------------------'
        #print 'ImageId: {}'.format(item['Raw'])
    print "######################################"