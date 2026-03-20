class Solution:
 def leftmostBuildingQueries(self, heights: List[int], queries: List[List[int]]) -> List[int]:

    n = len(heights)
    ans = [-1] * len(queries)

    # bucket pending queries by their right index
    # each entry: (min_height_needed, query_index)
    pending = [[] for _ in range(n)]

    for i, (a, b) in enumerate(queries):
        a, b = min(a, b), max(a, b)
        if a == b:
            ans[i] = a
        elif heights[a] < heights[b]:
            ans[i] = b
        else:
            # need first j > b with heights[j] > heights[a]
            needed = heights[a]
            pending[b].append((needed, i))

    # min-heap: (min_height_needed, query_index)
    heap = []

    for j in range(n):
        # resolve any pending queries where heights[j] satisfies
        while heap and heap[0][0] < heights[j]:
            _, qi = heapq.heappop(heap)
            ans[qi] = j

        for entry in pending[j]:
            heapq.heappush(heap, entry)

    return ans