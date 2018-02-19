# -*- coding: utf-8 -*-
"""
    S3 File
    -------

    Module contains functionality used to interact with files uploaded to an S3 bucket

"""

from sns_helpers import emit_message


def notify_file_upload(event, _):
    """Notify via SNS topic message when a file is uploaded to S3."""

    file_name = event["path"]["file_name"]

    if file_name:
        print(f"Emitting file upload for {file_name}")
        emit_message(message={"s3_file_uploaded": file_name})
