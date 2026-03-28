class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        new = [value, value]
        merged = []
        inserted = False

        for s, e in self.intervals:
            if e + 1 < new[0]:          # current interval ends before new starts
                merged.append([s, e])
            elif s - 1 > new[1]:        # current interval starts after new ends
                if not inserted:
                    merged.append(new)
                    inserted = True
                merged.append([s, e])
            else:                        # overlap or adjacent — merge
                new[0] = min(new[0], s)
                new[1] = max(new[1], e)

        if not inserted:
            merged.append(new)

        self.intervals = merged

    def getIntervals(self) -> list[list[int]]:
        return self.intervals