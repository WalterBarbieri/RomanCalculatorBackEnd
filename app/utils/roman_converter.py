roman_numerals_map = (
    (1000, "M"),
    (900, "CM"),
    (500, "D"),
    (400, "CD"),
    (100, "C"),
    (90, "XC"),
    (50, "L"),
    (40, "XL"),
    (10, "X"),
    (9, "IX"),
    (5, "V"),
    (4, "IV"),
    (1, "I"),
)


def int_to_roman(num: int) -> str:
    result = ""
    for value, symbol in roman_numerals_map:
        while num >= value:
            result += symbol
            num -= value

    return result


def old_int_to_roman(num: int) -> str:
    result = ""

    if num >= 1000:
        thousands = num // 1000
        result += "M" * thousands
        num -= 1000 * thousands
    if num >= 900:
        result += "CM"
        num -= 900
    if num >= 500:
        result += "D"
        num -= 500
    if num >= 400:
        result += "CD"
        num -= 400
    if num >= 100:
        hundreds = num // 100
        result += "C" * hundreds
        num -= 100 * hundreds
    if num >= 90:
        result += "XC"
        num -= 90
    if num >= 50:
        result += "L"
        num -= 50
    if num >= 40:
        result += "XL"
        num -= 40
    if num >= 10:
        tens = num // 10
        result += "X" * tens
        num -= 10 * tens
    if num >= 9:
        result += "IX"
        num -= 9
    if num >= 5:
        result += "V"
        num -= 5
    if num >= 4:
        result += "IV"
        num -= 4
    if num >= 1:
        result += "I" * num
    return result
