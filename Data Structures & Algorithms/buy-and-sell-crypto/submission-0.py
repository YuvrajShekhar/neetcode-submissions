class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        for i, price in enumerate(prices):
            for j in range(i+1, len(prices)):
                diff = prices[j] - price
                output = max(diff, output)
        return output
