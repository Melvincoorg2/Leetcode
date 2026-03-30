from sortedcontainers import SortedList

class RangeModule:

    def __init__(self):
        self.ranges = SortedList(key=lambda x: x[0])

    def addRange(self, left: int, right: int) -> None:
        # find all overlapping or adjacent intervals
        new_left, new_right = left, right
        to_remove = []

        idx = self.ranges.bisect_left((left,))
        # check one before in case it overlaps
        if idx > 0:
            idx -= 1

        for i in range(idx, len(self.ranges)):
            s, e = self.ranges[i]
            if s > right:
                break
            if e >= left and s <= right:
                new_left = min(new_left, s)
                new_right = max(new_right, e)
                to_remove.append((s, e))

        for r in to_remove:
            self.ranges.remove(r)
        self.ranges.add((new_left, new_right))

    def queryRange(self, left: int, right: int) -> bool:
        idx = self.ranges.bisect_right((left, float('inf'))) - 1
        if idx < 0:
            return False
        s, e = self.ranges[idx]
        return s <= left and e >= right

    def removeRange(self, left: int, right: int) -> None:
        to_remove = []
        to_add = []

        idx = self.ranges.bisect_left((left,))
        if idx > 0:
            idx -= 1

        for i in range(idx, len(self.ranges)):
            s, e = self.ranges[i]
            if s >= right:
                break
            if e > left and s < right:
                to_remove.append((s, e))
                if s < left:
                    to_add.append((s, left))
                if e > right:
                    to_add.append((right, e))

        for r in to_remove:
            self.ranges.remove(r)
        for r in to_add:
            self.ranges.add(r)
