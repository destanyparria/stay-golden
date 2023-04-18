import boto3

# Call out the AWS service client
dynamodb = boto3.client('dynamodb')

response = dynamodb.create_table(
    AttributeDefinitions=[
        {
            'AttributeName': 'Season',
            'AttributeType': 'N', #This defines the attribute as a number data type
            
        },
        {
            'AttributeName': 'Episode',
            'AttributeType': 'N'
        }
    ],
    KeySchema=[
        {
            'AttributeName': 'Season', 
            'KeyType': 'HASH', #The HASH keytype is sets "Season" as the partition key
        },
        {
            'AttributeName': 'Episode',
            'KeyType': 'RANGE' #The RANGE keytype sets "Episode" as the sort key
        }
    ],
    ProvisionedThroughput={ 
        'ReadCapacityUnits': 1,
        'WriteCapacityUnits': 1,
    },
    TableName='The_Office', #Gives the table a name
)

print(response)
print("Table status:", response.table_status)