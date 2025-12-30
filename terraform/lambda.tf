resource "aws_lambda_function" "processor_lambda" {
  function_name = "event-processor"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.10"
  handler       = "processor.lambda_handler"
  filename      = "../lambda/processor.zip"
}

resource "aws_lambda_function" "report_lambda" {
  function_name = "daily-report-generator"
  role          = aws_iam_role.lambda_role.arn
  runtime       = "python3.10"
  handler       = "report_generator.lambda_handler"
  filename      = "../lambda/report.zip"
}
