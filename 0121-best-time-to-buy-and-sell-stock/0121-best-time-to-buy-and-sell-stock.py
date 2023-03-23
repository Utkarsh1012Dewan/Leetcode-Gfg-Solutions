class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minEle = prices[0]
        profit = 0
        
        for i in prices:
            if i < minEle:
                minEle = i
            else:
                profit = max(profit, i - minEle)
        
        return profit
        