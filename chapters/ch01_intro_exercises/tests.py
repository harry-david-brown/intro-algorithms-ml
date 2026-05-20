import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from chapters.ch01_intro_exercises.exercises import (
    check_if_symmetric,
    convert_to_numbers,
    convert_to_letters,
    get_intersection,
    get_union,
    count_characters,
    is_prime,
)
from utils.test_runner import run_tests


# ── check_if_symmetric ────────────────────────────────────────────────────────
symmetric_tests = [
    {'function': check_if_symmetric, 'input': 'racecar',       'output': True},
    {'function': check_if_symmetric, 'input': 'batman',        'output': False},
    {'function': check_if_symmetric, 'input': '',              'output': True},   # edge: empty
    {'function': check_if_symmetric, 'input': 'a',             'output': True},   # edge: single char
    {'function': check_if_symmetric, 'input': 'Racecar',       'output': True},   # case-insensitive
    {'function': check_if_symmetric, 'input': '!ab123 4 321ba!', 'output': True}, # from book
]

# ── convert_to_numbers ────────────────────────────────────────────────────────
to_numbers_tests = [
    {'function': convert_to_numbers, 'input': 'a cat',  'output': [1, 0, 3, 1, 20]},
    {'function': convert_to_numbers, 'input': '',       'output': []},
    {'function': convert_to_numbers, 'input': ' ',      'output': [0]},
    {'function': convert_to_numbers, 'input': 'z',      'output': [26]},
]

# ── convert_to_letters ────────────────────────────────────────────────────────
to_letters_tests = [
    {'function': convert_to_letters, 'input': [1, 0, 3, 1, 20], 'output': 'a cat'},
    {'function': convert_to_letters, 'input': [],               'output': ''},
    {'function': convert_to_letters, 'input': [0],              'output': ' '},
    {'function': convert_to_letters, 'input': [26],             'output': 'z'},
]

# ── get_intersection ──────────────────────────────────────────────────────────
# Note: order in output doesn't matter — adjust if your impl differs
intersection_tests = [
    {'function': get_intersection, 'input': ([1,2,3], [2,3,4]),    'output': [2, 3]},
    {'function': get_intersection, 'input': ([1,2,3], [4,5,6]),    'output': []},
    {'function': get_intersection, 'input': ([1,1,2], [1,2,2]),    'output': [1, 2]},  # duplicates stripped
    {'function': get_intersection, 'input': ([], [1,2]),           'output': []},
]

# ── get_union ─────────────────────────────────────────────────────────────────
union_tests = [
    {'function': get_union, 'input': ([1,2,3], [2,3,4]),    'output': [1, 2, 3, 4]},
    {'function': get_union, 'input': ([1,2,3], [4,5,6]),    'output': [1, 2, 3, 4, 5, 6]},
    {'function': get_union, 'input': ([], []),              'output': []},
]

# ── count_characters ─────────────────────────────────────────────────────────
count_tests = [
    {'function': count_characters, 'input': 'A cat!!!', 'output': {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}},
    {'function': count_characters, 'input': '',         'output': {}},
    {'function': count_characters, 'input': 'aA',       'output': {'a': 2}},
]

# ── is_prime ──────────────────────────────────────────────────────────────────
prime_tests = [
    {'function': is_prime, 'input': 2,   'output': True},
    {'function': is_prime, 'input': 3,   'output': True},
    {'function': is_prime, 'input': 4,   'output': False},
    {'function': is_prime, 'input': 17,  'output': True},
    {'function': is_prime, 'input': 100, 'output': False},
    {'function': is_prime, 'input': 97,  'output': True},
]


if __name__ == '__main__':
    print("=== check_if_symmetric ===")
    run_tests(symmetric_tests)

    print("\n=== convert_to_numbers ===")
    run_tests(to_numbers_tests)

    print("\n=== convert_to_letters ===")
    run_tests(to_letters_tests)

    print("\n=== get_intersection ===")
    run_tests(intersection_tests)

    print("\n=== get_union ===")
    run_tests(union_tests)

    print("\n=== count_characters ===")
    run_tests(count_tests)

    print("\n=== is_prime ===")
    run_tests(prime_tests)
