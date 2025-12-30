resource "aws_cloudwatch_event_rule" "daily_report" {
  name                = "daily-report-rule"
  schedule_expression = "rate(1 day)"
}

resource "aws_cloudwatch_event_target" "report_lambda_target" {
  rule = aws_cloudwatch_event_rule.daily_report.name
  arn  = aws_lambda_function.report_lambda.arn
}
