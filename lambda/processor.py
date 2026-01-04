import boto3
import urllib.parse

s3 = boto3.client("s3")

OUTPUT_BUCKET = "event-output-bucket-12345"

def lambda_handler(event, context):
    record = event["Records"][0]
    input_bucket = record["s3"]["bucket"]["name"]
    key = urllib.parse.unquote_plus(record["s3"]["object"]["key"])

    # Read input file
    response = s3.get_object(Bucket=input_bucket, Key=key)
    data = response["Body"].read().decode("utf-8")

    # Process data (simple example)
    processed_data = data.upper()

    # Write to output bucket
    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=f"processed-{key}",
        Body=processed_data
    )

    print(f"Processed {key} successfully")

    return {
        "statusCode": 200,
        "message": "File processed and stored"
    }
