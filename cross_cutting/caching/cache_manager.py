from functools import lru_cache

@lru_cache(maxsize=1024)
def cached(key: str):
    return key
