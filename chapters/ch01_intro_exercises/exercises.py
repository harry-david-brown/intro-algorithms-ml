# Chapter 1 - Some Short Introductory Coding Exercises
# Rules: no external libraries, no built-ins that bypass loops/conditionals in
# nontrivial ways. No Set or Counter. Primitives like len() and list.append() are fine.


def check_if_symmetric(string: str) -> bool:
    """Return True if string is a palindrome (case-insensitive), False otherwise."""
    pass


def convert_to_numbers(string: str) -> list[int]:
    """
    Return list of ints: space=0, a=1, b=2, ..., z=26.
    e.g. convert_to_numbers('a cat') -> [1, 0, 3, 1, 20]
    """
    pass


def convert_to_letters(numbers: list[int]) -> str:
    """
    Inverse of convert_to_numbers.
    e.g. convert_to_letters([1, 0, 3, 1, 20]) -> 'a cat'
    """
    pass


def get_intersection(array1: list, array2: list) -> list:
    """Return elements present in both arrays, no duplicates."""
    pass


def get_union(array1: list, array2: list) -> list:
    """Return elements present in either array, no duplicates."""
    pass


def count_characters(string: str) -> dict[str, int]:
    """
    Count occurrences of each character (case-insensitive).
    e.g. count_characters('A cat!!!') -> {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}
    """
    pass


def is_prime(n: int) -> bool:
    """
    Return True if n > 1 is prime.
    Check divisibility by each integer in {2, 3, ..., floor(n/2)}.
    """
    pass
