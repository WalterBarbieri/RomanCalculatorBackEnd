# Roman Calculator and Converter

## Supported Inputs
- Accepts only postive integers
- Range: 1 : 3999

## Supported Operations
- "add" = Addition
- "subtract" = Subtraction

## API

POST http://127.0.0.1:5000/api/calculator/convert
```json
{
  "value": 5
}
```
- Response:
```json
{ 
  "roman": "V",
  "value": 5
}
```

POST http://127.0.0.1:5000/api/calculator/operation
```json
{
  "value1": int
  "value2": int
  "operator": str
}

- Response:
```json
{ 
  "operator": str
  "result": int
  "roman_result": str
  "value1": int
  "value2": int
}


## Error Handling
- Input out of Range => if (0 <= input > 3999):
```json
{
  "error": "Input must be between 1 and 3999",
  "code": "INPUT_OUT_OF_RANGE",
  "http_error": 400
}
- Result out of Range => if (0 <= result > 3999):
```json
{
  "error": "Result must be between 1 and 3999",
  "code": "RESULT_OUT_OF_RANGE",
  "http_error": 422
}
- Input not an integer => if (input != integer):
```json
{
  "error": "Input must be an integer",
  "code": "INVALID_TYPE",
  "http_error": 400

}
- Operator not supported => (operator != "add" || operator != "subtract"):
```json
{
  "error": "Operator {operator} not supported",
  "code": "UNSUPPORTED_OPERATOR",
  "http_error": 400

}

- Missing input => (input == null):
```json
{
  "error": "Input values is missing",
  "code": "MISSING_INPUT",
  "http_error": 400

}
