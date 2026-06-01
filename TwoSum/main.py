from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        profit = 0
        for cost in prices:
            if cost < buy:
                buy = cost
            if profit < cost - buy:
                profit = cost - buy
        return profit
prices = [7,1,5,3,6,4]
sol = Solution()
print(sol.maxProfit(prices))
