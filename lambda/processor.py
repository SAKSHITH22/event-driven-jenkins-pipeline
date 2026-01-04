import json
import boto3
import urllib.parse

s3 = boto3.client('s3')

OUTPUT_BUCKET = "event-output-bucket-12345"

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Get uploaded file details
    record = event['Records'][0]
    input_bucket = record['s3']['bucket']['name']
    input_key = urllib.parse.unquote_plus(record['s3']['object']['key'])

    # Read file from input bucket
    response = s3.get_object(Bucket=input_bucket, Key=input_key)
    file_content = response['Body'].read().decode('utf-8')

    # Simple processing
    processed_content = f"Processed content:\n{file_content}"

    # Write to output bucket
    output_key = f"processed-{input_key}"
    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=processed_content
    )

    print(f"File written to {OUTPUT_BUCKET}/{output_key}")

    return {
        "statusCode": 200,
        "message": "File processed successfully"
    }
