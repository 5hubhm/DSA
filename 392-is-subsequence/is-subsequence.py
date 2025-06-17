class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # i = 0
        # for char in t:
        #     if i < len(s) and s[i] == char:
        #         i += 1
        # return i == len(s)
        def backtrack(i,j):
            if i == len(s):
                return True
            if j == len(t):
                return False
            if s[i]==t[j]:
                return backtrack(i+1, j+1)
            return backtrack(i, j+1)
            
        return backtrack(0,0)
