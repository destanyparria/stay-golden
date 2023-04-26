import boto3

#Create a SQS client with the service name
sqs = boto3.client('sqs') 

#Create the SQS Queue and give it a name
response = sqs.create_queue(
    QueueName='project_queue'
)

response = sqs.get_queue_url(
    QueueName='project_queue'
)

url = response['QueueUrl']

print('Queue created')
print(url)