# from functools import lru_cache
# class Solution:
#     def longestCommonSubsequence(self, text1: str, text2: str) -> int:
#         @lru_cache(None)
#         def backtrack(i1, i2):
#             if i1==len(text1) or i2==len(text2):
#                 return 0
#             if text1[i1]==text2[i2]:
#                 return 1+backtrack(i1+1, i2+1)
#             else:
#                 return max(backtrack(i1, i2+1), backtrack(i1+1, i2))
                
#         return backtrack(0,0)

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def backtrack(i, j):
            if i==len(text1) or j==len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i,j)]
            if text1[i]==text2[j]:
                memo[(i,j)] = 1 + backtrack(i+1, j+1)
            else:
                memo[(i,j)] =  max(backtrack(i+1,j), backtrack(i,j+1))
            
            return memo[(i,j)]
        
        memo={}
        return backtrack(0,0)