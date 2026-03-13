class Solution:
 def maximalPathQuality(self, values: List[int], edges: List[List[int]], maxTime: int) -> int:
    n = len(values)
    graph = [[] for _ in range(n)]
    
    for u, v, t in edges:
        graph[u].append((v, t))
        graph[v].append((u, t))
    
    best = [0]
    visited = [0] * n
    visited[0] = 1

    def dfs(node, time_left, quality):
        if node == 0:
            best[0] = max(best[0], quality)
        
        for nei, t in graph[node]:
            if time_left - t >= 0:
                is_new = visited[nei] == 0
                visited[nei] += 1
                dfs(nei, time_left - t, quality + (values[nei] if is_new else 0))
                visited[nei] -= 1

    dfs(0, maxTime, values[0])
    return best[0]