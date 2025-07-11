class Solution:

    def isSafe(self, row, col, board, n):
        dupRow, dupCol = row, col
        while row>=0 and col>=0:
            if board[row][col] == 'Q':
                return False
            row-=1
            col-=1
        
        row, col = dupRow, dupCol
        while col>=0:
            if board[row][col] == 'Q':
                return False
            col-=1

        row, col = dupRow, dupCol
        while row<n and col>=0:
            if board[row][col] == 'Q':
                return False
            row+=1
            col-=1
        
        return True

    def solve(self, col, board, ans, n):
        if col == n:
            b =  board[:]
            print(b)
            ans.append(b)
            return
        
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col] = 'Q'
                self.solve(col+1, board, ans, n)
                board[row][col] = '.'

    def totalNQueens(self, n: int) -> int:
        ans = []
        board = [['.' for _ in range(n)] for _ in range(n)]
        # print(board)
        self.solve(0, board, ans, n)
        return len(ans)
        