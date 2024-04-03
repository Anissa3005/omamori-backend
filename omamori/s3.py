import boto3
import logging

from botocore.exceptions import ClientError

# s3 = boto3.client('s3')

# my_object = s3.list_objects_v2(Bucket='omamori-finder-images')

# for object in my_object['Contents']:
#     print(object['Key'])


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


print(create_presigned_url(bucket_name='omamori-finder-images',
                           object_name='media/study_omamori.jpg'))
