class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, total):
            if len(path) == k:
                if total == n:
                    res.append(path[:])
                return
            
            for i in range(start, 10):
                if total + i > n:
                    break
                path.append(i)
                backtrack(i + 1, path, total + i)
                path.pop()
        
        res = []
        backtrack(1, [], 0)
        return res
