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
resource "aws_s3_bucket_notification" "input_trigger" {
  bucket = aws_s3_bucket.input_bucket.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.processor_lambda.arn
    events              = ["s3:ObjectCreated:*"]
  }

  depends_on = [aws_lambda_permission.allow_s3_invoke]
}

