class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(idx, target, comb, n):
            if idx == n:
                if target == 0:
                    res.append(comb[:])
                return 
            if candidates[idx]<=target:
                comb.append(candidates[idx])
                backtrack(idx, target - candidates[idx], comb, n)
                comb.pop()
            backtrack(idx+1, target, comb, n)

        res = []
        comb = []
        n = len(candidates)
        backtrack(0, target, comb, n)
        return res