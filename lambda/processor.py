import boto3

s3 = boto3.client("s3")
OUTPUT_BUCKET = "event-output-bucket-12345"

def lambda_handler(event, context):
    print("Event received:", event)

    for record in event["Records"]:
        input_bucket = record["s3"]["bucket"]["name"]
        input_key = record["s3"]["object"]["key"]

        # Read file from input bucket
        response = s3.get_object(Bucket=input_bucket, Key=input_key)
        content = response["Body"].read()

        # Write processed file to output bucket
        s3.put_object(
            Bucket=OUTPUT_BUCKET,
            Key=f"processed-{input_key}",
            Body=content.upper()
        )

    return {
        "statusCode": 200,
        "message": "File processed and stored successfully"
    }
