class Solution:
 def solveSudoku(self, board: List[List[str]]) -> None:

    rows  = [set() for _ in range(9)]
    cols  = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    empty = []

    # build initial state
    for i in range(9):
        for j in range(9):
            val = board[i][j]
            if val == '.':
                empty.append((i, j))
            else:
                box = (i // 3) * 3 + (j // 3)
                rows[i].add(val)
                cols[j].add(val)
                boxes[box].add(val)

    def backtrack(idx):
        if idx == len(empty):
            return True
        i, j = empty[idx]
        box = (i // 3) * 3 + (j // 3)

        for d in '123456789':
            if d not in rows[i] and d not in cols[j] and d not in boxes[box]:
                board[i][j] = d
                rows[i].add(d)
                cols[j].add(d)
                boxes[box].add(d)

                if backtrack(idx + 1):
                    return True

                board[i][j] = '.'
                rows[i].discard(d)
                cols[j].discard(d)
                boxes[box].discard(d)

        return False

    backtrack(0)