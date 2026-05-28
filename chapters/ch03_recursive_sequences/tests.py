import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..'))

from chapters.ch03_recursive_sequences.exercises import (
    calc_first_n_terms_seq1, calc_nth_term_seq1,
    calc_first_n_terms_seq2, calc_nth_term_seq2,
    calc_first_n_terms_seq3, calc_nth_term_seq3,
    calc_first_n_terms_seq4, calc_nth_term_seq4,
)
from utils.test_runner import run_tests


# ── sequence 1: 5, *3-4 ───────────────────────────────────────────────────────
# 5, 11, 29, 83, 245
seq1_first_n_tests = [
    {'function': calc_first_n_terms_seq1, 'input': 1, 'output': [5]},
    {'function': calc_first_n_terms_seq1, 'input': 3, 'output': [5, 11, 29]},
    {'function': calc_first_n_terms_seq1, 'input': 5, 'output': [5, 11, 29, 83, 245]},
]
seq1_nth_tests = [
    {'function': calc_nth_term_seq1, 'input': 1, 'output': 5},
    {'function': calc_nth_term_seq1, 'input': 2, 'output': 11},
    {'function': calc_nth_term_seq1, 'input': 5, 'output': 245},
]

# ── sequence 2: 25, collatz ───────────────────────────────────────────────────
# 25, 76, 38, 19, 58
seq2_first_n_tests = [
    {'function': calc_first_n_terms_seq2, 'input': 1, 'output': [25]},
    {'function': calc_first_n_terms_seq2, 'input': 3, 'output': [25, 76, 38]},
    {'function': calc_first_n_terms_seq2, 'input': 5, 'output': [25, 76, 38, 19, 58]},
]
seq2_nth_tests = [
    {'function': calc_nth_term_seq2, 'input': 1, 'output': 25},
    {'function': calc_nth_term_seq2, 'input': 2, 'output': 76},
    {'function': calc_nth_term_seq2, 'input': 4, 'output': 19},
]

# ── sequence 3: fibonacci ─────────────────────────────────────────────────────
# 0, 1, 1, 2, 3, 5, 8, 13
seq3_first_n_tests = [
    {'function': calc_first_n_terms_seq3, 'input': 1, 'output': [0]},
    {'function': calc_first_n_terms_seq3, 'input': 2, 'output': [0, 1]},
    {'function': calc_first_n_terms_seq3, 'input': 6, 'output': [0, 1, 1, 2, 3, 5]},
]
seq3_nth_tests = [
    {'function': calc_nth_term_seq3, 'input': 1, 'output': 0},
    {'function': calc_nth_term_seq3, 'input': 2, 'output': 1},
    {'function': calc_nth_term_seq3, 'input': 6, 'output': 5},
    {'function': calc_nth_term_seq3, 'input': 8, 'output': 13},
]

# ── sequence 4: 2, -3, add product of previous two ───────────────────────────
# 2, -3, -3+2*(-3) = -9, -9+(-3)*(-9) = 18, 18+(-9)*18 = -144
seq4_first_n_tests = [
    {'function': calc_first_n_terms_seq4, 'input': 1, 'output': [2]},
    {'function': calc_first_n_terms_seq4, 'input': 2, 'output': [2, -3]},
    {'function': calc_first_n_terms_seq4, 'input': 5, 'output': [2, -3, -9, 18, -144]},
]
seq4_nth_tests = [
    {'function': calc_nth_term_seq4, 'input': 1, 'output': 2},
    {'function': calc_nth_term_seq4, 'input': 2, 'output': -3},
    {'function': calc_nth_term_seq4, 'input': 3, 'output': -9},
    {'function': calc_nth_term_seq4, 'input': 5, 'output': -144},
]


if __name__ == '__main__':
    print("=== seq1: first n terms ===")
    run_tests(seq1_first_n_tests)
    print("\n=== seq1: nth term ===")
    run_tests(seq1_nth_tests)

    print("\n=== seq2: first n terms ===")
    run_tests(seq2_first_n_tests)
    print("\n=== seq2: nth term ===")
    run_tests(seq2_nth_tests)

    print("\n=== seq3: first n terms ===")
    run_tests(seq3_first_n_tests)
    print("\n=== seq3: nth term ===")
    run_tests(seq3_nth_tests)

    print("\n=== seq4: first n terms ===")
    run_tests(seq4_first_n_tests)
    print("\n=== seq4: nth term ===")
    run_tests(seq4_nth_tests)
