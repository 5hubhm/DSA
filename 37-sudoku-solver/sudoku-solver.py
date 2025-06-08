from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        self.rows = [0] * 9
        self.cols = [0] * 9
        self.boxes = [0] * 9
        self.empty = []

        for r in range(9):
            for c in range(9):
                if board[r][c] == '.':
                    self.empty.append((r, c))
                else:
                    d = int(board[r][c])
                    mask = 1 << d
                    self.rows[r] |= mask
                    self.cols[c] |= mask
                    self.boxes[(r // 3) * 3 + c // 3] |= mask

        self.backtrack(0, board)

    def backtrack(self, idx: int, board: List[List[str]]) -> bool:
        if idx == len(self.empty):
            return True

        r, c = self.empty[idx]
        box = (r // 3) * 3 + c // 3

        for d in range(1, 10):
            mask = 1 << d
            if not (self.rows[r] & mask or self.cols[c] & mask or self.boxes[box] & mask):
                # Place digit
                board[r][c] = str(d)
                self.rows[r] |= mask
                self.cols[c] |= mask
                self.boxes[box] |= mask

                if self.backtrack(idx + 1, board):
                    return True

                # Backtrack
                board[r][c] = '.'
                self.rows[r] ^= mask
                self.cols[c] ^= mask
                self.boxes[box] ^= mask

        return False
