class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = []
        per = []

        def backtrack():
            if len(per) == n:
                ans.append(per[:])

            
            for num in nums:
                if num not in per:
                    per.append(num)
                    backtrack()
                    per.pop()

        backtrack()
        return ans

