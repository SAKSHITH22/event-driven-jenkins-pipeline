def lambda_handler(event, context):
    print("Generating daily report...")
    return {
        "statusCode": 200,
        "message": "Daily report generated"
    }
