from collections import deque
class Solution:
 def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        

    # build adjacency: adj[node] = list of (neighbor, color)
    RED, BLUE = 0, 1
    adj = [[] for _ in range(n)]

    for a, b in redEdges:
        adj[a].append((b, RED))
    for a, b in blueEdges:
        adj[a].append((b, BLUE))

    answer = [-1] * n
    answer[0] = 0

    # state: (node, last_color_used)
    # start with both colors possible from node 0
    visited = set()
    queue = deque()
    queue.append((0, RED, 0))   # (node, last_color, dist)
    queue.append((0, BLUE, 0))
    visited.add((0, RED))
    visited.add((0, BLUE))

    while queue:
        node, last_color, dist = queue.popleft()

        for neighbor, color in adj[node]:
            if color == last_color:         # must alternate
                continue
            if (neighbor, color) in visited:
                continue
            visited.add((neighbor, color))
            if answer[neighbor] == -1:
                answer[neighbor] = dist + 1
            queue.append((neighbor, color, dist + 1))

    return answer