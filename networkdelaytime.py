import heapq
from collections import defaultdict

class Solution:
 def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

    adj = defaultdict(list)
    for u, v, w in times:
        adj[u].append((v, w))

    dist = {i: float('inf') for i in range(1, n + 1)}
    dist[k] = 0
    heap = [(0, k)]  # (cost, node)

    while heap:
        cost, node = heapq.heappop(heap)
        if cost > dist[node]:
            continue
        for neighbor, weight in adj[node]:
            new_cost = cost + weight
            if new_cost < dist[neighbor]:
                dist[neighbor] = new_cost
                heapq.heappush(heap, (new_cost, neighbor))

    max_dist = max(dist.values())
    return max_dist if max_dist < float('inf') else -1