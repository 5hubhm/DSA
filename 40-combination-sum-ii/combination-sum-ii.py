class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(idx, comb, target):
            if target == 0:
                res.append(comb[:])
                return
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue  # skip duplicates
                if candidates[i] > target:
                    break
                comb.append(candidates[i])
                backtrack(i + 1, comb, target - candidates[i])  # use i + 1 instead of idx + 1
                comb.pop()

        candidates.sort()
        res = []
        backtrack(0, [], target)
        return res
