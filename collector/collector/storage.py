import boto3

from collector.config import settings


def get_bucket():
    s3 = boto3.resource("s3")
    bucket = s3.Bucket(settings.IMAGE_BUCKET)
    return bucket


def get_file_url(bucket, image_name):
    url = f"https://{bucket.name}.s3.amazonaws.com/{image_name}"
    return url
