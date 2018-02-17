# -*- coding: utf-8 -*-
"""
    S3 File
    -------

    Module contains functionality used to interact with files uploaded to an S3 bucket

"""

from sns_helpers import emit_sns_msg


def file_added(event, _):
    """Notify via SNS topic message when a file is uploaded to S3."""

    file_name = event["path"]["file_name"]
    if file_name:
        print(f"[SUCCESS] Emitting SNS message for {file_name}.")
        return emit_sns_msg(message={"s3_file_uploaded": file_name})

    print(f"[ERROR] No file found in API url.")
