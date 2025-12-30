resource "aws_lambda_function" "processor_lambda" {
  function_name = "event-processor"
  runtime       = "python3.10"
  handler       = "processor.lambda_handler"
  role          = aws_iam_role.lambda_role.arn
  filename      = "../lambda/processor.zip"
  timeout       = 3
}

resource "aws_lambda_function" "report_lambda" {
  function_name = "daily-report-generator"
  runtime       = "python3.10"
  handler       = "report_generator.lambda_handler"
  role          = aws_iam_role.lambda_role.arn
  filename      = "../lambda/report.zip"
  timeout       = 3
}
