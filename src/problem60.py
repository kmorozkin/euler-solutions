'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from src.utils.primes import gen_primes, is_probable_prime
from itertools import permutations


def is_prime_pair(item1, item2):
    juxtaposed = ('%d%d' % permutation_tuple for permutation_tuple in permutations((item1, item2), 2))
    return all(map(is_probable_prime, map(int, juxtaposed)))


class Collector:
    def __init__(self):
        self.cache_dictionary = dict()
        self.max_pair_num = 0

    def add_pair(self, item1, item2):
        for pair in ((item1, item2), (item2, item1)):
            cache = self.cache_dictionary.setdefault(pair[0], {pair[0]})
            if all(is_prime_pair(x, pair[1]) for x in cache):
                cache.add(pair[1])
                self.max_pair_num = max(len(cache), self.max_pair_num)

    def pairs(self, size):
        return [v for v in self.cache_dictionary.values() if len(v) == size]


limit = 5
collector = Collector()
iterator = gen_primes()
generated = [next(iterator)]
for prime_x in iterator:
    for prime_y in generated:
        if is_prime_pair(prime_y, prime_x):
            collector.add_pair(prime_y, prime_x)
    generated.append(prime_x)
    if collector.max_pair_num >= limit:
        current_pairs = collector.pairs(limit)
        for group in current_pairs:
            print(group)
            print(sum(group))
        exit()


# primes_list = list(islice(gen_primes(), 0, 700))
# for i in range(len(primes_list)):
#     for j in range(i, len(primes_list)):
#         prime_x = primes_list[i]
#         prime_y = primes_list[j]
#         if is_prime_pair(prime_x, prime_y):
#             collector.add_pair(prime_x, prime_y)
# print(collector.pairs(5))

