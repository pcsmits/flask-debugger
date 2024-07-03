from flask import Blueprint, current_app, request

import boto3
from botocore.exceptions import ClientError

s3 = Blueprint('s3', __name__)

@s3.route('/s3', methods=['GET', 'POST'])
def s3_main():
    bucket = request.args.get('bucket', "No 'bucket' provided")
    client = boto3.client('s3')
    
    if bucket == "No 'bucket' provided": 
        print(f"Bucket: {bucket}")
        list_bucket_msg = list_buckets(client)
        return f"->{list_bucket_msg}"
    else:
        print(f"Bucket: {bucket}")
        list_bucket_msg = list_buckets(client)
        obj_msg = list_bucket_objects(client, bucket)
        return f"->{list_bucket_msg}\n{obj_msg}"


    


def list_buckets(client):
    # Establish the connection
    try:
        print("listing buckets")
        return client.list_buckets()
    except Exception as e:
        return f'Error: Unable to connect to the s3: {e}'


def list_bucket_objects(client, bucket):
    # Establish the connection
    contents = "<br><br>" + "S3 Objects:" + "<br>" + "---------------------------"
    try:
        print("listing bucket objects")
        for key in client.list_objects(Bucket=bucket)['Contents']:
            print(key['Key'])
            contents = contents + "<br>" + key['Key']
        return contents
    except Exception as e:
        return f'Error: Unable to connect to the s3: {e}'
