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
    scalar_dict = {'1':1,'2':2,'3':3, '4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
                   'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

    for char in string:
        if (char != '0'):
            total += (16 ** digit_position) * scalar_dict.get(char)
        digit_position -= 1
    
    text = str(total)
    
    return text


def decimal_to_binary(string: str) -> str:
    """e.g. decimal_to_binary('26') -> '11010'"""
    pass


def decimal_to_hexadecimal(string: str) -> str:
    """e.g. decimal_to_hexadecimal('241791') -> '3B07F'"""
    pass


def binary_to_hexadecimal(string: str) -> str:
    """Hint: compose binary_to_decimal and decimal_to_hexadecimal."""
    pass


def hexadecimal_to_binary(string: str) -> str:
    """Hint: compose hexadecimal_to_decimal and decimal_to_binary."""
    pass
