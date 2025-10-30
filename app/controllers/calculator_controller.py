from flask import Blueprint, request
from app.services import CalculatorService
from app.utils import validate_input, validate_operator, InputOutOfRangeError, InputTypeError, MissingInputError, UnsupportedOperatorError, ResultOutOfRangeError


bp = Blueprint('calculator', __name__, url_prefix='/api/calculator')
calculator_service = CalculatorService()

error_map = {
    InputOutOfRangeError: "INPUT_OUT_OF_RANGE",
    InputTypeError: "INVALID_TYPE",
    MissingInputError: "MISSING_INPUT",
    UnsupportedOperatorError: "UNSUPPORTED_OPERATOR",
    ResultOutOfRangeError: "RESULT_OUT_OF_RANGE",
}

# POST /api/calculator/convert
@bp.route('/convert', methods=['POST'])
def convert_single_value():
    data = request.json or {}
    value = data.get('value')

    try:
        validate_input(value)
    except tuple(error_map.keys()) as e:
        return {"error": str(e), "code": error_map[type(e)]}, 400
    result = calculator_service.convert_single_value(value)
    return result, 200

# POST /api/calculator/operation
@bp.route('/operation', methods=['POST'])
def perform_operation_and_convert():
    data = request.json or {}
    value1 = data.get('value1')
    value2 = data.get('value2')
    operator = data.get('operator')

    try:
        validate_input(value1)
        validate_input(value2)
        validate_operator(operator)
    except tuple(error_map.keys()) as e:
        return {"error": str(e), "code": error_map[type(e)]}, 400
    
    try:
     result = calculator_service.convert_values(value1, value2, operator)
    except (ResultOutOfRangeError) as e:
        return {"error": str(e), "code": error_map[type(e)]}, 422
    return result, 200

    