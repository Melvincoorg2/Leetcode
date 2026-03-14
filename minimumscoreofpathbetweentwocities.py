class Solution:
 def minScore(self, n: int, roads: List[List[int]]) -> int:
    adj = [[] for _ in range(n + 1)]
    for a, b, dist in roads:
        adj[a].append((b, dist))
        adj[b].append((a, dist))

    visited = [False] * (n + 1)
    result = float('inf')

    # BFS from node 1, find min edge in its component
    queue = [1]
    visited[1] = True

    while queue:
        next_queue = []
        for node in queue:
            for neighbor, dist in adj[node]:
                result = min(result, dist)
                if not visited[neighbor]:
                    visited[neighbor] = True
                    next_queue.append(neighbor)
        queue = next_queue

    return result