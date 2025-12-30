resource "aws_s3_bucket" "input_bucket" {
  bucket = "event-input-bucket-12345"
}

resource "aws_s3_bucket" "output_bucket" {
  bucket = "event-output-bucket-12345"
}

resource "aws_cloudwatch_log_group" "lambda_logs" {
  name              = "/aws/lambda/event-processor"
  retention_in_days = 7
}