class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(temp, used):
            if len(temp)==len(nums):
                res.append(temp[:])
                return
            
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i] = 1
                temp.append(nums[i])
                backtrack(temp, used)
                e = temp.pop()
                used[i] = 0

        temp = []
        used = [0] * len(nums)
        backtrack(temp, used)
        return res
