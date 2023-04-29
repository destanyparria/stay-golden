import json
import boto3
import time
import datetime

def lambda_handler(event, content):
  utc_dt = datetime.datetime.now().timestamp()
  utc_hr = time.ctime(utc_dt)
  sqs = boto3.client('sqs', region_name = 'us-east-1')
  sqs.send_message(
    QueueUrl = "https://sqs.us-east-1.amazonaws.com/215911252642/project_queue",
    MessageBody = ("The current date and time is "+ str(utc_hr) + ".")
    )
  return {
    'statusCode': 200,
    'body': json.dumps("The current date and time is "+ str(utc_hr) + ".")
  }