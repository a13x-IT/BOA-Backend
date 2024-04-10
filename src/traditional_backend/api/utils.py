from functools import lru_cache

@lru_cache(maxsize=None)
def average(lst : list[int]) -> int:
  return int(sum(lst) / len(lst)) 