import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

#Connect with the table
table = dynamodb.Table('The_Office_Episodes')

#Add the items to our table
with table.batch_writer() as batch: 
    batch.put_item(
        Item={
            'Season': 1,
            'Episode': 'Basketball'
        }
    )
    batch.put_item(
        Item={
            'Season': 1,
            'Episode': 'The Dundies'
        }
    )
    batch.put_item(
        Item={
            'Season': 3,
            'Episode': 'The Merger'
        }
    )
    batch.put_item(
        Item={
            'Season': 3,
            'Episode': 'Business School'
        }
    )
    batch.put_item(
        Item={
            'Season': 4,
            'Episode': 'Dinner Party'
        }
    )
    batch.put_item(
        Item={
            'Season': 4,
            'Episode': 'Goodbye, Toby Part 2'
        }
    )
    batch.put_item(
        Item={
            'Season': 5,
            'Episode': 'The Michael Scott Paper Company'
        }
    )
    batch.put_item(
        Item={
        'Season': 5,
        'Episode': 'Broke'
        }
    )
    batch.put_item(
        Item={
            'Season': 5,
            'Episode': 'Company Picnic'
        }
    )
    batch.put_item(
        Item={
            'Season': 6,
            'Episode': 'Niagra Part 2'
        }
    )
        
print("Added Items")