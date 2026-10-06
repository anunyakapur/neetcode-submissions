class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # if every consecutive value is = or < prev, return 0
        
        # running value to maximize the delta
        max_profit = 0
        for i in range(0, len(prices)-1):
            for j in range(i+1, len(prices)):
                # i and j are indices
                if prices[j]-prices[i] > max_profit:
                    max_profit = prices[j]-prices[i]

        return max_profit
        # i = 0..4, j = 1..5
        # O(n^2)