import json

def lambda_handler(event, context):
    print("New data received")
    print(json.dumps(event))
  
    return {
        "statusCode": 200,
        "body": "Data processed successfully"
    }
