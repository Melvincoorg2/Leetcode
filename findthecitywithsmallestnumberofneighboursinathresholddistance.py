class Solution:
 def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:

    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    # floyd-warshall
    for mid in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][mid] + dist[mid][j] < dist[i][j]:
                    dist[i][j] = dist[i][mid] + dist[mid][j]

    result = -1
    min_count = INF

    for i in range(n):
        count = sum(1 for j in range(n) if i != j and dist[i][j] <= distanceThreshold)
        if count <= min_count:   # <= to prefer higher city index
            min_count = count
            result = i

    return result