class RangeFreqQuery:

    def __init__(self, arr: list[int]):
        self.positions = defaultdict(list)
        for i, val in enumerate(arr):
            self.positions[val].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        pos = self.positions[value]
        return bisect_right(pos, right) - bisect_left(pos, left)