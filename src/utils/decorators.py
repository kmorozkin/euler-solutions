class Memoize:
    def __init__(self, fn):
        self.fn = fn
        self.memo = {}

    def __call__(self, *args):
        cached = self.memo.get(args)
        if not cached:
            cached = self.fn(*args)
            self.memo[args] = cached
        return cached

