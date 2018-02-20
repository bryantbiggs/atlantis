# -*- coding: utf-8 -*-
"""
    DB Upload
    ---------

    Module contains functionality used to upload records to a PostgreSQL database

"""

import os
import csv

import boto3
from psycopg2.extensions import AsIs

from .sns_helpers import get_sns_msg, emit_sns_msg
from .db_helpers import yield_db_cursor
from .s3_helpers import get_s3_file

#: S3 resource to interact with S3 objects
S3_RESOURCE = boto3.resource("s3")

#: S3 bucket where uploaded files reside
S3_BUCKET = os.environ.get("S3_BUCKET")

COLS = ["customer_id", "first_name", "last_name", "street_address",
        "state", "zip_code", "purchase_status", "product_id",
        "product_name", "cost", "transaction_date"]


def upsert_customer(records):
    """Upsert records in the `customer` database table.

    :param records: records to extract customer attributes and upsert
    :type records: list[dict]
    :returns: None
    :rtype: None
    """
    upsert = """INSERT INTO subscriptions.customer(%s) VALUES %s
                ON CONFLICT (id)
                DO UPDATE SET (%s) = %s WHERE customer.id = %s;"""

    cols = ["customer_id", "first_name", "last_name", "street_address", "state", "zip_code"]
    recs = [{key: val for key, val in rec.items() if key in cols} for rec in records]

    for rec in recs:
        keys = tuple([key if (key != "customer_id") else "id" for key in rec.keys()])
        values = tuple(rec.values())
        with yield_db_cursor() as cur:
            mogged = cur.mogrify(upsert, (AsIs(", ".join(keys)), values,
                                          AsIs(", ".join(keys[1:])), values[1:], values[0]))
            cur.execute(mogged)


def upsert_product(records):
    """Upsert records in the `product` database table.

    :param records: records to extract product attributes and upsert
    :type records: list[dict]
    :returns: None
    :rtype: None
    """
    upsert = """INSERT INTO subscriptions.product(%s) VALUES %s
                ON CONFLICT (id)
                DO UPDATE SET (%s) = %s WHERE product.id = %s;"""

    cols = ["product_id", "product_name", "cost"]
    recs = [{key: val for key, val in rec.items() if key in cols} for rec in records]
    for rec in recs:
        keys = tuple([key if (key != "product_id") else "id" for key in rec.keys()])
        values = tuple(rec.values())
        with yield_db_cursor() as cur:
            mogged = cur.mogrify(upsert, (AsIs(", ".join(keys)), values,
                                          AsIs(", ".join(keys[1:])), values[1:], values[0]))
            cur.execute(mogged)


def insert_transactions(records):
    """Insert records into `transactions` database table.

    :param records: all records to be inserted into database table
    :type records: list[dict]
    :returns: None
    :rtype: None
    """
    insert = """INSERT INTO subscriptions.sales(%s) VALUES %s
                ON CONFLICT DO NOTHING;"""
    cols = ["customer_id", "product_id", "purchase_status", "transaction_date"]
    recs = [{key: val for key, val in rec.items() if key in cols} for rec in records]

    for rec in recs:
        keys = tuple(rec.keys())
        values = tuple(rec.values())
        with yield_db_cursor() as cur:
            mogged = cur.mogrify(insert, (AsIs(", ".join(keys)), values))
            cur.execute(mogged)


def upload_records(event, _):
    """Upload records contained within S3 file."""

    message = get_sns_msg(event)
    file_name = message["s3_file_uploaded"]
    s3_file = get_s3_file(s3_key=f"data/{file_name}", s3_bucket=S3_BUCKET)

    records = [dict(rec) for rec in csv.DictReader(s3_file, fieldnames=COLS, delimiter="\t")]
    upsert_customer(records)
    upsert_product(records)
    insert_transactions(records)
    return emit_sns_msg(message={"db_records_uploaded": file_name})
