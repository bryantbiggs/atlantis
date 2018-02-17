# -*- coding: utf-8 -*-
"""
    SNS Helpers
    -----------

    Module contains shared functionality for working with AWS SNS topics

"""

import os
import json
import boto3

SNS_CLIENT = boto3.client("sns", region_name=os.environ.get("REGION", "us-east-1"))

EMIT_MESSAGE_TOPIC = os.environ.get('EMIT_MESSAGE_TOPIC')


def emit_sns_msg(message, topic_arn=EMIT_MESSAGE_TOPIC):
    """Emits an SNS message to a given SNS topic ARN.

    :param message: JSON serializable Python object
    :type message: dict
    :param topic_arn: the topic arn to which to emit the message to
    :type topic_arn: str
    :returs: None
    :rtype: None
    """

    SNS_CLIENT.publish(Message=json.dumps(message), TopicArn=topic_arn)


def get_sns_msg(event):
    """Returns a message object extracted from AWS SNS event.

    :param event: AWS event object
    :type event: dict
    :returns: JSON serialized SNS message object
    :rtype: dict
    """

    return json.loads(event['Records'][0]['Sns']['Message'])
