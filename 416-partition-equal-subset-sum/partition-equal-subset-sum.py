# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         memo = {}  # key = (idx, target), value = True/False

#         def dp(idx, target):
#             if target == 0:
#                 return True
#             if idx == len(nums) or target < 0:
#                 return False

#             if (idx, target) in memo:
#                 return memo[(idx, target)]

#             # Try including or excluding the current number
#             choose = dp(idx + 1, target - nums[idx])
#             not_choose = dp(idx + 1, target)

#             memo[(idx, target)] = choose or not_choose
#             return memo[(idx, target)]

#         s = sum(nums)
#         if s % 2 != 0:
#             return False

#         target = s // 2
#         return dp(0, target)
from typing import List
from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)
        if s % 2 != 0:
            return False  # Cannot split into two equal subsets if the sum is odd

        target = s // 2

        @lru_cache(maxsize=None)
        def dp(idx, target):
            if target == 0:
                return True
            if idx == len(nums) or target < 0:
                return False

            # Choose or skip the current number
            return dp(idx + 1, target - nums[idx]) or dp(idx + 1, target)

        return dp(0, target)
