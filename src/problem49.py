'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i)
each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?

'''
from src.utils.primes import gen_primes
from src.utils.digits import *
from itertools import permutations, takewhile

primes = gen_primes()
primes = takewhile(lambda x : x < 10000, primes)
primes = filter(lambda x: x > 1000, primes)
primes = set(primes)

def num_permutations(num):
    for x in permutations(num2digits(num)):
        yield digits2num(x)

for prime in primes:
    prime_perms = filter(lambda x: x in primes, num_permutations(prime))
    prime_perms = set(prime_perms)
    prime_perms.remove(prime)
    for perm in prime_perms:
        diff = perm - prime
        if perm + diff in prime_perms:
            print('FOUND! {}-{}-{}'.format(prime, perm, perm + diff))

