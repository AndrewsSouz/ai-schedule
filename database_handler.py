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

TABLE_NAME = "ai-service-schedule"


def insert_user_schedule(schedule):
    item = {
        "id": {"S": str(uuid.uuid4())},  # Gera um UUID e armazena como string
        "date":{"S": datetime.now().strftime("%Y-%m-%d")},  # Armazena a data atual como string
        "schedule": {"S": schedule}  # Mantém o schedule como string
    }

    response = dynamo_db.put_item(
        TableName=TABLE_NAME,
        Item=item
    )

    return response


def get_user_schedule():
    response = dynamo_db.scan(
        TableName=TABLE_NAME
    )

    return response['Items']