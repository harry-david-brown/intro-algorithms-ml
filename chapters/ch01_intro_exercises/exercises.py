# Chapter 0 - Some Short Introductory Coding Exercises
# Rules: no external libraries, no built-ins that bypass loops/conditionals in
# nontrivial ways. No Set or Counter. Primitives like len() and list.append() are fine.


def check_if_symmetric(s: str) -> bool:
    """Return True if string is a palindrome (case-insensitive), False otherwise."""
    s = s.upper()
    s2 = ''
    for i in range(len(s)-1, -1, -1):
        s2 += s[i]
    if(s == s2):
        return True
    else:
        return False


def convert_to_numbers(s: str) -> list[int]:
    """
    Return list of ints: space=0, a=1, b=2, ..., z=26.
    e.g. convert_to_numbers('a cat') -> [1, 0, 3, 1, 20]
    """
    
    letters = ' abcdefghijklmnopqrstuvwxyz'
    counter = 0
    dictionary = []
    
    for i in range(0, len(letters)):
        c = letters[i]
        pair = [c, counter]
        dictionary.append(pair)
        counter += 1

    final_array = []
    for letter in s:
        for hash in dictionary:
            if (letter == hash[0]):
                final_array.append(hash[1])
                break

    return final_array


def convert_to_letters(numbers: list[int]) -> str:
    """
    Inverse of convert_to_numbers.
    e.g. convert_to_letters([1, 0, 3, 1, 20]) -> 'a cat'
    """
    letters = ' abcdefghijklmnopqrstuvwxyz'
    counter = 0
    dictionary = []
    
    for i in range(0, len(letters)):
        c = letters[i]
        pair = [c, counter]
        dictionary.append(pair)
        counter += 1

    final_str = ''
    for index in numbers:
        for hash in dictionary:
            if (index == hash[1]):
                final_str += hash[0]
                break

    return final_str


def get_intersection(array1: list, array2: list) -> list:
    """Return elements present in both arrays, no duplicates."""
    inter = []
    for i in array1:
        if(i in array2):
            if(i not in inter):
                inter.append(i)

    return inter


def get_union(array1: list, array2: list) -> list:
    """Return elements present in either array, no duplicates."""
    union = []
    for i in array1:
        if(i not in union):
            union.append(i)
    for j in array2:
        if(j not in union):
            union.append(j)

    return union


def count_characters(s: str) -> dict[str, int]:
    """
    Count occurrences of each character (case-insensitive).
    e.g. count_characters('A cat!!!') -> {'a': 2, 'c': 1, 't': 1, ' ': 1, '!': 3}
    """
    str = s.lower()
    characters = {}

    for i in str:
        characters[i] = 0
    for j in str:
        characters[j] += 1

    return characters


def is_prime(n: int) -> bool:
    """
    Return True if n > 1 is prime.
    Check divisibility by each integer in {2, 3, ..., floor(n/2)}.
    """
    if(n == 1):
        return False
    elif(n == 2):
        return True

    for i in range(2, n+1):
        if(i == n):
            return True

        elif(n % i == 0):
            return False


function = is_prime
print(function(7))
