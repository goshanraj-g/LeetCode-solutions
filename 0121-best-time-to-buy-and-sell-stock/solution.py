class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        while (r < len(prices)):
            if prices[r] >= prices[l]:
                profit = max(prices[r]-prices[l], profit)
                r += 1
            else:
                l += 1
                
        return profit
        
