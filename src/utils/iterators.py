class Encache:
    def __init__(self, iterator):
        self.cache = []
        self.iterator = iterator

    def __iter__(self):
        return CachedIterator(self.cache, self.iterator)


class CachedIterator:
    def __init__(self, cache, iterator):
        self.cache = cache
        self.iterator = iterator
        self.x = 0

    def __iter__(self):
        return self

    def __next__(self):
        x = self.x
        self.x += 1
        if x < len(self.cache):
            return self.cache[x]
        else:
            val = next(self.iterator)
            self.cache.append(val)
            return val