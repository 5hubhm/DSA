# class Solution:
#     def minimumTotal(self, triangle: List[List[int]]) -> int:

#         def dp(row, col):
#             if row==len(triangle):
#                 return 0
#             if (row, col) in memo:
#                 return memo[(row, col)]
#             left = dp(row+1, col)
#             right = dp(row+1, col+1)

#             memo[(row, col)] = triangle[row][col] + min(left, right)
#             return memo[(row, col)]

#         if len(triangle)==1:
#             return triangle[0][0]
#         memo = {}
#         return dp(0, 0)

from functools import lru_cache
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(row, col):
            if row==len(triangle):
                return 0
            left = dp(row+1, col)
            right = dp(row+1, col+1)

            return triangle[row][col] + min(left, right)

        if len(triangle)==1:
            return triangle[0][0]
        return dp(0, 0)
        