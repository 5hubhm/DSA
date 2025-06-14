# class Solution:
#     def uniquePaths(self, m: int, n: int) -> int:
#         def backtrack(row, col, res):
#             if row==m-1 and col == n-1:
#                 res.append(1)
#                 return
#             if row<m-1:
#                 backtrack(row+1, col, res)
#             if col<n-1:
#                 backtrack(row, col+1, res)

#         res =[]
#         backtrack(0, 0, res)
#         return sum(res)

from functools import lru_cache 
class Solution:
    def uniquePaths(self, m:int, n:int) -> int:
        
        @lru_cache(None)
        def dp(row,col):
            if row==m-1 and col==n-1:
                return 1
            
            if row>m-1 or col>n-1:
                return 0

            return dp(row+1, col) + dp(row, col+1)
        
        return dp(0,0)
