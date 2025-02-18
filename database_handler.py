import uuid
from datetime import datetime

import boto3

from config.environment import Environment

dynamo_db = boto3.client(
    "dynamodb",
    aws_access_key_id=Environment().AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Environment().AWS_SECRET_ACCESS_KEY,
    region_name="sa-east-1"
)

TABLE_NAME = "ai-schedule-events"


def get_user_schedule():
    response = dynamo_db.scan(
        TableName=TABLE_NAME
    )

    return response['Items']


def insert_user_schedule(event):
    item = {
        "id": {"S": str(uuid.uuid4())},
        "title": {"S": event['title']},
        "description": {"S": event['description']},
        "start_time": {"S": event['start_time']},
        "end_time": {"S": event['end_time']},
        "user_id": {"S": event['user_id']},
        "created_at": {"S": datetime.now().isoformat()},
    }

    response = dynamo_db.put_item(
        TableName=TABLE_NAME,
        Item=item
    )

    return response


def update_user_schedule(event):
    item = {
        "id": {"S": event['id']},
        "title": {"S": event['title']},
        "description": {"S": event['description']},
        "start_time": {"S": event['start_time']},
        "end_time": {"S": event['end_time']},
        "user_id": {"S": event['user_id']},
    }

    response = dynamo_db.put_item(
        TableName=TABLE_NAME,
        Item=item
    )

    return response


def delete_user_schedule(id):
    response = dynamo_db.delete_item(
        TableName=TABLE_NAME,
        Key={"id": {"S": id}}
    )

    return response