class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, subset):
            if idx>n-1:
                if subset not in res:
                    res.append(subset[:])
                return
            
            subset.append(nums[idx])
            backtrack(idx+1, subset)
            subset.pop()
            backtrack(idx+1, subset)

        res = []
        subset = []
        n = len(nums)
        nums.sort()
        backtrack(0, subset)
        return res