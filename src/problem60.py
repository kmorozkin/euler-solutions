'''
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the
result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes,
792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
from src.utils.decorators import Memoize
from src.utils.primes import gen_primes, is_probable_prime
from itertools import permutations


@Memoize
def is_prime_pair(item1, item2):
    juxtaposed = ('%d%d' % permutation_tuple for permutation_tuple in permutations((item1, item2), 2))
    return all(map(is_probable_prime, map(int, juxtaposed)))


class Collector:
    def __init__(self):
        self.max_pair_num = 0
        self.cache = []

    def add(self, *items):
        def all_match(coll1, coll2):
            for other_item in coll1:
                for cache_item in coll2:
                    if not is_prime_pair(cache_item, other_item):
                        return False
            return True

        def update():
            items_list = list(items)
            for i, item in enumerate(items_list):
                rest = [v for j, v in enumerate(items_list) if j != i]
                for cache_set in self.cache:
                    if item in cache_set and all_match(rest, cache_set):
                        cache_set.update(rest)
                        self.max_pair_num = max(len(cache_set), self.max_pair_num)
                        return True
            return False
        if not update():
            self.cache.append(set(items))

    def pairs(self, size):
        return [v for v in self.cache if len(v) == size]


limit = 5
collector = Collector()
iterator = gen_primes()
generated = [next(iterator)]
for prime_x in iterator:
    for prime_y in generated:
        if is_prime_pair(prime_y, prime_x):
            collector.add(prime_y, prime_x)
    generated.append(prime_x)
    if collector.max_pair_num >= limit:
        current_pairs = collector.pairs(limit)
        for group in current_pairs:
            print(group)
            print(sum(group))
        exit()

