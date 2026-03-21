class Solution:
 def minCostConnectPoints(self, points: List[List[int]]) -> int:
    n = len(points)
    visited = [False] * n
    heap = [(0, 0)]  # (cost, node)
    total = 0
    count = 0

    while count < n:
        cost, i = heapq.heappop(heap)
        if visited[i]:
            continue
        visited[i] = True
        total += cost
        count += 1

        for j in range(n):
            if not visited[j]:
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                heapq.heappush(heap, (dist, j))

    return total
