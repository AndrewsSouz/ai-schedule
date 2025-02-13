import boto3
from config.environment import Environment
from botocore.exceptions import ParamValidationError

dynamo_db = boto3.client(
    "dynamodb",
    aws_access_key_id=Environment().AWS_ACCESS_KEY_ID,
    aws_secret_access_key=Environment().AWS_SECRET_ACCESS_KEY,
    region_name="us-east-2"
)

table_name = "userSchedule"


def insert_user_schedule(schedule):
    print(schedule)
    try:
        response = dynamo_db.put_item(
            TableName=table_name,
            Item={
                "id": {"N": str(schedule["user_id"])},  # "N" para Number
                "user_id": {"N": str(schedule["user_id"])},  # "N" para Number
                "schedule": {"S": schedule["schedule"]}   # "S" para String
            }
        )
        return response
    except ParamValidationError as e:
        print(f"Erro de validação: {e}")
        return {"error": str(e)} # Retorna um dicionário com o erro para tratamento
    except Exception as e: # Captura outros erros
        print(f"Erro ao inserir item: {e}")
        return {"error": str(e)}
