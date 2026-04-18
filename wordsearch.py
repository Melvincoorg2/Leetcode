class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        def dfs(i, j, k):
            # k = index in word

            # base case → all chars matched
            if k == len(word):
                return True

            # out of bounds or mismatch
            if i < 0 or j < 0 or i >= m or j >= n or board[i][j] != word[k]:
                return False

            # mark visited
            temp = board[i][j]
            board[i][j] = "#"

            # explore 4 directions
            found = (
                dfs(i+1, j, k+1) or
                dfs(i-1, j, k+1) or
                dfs(i, j+1, k+1) or
                dfs(i, j-1, k+1)
            )

            # backtrack
            board[i][j] = temp

            return found

        # try every cell as starting point
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True

        return False