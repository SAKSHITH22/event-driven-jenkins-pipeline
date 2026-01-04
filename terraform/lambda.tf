resource "aws_lambda_function" "processor_lambda" {
  function_name = "event-processor"
  runtime       = "python3.10"
  handler       = "processor.lambda_handler"
  role          = aws_iam_role.lambda_role.arn
  filename      = "../lambda/processor.zip"
  timeout       = 10
}

resource "aws_lambda_function" "report_lambda" {
  function_name = "daily-report-generator"
  runtime       = "python3.10"
  handler       = "report_generator.lambda_handler"
  role          = aws_iam_role.lambda_role.arn
  filename      = "../lambda/report.zip"
  timeout       = 10
}

resource "aws_lambda_permission" "allow_s3_invoke" {
  statement_id  = "AllowS3Invoke"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.processor_lambda.function_name
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.input_bucket.arn
}
