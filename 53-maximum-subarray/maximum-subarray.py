class Solution:        
    def maxSubArray(self, nums: list[int]) -> int:
        curr_sum = 0
        max_sum = float(-inf)
        n = len(nums)

        for i in range(n):
            curr_sum += nums[i]
            max_sum = max(max_sum, curr_sum)
            if curr_sum <0:
                curr_sum = 0
        return max_sum