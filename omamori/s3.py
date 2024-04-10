import boto3
import logging
import os

from botocore.exceptions import ClientError
from dotenv import load_dotenv

load_dotenv()


def create_credentials():
    client = boto3.client('sts')

    response = client.assume_role(
        RoleArn=os.environ['AWS_ROLE_ARN'],
        RoleSessionName=os.environ['AWS_ROLE_SESSION_NAME'],
    )

    temporary_credentials = {
        'AccessKeyId': response['Credentials']['AccessKeyId'],
        'SecretAccessKey': response['Credentials']['SecretAccessKey'],
        'SessionToken': response['Credentials']['SessionToken']
    }

    return temporary_credentials


def get_bucket_name():

    credentials = create_credentials()

    access_key = credentials['AccessKeyId']
    secret_key = credentials['SecretAccessKey']
    session = credentials['SessionToken']

    client = boto3.client(
        's3',
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session
    )

    response = client.list_buckets()

    print(response['Buckets'])
    return


get_bucket_name()


# def get_all_images():
#     s3 = boto3.client('s3')
#     bucket = 'omamori-finder-images'

#     my_objects = s3.list_objects_v2(Bucket='omamori-finder-images')

#     presigned_urls = []

#     for object in my_objects['Contents']:
#         presigned_urls.append(create_presigned_url(
#             bucket_name=bucket, object_name=object['Key']))

#     return presigned_urls


# def create_presigned_url(bucket_name, object_name, expiration=3600):
#     """Generate a presigned URL to share an S3 object

#     :param bucket_name: string
#     :param object_name: string
#     :param expiration: Time in seconds for the presigned URL to remain valid
#     :return: Presigned URL as string. If error, returns None.
#     """

#     # Generate a presigned URL for the S3 object
#     s3_client = boto3.client('s3')
#     try:
#         response = s3_client.generate_presigned_url('get_object',
#                                                     Params={'Bucket': bucket_name,
#                                                             'Key': object_name},
#                                                     ExpiresIn=expiration)
#     except ClientError as e:
#         logging.error(e)
#         return None

#     # The response contains the presigned URL
#     return response
