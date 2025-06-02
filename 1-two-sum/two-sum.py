class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Two sum
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if nums[j] == target-nums[i]:
                    return [i,j]

        