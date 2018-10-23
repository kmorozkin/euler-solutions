import math
import random


# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/
def gen_primes():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


PLAIN_PRIMES = {3, 5, 7, 11, 13}


def is_probable_prime(n):
    """
    Miller-Rabin prime test
    """

    if not n & 1:
        return False
    if n == 1 or n in PLAIN_PRIMES:
        return True
    for plain_prime in PLAIN_PRIMES:
        if n % plain_prime == 0:
            return False

    def check(a, s, d, n):
        x = pow(a, d, n)
        if x == 1:
            return True
        for i in range(1, s):
            if x == n - 1:
                return True
            x = pow(x, 2, n)
        return x == n - 1

    d = n - 1
    s = 0
    while d % 2 == 0:
        d >>= 1
        s += 1
    iter_count = max(5, int(math.log2(n)))
    for iteration in range(iter_count):
        a = random.randrange(1, n)
        if not check(a, s, d, n):
            return False
    return True
