import boto3
import logging

from botocore.exceptions import ClientError


def get_all_images():
    s3 = boto3.client('s3')
    bucket = 'omamori-finder-images'

    my_objects = s3.list_objects_v2(Bucket='omamori-finder-images')

    presigned_urls = []

    for object in my_objects['Contents']:
        presigned_urls.append(create_presigned_url(
            bucket_name=bucket, object_name=object['Key']))

    return presigned_urls


def create_presigned_url(bucket_name, object_name, expiration=3600):
    """Generate a presigned URL to share an S3 object

    :param bucket_name: string
    :param object_name: string
    :param expiration: Time in seconds for the presigned URL to remain valid
    :return: Presigned URL as string. If error, returns None.
    """

    # Generate a presigned URL for the S3 object
    s3_client = boto3.client('s3')
    try:
        response = s3_client.generate_presigned_url('get_object',
                                                    Params={'Bucket': bucket_name,
                                                            'Key': object_name},
                                                    ExpiresIn=expiration)
    except ClientError as e:
        logging.error(e)
        return None

    # The response contains the presigned URL
    return response


print(get_all_images())
