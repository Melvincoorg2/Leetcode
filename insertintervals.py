class Solution:
 def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

    result = []
    i = 0
    n = len(intervals)

    # add all intervals that end before newInterval starts
    while i < n and intervals[i][1] < newInterval[0]:
        result.append(intervals[i])
        i += 1

    # merge overlapping intervals
    while i < n and intervals[i][0] <= newInterval[1]:
        newInterval[0] = min(newInterval[0], intervals[i][0])
        newInterval[1] = max(newInterval[1], intervals[i][1])
        i += 1

    result.append(newInterval)

    # add remaining
    while i < n:
        result.append(intervals[i])
        i += 1

    return result