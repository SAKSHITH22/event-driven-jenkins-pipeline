import json
import boto3
import urllib.parse

s3 = boto3.client("s3")
OUTPUT_BUCKET = "event-output-bucket-12345"

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    record = event["Records"][0]
    input_bucket = record["s3"]["bucket"]["name"]
    object_key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

    response = s3.get_object(Bucket=input_bucket, Key=object_key)
    content = response["Body"].read().decode("utf-8")

    processed_content = content.upper()
    output_key = f"processed-{object_key}"

    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=processed_content
    )

    print(f"Stored file: {OUTPUT_BUCKET}/{output_key}")

    return {
        "statusCode": 200,
        "message": "File processed and stored successfully"
    }
