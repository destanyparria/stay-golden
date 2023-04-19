import boto3

#Connect with the table
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
table = dynamodb.Table('The_Office_Episodes')

#Calls out the scan request for items
response = table.scan()
data = response['Items']

#Creates a loop to scan through the items in the list
while 'Last Evaluated Key' in response:
    response = table.scan(ExclusiveStartKey=response['LastEvaluatedKey'])
    data.extended(response['Items'])
    
print("Scan Complete")
