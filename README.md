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

POST http://127.0.0.1:5000/api/calculator/compute
```json
{
  "value1": 187,
  "value2": 213,
  "operator": "add"
}
```
- Response:
```json
{ 
  "operator": "add",
  "result": 400,
  "roman_result": "CD",
  "value1": 187,
  "value2": 213
}
```

## Error Handling

- HTTP_ERROR: 400
  - Input out of Range => if input < 1 or input > 3999:
```json
{
  "error": "Input must be between 1 and 3999",
  "code": "INPUT_OUT_OF_RANGE"
}
```
- HTTP_ERROR: 400
  - Input not an integer => if (input != integer):
```json
{
  "error": "Input must be an integer",
  "code": "INVALID_TYPE"
}
```
- HTTP_ERROR: 400
  - Operator not supported => (operator != "add" || operator != "subtract"):
```json
{
  "error": "Operator {operator} not supported",
  "code": "UNSUPPORTED_OPERATOR"
}
```
- HTTP_ERROR: 400
  - Missing input => (input == null):
```json
{
  "error": "Input values is missing",
  "code": "MISSING_INPUT"
}
```
- HTTP_ERROR: 422
  - Result out of Range => if resul < 1 or result > 3999:
```json
{
  "error": "Result must be between 1 and 3999",
  "code": "RESULT_OUT_OF_RANGE",
  "http_error": 422
}
```
