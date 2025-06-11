class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7

        # Sum for complete weeks
        total = 0
        for i in range(weeks):
            total += (7 * i) + 28  # 28 = 1+2+...+7

        # Sum for remaining days
        for i in range(days):
            total += weeks + i + 1  # money starts from weeks+1 on that Monday

        return total
