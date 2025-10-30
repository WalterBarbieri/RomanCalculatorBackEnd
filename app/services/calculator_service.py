from app.utils import validate_result
from app.utils import int_to_roman, old_int_to_roman


class CalculatorService:
    def add(self, a: int, b: int) -> int:
        result = a + b
        validate_result(result)
        return result

    def subtract(self, a: int, b: int) -> int:
        result = a - b
        validate_result(result)
        return result

    def convert_single_value(self, value: int) -> dict:

        roman_value: str = int_to_roman(value)
        return {"value": value, "roman": roman_value}

    def convert_values(self, a: int, b: int, operator: str) -> dict:
        if operator == "add":
            result = self.add(a, b)
        elif operator == "subtract":
            result = self.subtract(a, b)

        roman_result: str = int_to_roman(result)

        return {"value1": a, "value2": b, "operator": operator, "result": result, "roman_result": roman_result}
