output "processor_lambda_name" {
  value = aws_lambda_function.processor_lambda.function_name
}

output "report_lambda_name" {
  value = aws_lambda_function.report_lambda.function_name
}
