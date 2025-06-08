class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]

        # Initialize sets based on the initial board state
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != '.':
                    rows[r].add(val)
                    cols[c].add(val)
                    box_index = (r // 3) * 3 + (c // 3)
                    boxes[box_index].add(val)

        def solve(row, col):
            if row == 9:
                return True
            if col == 9:
                return solve(row + 1, 0)
            if board[row][col] != '.':
                return solve(row, col + 1)

            box_index = (row // 3) * 3 + (col // 3)
            for val in map(str, range(1, 10)):
                if val not in rows[row] and val not in cols[col] and val not in boxes[box_index]:
                    board[row][col] = val
                    rows[row].add(val)
                    cols[col].add(val)
                    boxes[box_index].add(val)

                    if solve(row, col + 1):
                        return True

                    # backtrack
                    board[row][col] = '.'
                    rows[row].remove(val)
                    cols[col].remove(val)
                    boxes[box_index].remove(val)

            return False

        solve(0, 0)