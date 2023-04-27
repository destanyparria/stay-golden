import json
import boto3
from datetime import datetime 


current_date_time = datetime.now()
sqs = boto3.client('sqs', region_name='us-east-1')


def lambda_handler(event, content):
    
    #Get the queue
    queue = sqs.get_queue_by_name(QueueName='project_queue')
    
    #Call out the current date and time at the time of trigger
    date_time = current_date_time.strftime("%d/%m/%Y %H:%M:%S") 
    
    #Create a message string that we will call later 
    time_message = ("The current date and time is " + str(date_time) + ".")
    
    response = queue.send_message(MessageBody = time_message)   
    
    return {
        "StatusCode": 200,
        'body': json.dumps(time_message)
    }