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
    hex_chars = '0123456789ABCDEF'

    length = len(string)
    remainder = length % 4
    if (remainder != 0):
        zeroes = 4 - remainder
        for i in range(zeroes):
            string = '0' + string


    text = ''
    while (string):
        if (len(string) == 0):
            break
        #take a slice
        quad = string[:4]
        string = string[4:]

        bit_values = {'0': 0, '1': 1}
        value = 0
        for bit in quad:
            value = value * 2 + bit_values[bit]
        text += hex_chars[value]

    return text


def hexadecimal_to_binary(string: str) -> str:
    """Hint: compose hexadecimal_to_decimal and decimal_to_binary."""
    binary = '01'
    hex_values = {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,
              'A':10,'B':11,'C':12,'D':13,'E':14,'F':15}

    text = ''

    if string == '0':
        return '0'

    while (string):
        slice = string[:1]
        string = string[1:]
        digit = hex_values[slice]
        chunk = ''
        while (digit > 0):
            chunk = str(digit % 2) + chunk
            digit = digit // 2
        text += chunk
    return text

