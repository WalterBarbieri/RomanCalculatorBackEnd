# Roman Calculator and Converter

## Supported Inputs
- Accepts only postive integers
- Range: 1 : 3999

## Supported Operations
- Addition
- Subtraction

## Error Handling
- Input out of Range => if (0 <= input > 3999):
{
  "error": "Input number out of range",
  "code": "OUT_OF_RANGE",
  "http_error": 400
}
- Result out of Range => if (0 <= result > 3999):
{
  "error": "Result out of range",
  "code": "RESULT_OUT_OF_RANGE",
  "http_error": 422
}
- Input not an integer => if (input != integer):
{
  "error": "Input must be an integer",
  "code": "INVALID_TYPE",
  "http_error": 400
}
