class InputOutOfRangeError(ValueError):
    pass


class InputTypeError(TypeError):
    pass

class MissingInputError(ValueError):
    pass

class ResultOutOfRangeError(ValueError):
    pass

class UnsupportedOperatorError(ValueError):
    pass



def validate_input(value):
    if value is None:
        raise MissingInputError("Input value is missing.")
    if not isinstance(value, int):
        raise InputTypeError("Input must be an integer.")
    if value < 1 or value > 3999:
        raise InputOutOfRangeError("Input must be between 1 and 3999.")
    return value

def validate_result(value):
    if value < 1 or value > 3999:
        raise ResultOutOfRangeError("Result must be between 1 and 3999.")
    return value

def validate_operator(operator):
    supported_operators = ['add', 'subtract']
    if operator not in supported_operators:
        raise UnsupportedOperatorError(f"Operator '{operator}' is not supported.")
    return operator
