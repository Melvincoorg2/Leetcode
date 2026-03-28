import random
from collections import defaultdict

class RandomizedCollection:

    def __init__(self):
        self.vals = []
        self.idx = defaultdict(set)

    def insert(self, val: int) -> bool:
        absent = len(self.idx[val]) == 0
        self.idx[val].add(len(self.vals))
        self.vals.append(val)
        return absent

    def remove(self, val: int) -> bool:
        if not self.idx[val]:
            return False

        last_idx = len(self.vals) - 1
        last_val = self.vals[last_idx]

        # prefer removing an index that isn't last to simplify swap
        if last_idx in self.idx[val]:
            remove_idx = last_idx
        else:
            remove_idx = next(iter(self.idx[val]))

        if remove_idx != last_idx:
            self.vals[remove_idx] = last_val
            self.idx[last_val].add(remove_idx)
            self.idx[last_val].discard(last_idx)

        self.idx[val].discard(remove_idx)
        self.vals.pop()
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)