class Solution:

    def isSafe(self, row, col, board, n):
        dupRow = row
        dupCol = col

        while row>=0 and col>=0:
            if board[row][col]=='Q':
                return False
            row-=1
            col-=1
        
        row = dupRow
        col = dupCol

        while col>=0:
            if board[row][col]=='Q':
                return False
            col-=1

        row = dupRow
        col = dupCol

        while row<n and col>=0:
            if board[row][col]=='Q':
                return False
            row+=1
            col-=1

        return True

    def solve(self, col, board, ans, n):
        if col == n:
            ans.append([''.join(row) for row in board])
            return 
        for row in range(n):
            if self.isSafe(row, col, board, n):
                board[row][col]='Q'
                self.solve(col+1, board, ans, n)
                board[row][col] = '.'

    def solveNQueens(self, n: int) -> List[List[str]]:
        ans = []
        board = [['.' for _ in range(n)] for i in range(n)]
        # print(board)
        self.solve(0, board, ans, n)
        return ans
        