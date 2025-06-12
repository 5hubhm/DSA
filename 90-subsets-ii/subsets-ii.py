class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, subset):
            if idx==n:
                res.append(subset[:])
                return
            
            subset.append(nums[idx])
            backtrack(idx+1, subset)
            subset.pop()
            while idx+1<n and nums[idx]==nums[idx+1]:
                idx += 1
            backtrack(idx+1, subset)

        res = []
        subset = []
        n = len(nums)
        nums.sort()
        backtrack(0, subset)
        return res