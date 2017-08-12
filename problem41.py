'''

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
 For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?

'''
from utils.primes import is_probable_prime
from utils.collections import permutations
from utils.digits import digits2num

max = 0
for permutation in permutations(range(1, 8)):
    number = digits2num(permutation)
    if is_probable_prime(number) and max < number:
        max = number

print(max)