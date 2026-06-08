# Chapter 3 - Recursive Sequences


# Sequence 1: starting with 5, multiply previous term by 3 and subtract 4
def calc_first_n_terms_seq1(n: int) -> list:
    terms = [5]

    while(len(terms) < n):
        prev_term = terms[-1]
        next_term = (prev_term * 3) - 4
        terms.append(next_term)

    return terms


def calc_nth_term_seq1(n: int) -> int:
    if(n==1):
        return 5

    prev_term = calc_nth_term_seq1(n-1)
    return (prev_term * 3) - 4


# Sequence 2: starting with 25, if even take half, if odd multiply by 3 and add 1 (Collatz)
def calc_first_n_terms_seq2(n: int) -> list:
    terms = [25]

    if (n == 1):
        return terms

    for i in range(1, n):
        if(terms[i-1] % 2 == 0):
            terms.append(terms[i-1] // 2)
        else:
            terms.append((terms[i-1] * 3) + 1)

    return terms


def calc_nth_term_seq2(n: int) -> int:
    if (n==1):
        return 25

    prev_term = calc_nth_term_seq2(n-1)
    if(prev_term % 2 == 0):
        return prev_term//2
    else:
        return (prev_term*3) + 1
    return n


# Sequence 3: starting with 0, 1, add previous two terms (Fibonacci)
def calc_first_n_terms_seq3(n: int) -> list:
    terms = [0,1]

    if (n < 2):
        return [0]
    if (n == 2):
        return terms

    for i in range(1, n-1):
        terms.append(terms[i] + terms[i-1])

    return terms


def calc_nth_term_seq3(n: int) -> int:
    
    if (n < 2):
        return 0
    if (n == 2):
        return 1

    prev_term = calc_nth_term_seq3(n-1)
    return n + prev_term



print(calc_nth_term_seq3(3))
# 0, 1, 1, 2, 3, 5, 8

# Sequence 4: starting with 2, -3, add product of previous two terms
def calc_first_n_terms_seq4(n: int) -> list:
    pass

def calc_nth_term_seq4(n: int) -> int:
    pass
