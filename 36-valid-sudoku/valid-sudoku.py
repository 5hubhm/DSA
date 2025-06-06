class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [[0] * 9 for _ in range(9)]
        cols = [[0] * 9 for _ in range(9)]
        boxes = [[0] * 9 for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c]) - 1  # convert '1'-'9' to 0–8
                    box_index = (r // 3) * 3 + (c // 3)

                    # If the digit is already seen in this row, column, or box → invalid
                    if rows[r][num] or cols[c][num] or boxes[box_index][num]:
                        return False

                    # Mark the digit as seen
                    rows[r][num] = 1
                    cols[c][num] = 1
                    boxes[box_index][num] = 1

        return True
