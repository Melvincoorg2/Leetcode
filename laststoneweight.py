import heapq

class Solution:
    def lastStoneWeight(self, stones):

        # Convert to max heap using negative values
        max_heap = [-stone for stone in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:

            y = -heapq.heappop(max_heap)  # largest
            x = -heapq.heappop(max_heap)  # second largest

            if y != x:
                heapq.heappush(max_heap, -(y - x))

        return -max_heap[0] if max_heap else 0