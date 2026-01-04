import json
import boto3

s3 = boto3.client("s3")

OUTPUT_BUCKET = "event-output-bucket-12345"

def lambda_handler(event, context):
    print("Event received:", json.dumps(event))

    # Get uploaded file details
    record = event["Records"][0]
    input_bucket = record["s3"]["bucket"]["name"]
    input_key = record["s3"]["object"]["key"]

    print(f"Processing file: {input_key} from bucket: {input_bucket}")

    # Read input file
    response = s3.get_object(Bucket=input_bucket, Key=input_key)
    content = response["Body"].read().decode("utf-8")

    # Simple processing
    processed_content = content.upper()

    # Write output file
    output_key = f"processed-{input_key}"
    s3.put_object(
        Bucket=OUTPUT_BUCKET,
        Key=output_key,
        Body=processed_content
    )

    print(f"Processed file written to {OUTPUT_BUCKET}/{output_key}")

    return {
        "statusCode": 200,
        "message": "File processed successfully"
    }
