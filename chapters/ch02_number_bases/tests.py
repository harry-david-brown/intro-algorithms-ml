import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from chapters.ch02_number_bases.exercises import (
    binary_to_decimal,
    hexadecimal_to_decimal,
    decimal_to_binary,
    decimal_to_hexadecimal,
    binary_to_hexadecimal,
    hexadecimal_to_binary,
)
from utils.test_runner import run_tests


# ── binary_to_decimal ─────────────────────────────────────────────────────────
binary_to_decimal_tests = [
    {'function': binary_to_decimal, 'input': '11010',  'output': '26'},
    {'function': binary_to_decimal, 'input': '0',      'output': '0'},
    {'function': binary_to_decimal, 'input': '1',      'output': '1'},
    {'function': binary_to_decimal, 'input': '1111',   'output': '15'},
    {'function': binary_to_decimal, 'input': '100000', 'output': '32'},
]

# ── hexadecimal_to_decimal ────────────────────────────────────────────────────
hexadecimal_to_decimal_tests = [
    {'function': hexadecimal_to_decimal, 'input': '3B07F', 'output': '241791'},
    {'function': hexadecimal_to_decimal, 'input': '0',     'output': '0'},
    {'function': hexadecimal_to_decimal, 'input': 'F',     'output': '15'},
    {'function': hexadecimal_to_decimal, 'input': '10',    'output': '16'},
    {'function': hexadecimal_to_decimal, 'input': 'FF',    'output': '255'},
]

# ── decimal_to_binary ─────────────────────────────────────────────────────────
decimal_to_binary_tests = [
    {'function': decimal_to_binary, 'input': '26', 'output': '11010'},
    {'function': decimal_to_binary, 'input': '0',  'output': '0'},
    {'function': decimal_to_binary, 'input': '1',  'output': '1'},
    {'function': decimal_to_binary, 'input': '15', 'output': '1111'},
    {'function': decimal_to_binary, 'input': '32', 'output': '100000'},
]

# ── decimal_to_hexadecimal ────────────────────────────────────────────────────
decimal_to_hexadecimal_tests = [
    {'function': decimal_to_hexadecimal, 'input': '241791', 'output': '3B07F'},
    {'function': decimal_to_hexadecimal, 'input': '0',      'output': '0'},
    {'function': decimal_to_hexadecimal, 'input': '15',     'output': 'F'},
    {'function': decimal_to_hexadecimal, 'input': '16',     'output': '10'},
    {'function': decimal_to_hexadecimal, 'input': '255',    'output': 'FF'},
]

# ── binary_to_hexadecimal ─────────────────────────────────────────────────────
binary_to_hexadecimal_tests = [
    {'function': binary_to_hexadecimal, 'input': '11010',    'output': '1A'},
    {'function': binary_to_hexadecimal, 'input': '0',        'output': '0'},
    {'function': binary_to_hexadecimal, 'input': '1111',     'output': 'F'},
    {'function': binary_to_hexadecimal, 'input': '11111111', 'output': 'FF'},
]

# ── hexadecimal_to_binary ─────────────────────────────────────────────────────
hexadecimal_to_binary_tests = [
    {'function': hexadecimal_to_binary, 'input': '1A', 'output': '11010'},
    {'function': hexadecimal_to_binary, 'input': '0',  'output': '0'},
    {'function': hexadecimal_to_binary, 'input': 'F',  'output': '1111'},
    {'function': hexadecimal_to_binary, 'input': 'FF', 'output': '11111111'},
]


if __name__ == '__main__':
    print("=== binary_to_decimal ===")
    run_tests(binary_to_decimal_tests)

    print("\n=== hexadecimal_to_decimal ===")
    run_tests(hexadecimal_to_decimal_tests)

    print("\n=== decimal_to_binary ===")
    run_tests(decimal_to_binary_tests)

    print("\n=== decimal_to_hexadecimal ===")
    run_tests(decimal_to_hexadecimal_tests)

    print("\n=== binary_to_hexadecimal ===")
    run_tests(binary_to_hexadecimal_tests)

    print("\n=== hexadecimal_to_binary ===")
    run_tests(hexadecimal_to_binary_tests)
