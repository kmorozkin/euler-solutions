'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

'''
from src.utils.primes import gen_primes, is_probable_prime
from math import sqrt


def failed(num):
    for base in range(1, int(sqrt(num / 2)) + 1):
        rest = num - 2 * base ** 2
        if is_probable_prime(rest):
            return False
    return True

primes = gen_primes()
last_prime = next(primes)
current = 8
while True:
    while last_prime < current:
        last_prime = next(primes)
    if current & 1 == 0 or last_prime == current:
        current += 1
        continue
    if failed(current):
        print(current)
        break
    current += 1