from collections import deque
class Solution:
 def catMouseGame(self, graph: List[List[int]]) -> int:
    n = len(graph)
    DRAW, MOUSE, CAT = 0, 1, 2

    # color[mouse][cat][turn] = result
    color = [[[0]*2 for _ in range(n)] for _ in range(n)]
    # degree[mouse][cat][turn] = remaining moves to explore
    degree = [[[0]*2 for _ in range(n)] for _ in range(n)]

    # precompute degrees
    for m in range(n):
        for c in range(n):
            degree[m][c][0] = len(graph[m])           # mouse's turn: mouse moves
            degree[m][c][1] = len(graph[c]) - (0 in graph[c])  # cat can't go to 0

    queue = deque()

    # seed known outcomes
    for i in range(n):
        for t in range(2):
            # mouse at hole → mouse wins (skip cat==hole which is invalid)
            if i != 0:
                color[0][i][t] = MOUSE
                queue.append((0, i, t, MOUSE))
            # cat catches mouse → cat wins (not at hole)
            if i != 0:
                color[i][i][t] = CAT
                queue.append((i, i, t, CAT))

    while queue:
        m, c, t, result = queue.popleft()

        # find all parents (states that lead to this state)
        if t == 1:  # current turn is cat, so parent turn is mouse (t=0), mouse moved to m
            for pm in graph[m]:  # mouse came from pm
                if color[pm][c][0] != DRAW:
                    continue
                if result == MOUSE:  # mouse wins → mouse would choose this
                    color[pm][c][0] = MOUSE
                    queue.append((pm, c, 0, MOUSE))
                else:  # cat wins → only mark if all mouse moves lead to cat win
                    degree[pm][c][0] -= 1
                    if degree[pm][c][0] == 0:
                        color[pm][c][0] = CAT
                        queue.append((pm, c, 0, CAT))

        else:  # current turn is mouse, so parent turn is cat (t=1), cat moved to c
            for pc in graph[c]:  # cat came from pc
                if pc == 0:
                    continue
                if color[m][pc][1] != DRAW:
                    continue
                if result == CAT:  # cat wins → cat would choose this
                    color[m][pc][1] = CAT
                    queue.append((m, pc, 1, CAT))
                else:  # mouse wins → only mark if all cat moves lead to mouse win
                    degree[m][pc][1] -= 1
                    if degree[m][pc][1] == 0:
                        color[m][pc][1] = MOUSE
                        queue.append((m, pc, 1, MOUSE))

    return color[1][2][0]