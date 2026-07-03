class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 0
        while right<len(prices):
            if left<len(prices) and right<len(prices) and prices[left]>prices[right]:
                left += 1
                right = left
            else:
                profit = max(profit,prices[right]-prices[left])
                right += 1
        return profit