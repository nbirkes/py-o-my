import json
import person
import boto3

client = boto3.client('s3')

tony = person.Person('Tony', 'Soprano')

# response = client.put_object()

print(json.dumps(tony.__dict__))
