# -*- coding: utf-8 -*-
"""
    S3 Helpers
    ----------

    Module contains shared functionality for working with AWS S3 buckets

"""

import os
import codecs

import boto3

#: S3 resource to interact with S3 objects
S3_RESOURCE = boto3.resource("s3")

#: S3 bucket where uploaded files reside
S3_BUCKET = os.environ.get("S3_BUCKET")


def get_s3_file(s3_key, s3_bucket=S3_BUCKET):
    """Retrieve file from S3 bucket and.

    :param s3_key: file name of scoped file within S3 bucket
    :type s3_key: str
    :param s3_bucket: AWS S3 bucket which contains file
    :type s3_bucket: str
    :returns: file stream of S3 file retrieved
    :rtype: encodings.utf_8.StreamReader
    """
    s3_obj = S3_RESOURCE.Object(bucket_name=S3_BUCKET, key=s3_key)
    response = s3_obj.get()
    return codecs.getreader("utf-8")(response["Body"])
