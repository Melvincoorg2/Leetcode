import heapq
class Solution:
    def isPossible(self, target: List[int]) -> bool:

        if len(target) == 1:
            return target[0] == 1

        total = sum(target)

        # max heap (use negative values)
        max_heap = [-x for x in target]
        heapq.heapify(max_heap)

        while True:

            x = -heapq.heappop(max_heap)
            rest = total - x

            if x == 1 or rest == 1:
                return True

            if rest == 0 or x <= rest:
                return False

            x = x % rest

            if x == 0:
                return False

            total = rest + x
            heapq.heappush(max_heap, -x)