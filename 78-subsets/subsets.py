class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, subset):
            if idx>n-1:
                res.append(subset[:])
                return
            
            subset.append(nums[idx])
            backtrack(idx+1, subset)
            subset.pop()
            backtrack(idx+1, subset)

        n = len(nums)
        subset = []
        res = []
        backtrack(0, subset)
        return res
        