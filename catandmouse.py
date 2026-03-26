class Solution:
 def catMouseGame(self, graph: List[List[int]]) -> int:

    n = len(graph)

    @lru_cache(maxsize=None)
    def solve(mouse, cat, turn, moves):
        # draw if too many moves
        if moves >= 2 * n:
            return 0
        # mouse reached hole
        if mouse == 0:
            return 1
        # cat caught mouse
        if mouse == cat:
            return 2

        if turn == 0:  # mouse's turn, wants to return 1
            best = 2   # worst case for mouse
            for nxt in graph[mouse]:
                res = solve(nxt, cat, 1, moves + 1)
                if res == 1:
                    return 1
                if res == 0:
                    best = 0
            return best
        else:          # cat's turn, wants to return 2
            best = 1   # worst case for cat
            for nxt in graph[cat]:
                if nxt == 0:   # cat can't go to hole
                    continue
                res = solve(mouse, nxt, 0, moves + 1)
                if res == 2:
                    return 2
                if res == 0:
                    best = 0
            return best

    return solve(1, 2, 0, 0)