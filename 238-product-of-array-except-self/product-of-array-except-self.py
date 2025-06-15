from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)

        # Step 1: Compute prefix products
        prefix = [1] * n
        product = 1
        for i in range(n):
            product *= nums[i]
            prefix[i] = product
        print("Prefix:", prefix)

        # Step 2: Compute postfix products
        postfix = [1] * n
        product = 1
        for i in range(n - 1, -1, -1):
            product *= nums[i]
            postfix[i] = product
        print("Postfix:", postfix)

        # Step 3: Build result
        result = [1] * n
        for i in range(n):
            left = prefix[i - 1] if i > 0 else 1
            right = postfix[i + 1] if i < n - 1 else 1
            result[i] = left * right

        return result
