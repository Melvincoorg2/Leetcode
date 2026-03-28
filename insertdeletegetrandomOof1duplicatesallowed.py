import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.vals = []                      # list of (val, index_in_set)
        self.idx = defaultdict(set)         # val -> set of indices in vals

    def insert(self, val: int) -> bool:
        absent = len(self.idx[val]) == 0
        self.idx[val].add(len(self.vals))
        self.vals.append(val)
        return absent

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False
        # pick any index of val, swap with last
        remove_idx = next(iter(self.idx[val]))
        last_val = self.vals[-1]

        self.vals[remove_idx] = last_val
        self.idx[last_val].add(remove_idx)
        self.idx[last_val].discard(len(self.vals) - 1)

        self.idx[val].discard(remove_idx)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)