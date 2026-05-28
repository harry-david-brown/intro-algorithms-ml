# Chapter 2 - Converting Between Binary, Decimal, and Hexadecimal
# All inputs and outputs are strings.


def binary_to_decimal(string: str) -> str:
    """e.g. binary_to_decimal('11010') -> '26'"""
    total = 0
    digit_position = len(string)-1

    for char in string:
        if (char == '1'):
            total += 2 ** digit_position
        digit_position -= 1
    
    text = str(total)
    return text


def hexadecimal_to_decimal(string: str) -> str:
    """e.g. hexadecimal_to_decimal('3B07F') -> '241791'"""
    total = 0
    digit_position = len(string)-1
    scalar_dict = {'0':0, '1':1,'2':2,'3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                   'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

    for char in string:
        if (char != '0'):
            total += (16 ** digit_position) * scalar_dict.get(char)
        digit_position -= 1

    text = str(total)

    return text


def decimal_to_binary(string: str) -> str:
    """e.g. decimal_to_binary('26') -> '11010'"""
    num = int(string)

    if num == 0:
        return '0'

    text = ''
    while num > 0:
        text = str(num % 2) + text
        num = num // 2

    return text


def decimal_to_hexadecimal(string: str) -> str:
    """e.g. decimal_to_hexadecimal('241791') -> '3B07F'"""
    num = int(string)
    hex_chars = '0123456789ABCDEF'

    if num == 0:
        return '0'

    text = ''
    while num > 0:
        remainder = num % 16
        text = hex_chars[remainder] + text
        num = num // 16

    return text


def binary_to_hexadecimal(string: str) -> str:
    """Hint: compose binary_to_decimal and decimal_to_hexadecimal."""
    pass


def hexadecimal_to_binary(string: str) -> str:
    """Hint: compose hexadecimal_to_decimal and decimal_to_binary."""
    pass
