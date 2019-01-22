from collections.abc import Iterator

class CachedIterator(Iterator):

    def __init__(self, iterator):
        self.iterator = iterator
        self.cache = []
        self.cached = False

    def __iter__(self):
        if not self.cached:
            return self
        else:
            return iter(self.cache)

    def __next__(self):
        try:
            current = next(self.iterator)
            self.cache.append(current)

            return current
        except StopIteration as e:
            self.cached = True

            raise e


def cache(iterator):
    return CachedIterator(iterator)


def cached(func):
    @wraps(func)
    def cached_func(*args, **kwargs):
        return cache(func(*args, **kwargs))

    return cached_func
