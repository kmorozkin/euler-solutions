'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

'''
from math import sqrt

def factors(num):
    results = set()
    # sieve until the number is odd
    while int(num) & 1 == 0:
        num /= 2
        results.add(2)
    # loop through evens; even non-primes are filtered by their lesser prime factors
    for factor in range(3, int(sqrt(num)) + 1, 2):
        while num % factor == 0:
            results.add(factor)
            num /= factor
    if num > 2:
        results.add(num)
    return results

def consecutive(num, count=4):
    length = len(factors(num))
    if length != count:
        return False
    for other in range(num + 1, num + count):
        if len(factors(other)) != length:
            return False
    return True

x = 2*3*5*7
while not consecutive(x, 4):
    x += 1
print(x)