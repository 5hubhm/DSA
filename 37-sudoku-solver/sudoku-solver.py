class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty = []

        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    empty.append((i, j))
                else:
                    val = board[i][j]
                    rows[i].add(val)
                    cols[j].add(val)
                    boxes[(i // 3) * 3 + (j // 3)].add(val)

        def backtrack(idx):
            if idx == len(empty):
                return True

            r, c = empty[idx]
            b = (r // 3) * 3 + (c // 3)

            for d in map(str, range(1, 10)):
                if d not in rows[r] and d not in cols[c] and d not in boxes[b]:
                    board[r][c] = d
                    rows[r].add(d)
                    cols[c].add(d)
                    boxes[b].add(d)

                    if backtrack(idx + 1):
                        return True

                    board[r][c] = "."
                    rows[r].remove(d)
                    cols[c].remove(d)
                    boxes[b].remove(d)
            return False

        backtrack(0)
