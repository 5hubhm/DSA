class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        n = 0
        for num in nums:
            n += 1
        max = abs(nums[n-1]-nums[0])

        for i in range(n-1):
            diff = abs(nums[i]-nums[i+1])
            max = diff if diff>max else max

        return max
        