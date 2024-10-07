"""
This is script to take a backup from local to AWS S3.
boto3+>used to do AWS tasks using python
"""

import boto3

s3 = boto3.resource("s3")


def show_buckets(s3):
    for bucket in s3.buckets.all():  # this will connect with aws s3
        print(bucket.name)


def create_bucket(s3, bucket_name, region):
    s3, create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": "us-east-1",
        },
    )
    print("bucket created successfully")


create_bucket(s3)
show_buckets(s3)
