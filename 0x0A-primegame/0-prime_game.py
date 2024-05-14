#!/usr/bin/python3
""" prime game
"""


def generate_primes(limit):
    """Generates primes up to a given limit using the
    Sieve of Eratosthenes algorithm."""
    primes = [True] * (limit + 1)
    primes[0], primes[1] = False, False
    for i in range(2, int(limit ** 0.5) + 1):
        if primes[i]:
            for j in range(i * i, limit + 1, i):
                primes[j] = False
    return primes


def count_primes(primes, n):
    """Counts the number of primes up to 'n'."""
    return sum(1 for prime in primes[:n] if prime)


def isWinner(x, nums):
    """Determines the winner of a prime game session with 'x' rounds."""
    if x < 1 or not nums:
        return None

    marias_wins, bens_wins = 0, 0
    max_num = max(nums)
    primes = generate_primes(max_num)

    for n in nums:
        primes_count = count_primes(primes, n)
        bens_wins += primes_count % 2 == 0
        marias_wins += primes_count % 2 == 1

    if marias_wins == bens_wins:
        return None
    return 'Maria' if marias_wins > bens_wins else 'Ben'
