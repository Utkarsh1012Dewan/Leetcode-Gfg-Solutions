class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        n = len(prices)

        def helper(i,buy):
            if i == n:
                return 0

            if dp[i][buy] != -1:
                return dp[i][buy]
            #0 - can buy stock
            #1 - can not buy only can sell stock
            #if buy == 0 then we can buy a stock
            #notBuy - do not buy the stock and go to the next day
            #buy -  buy the stock and go to next day. -prices[i] because we pay to buy stock
            if buy == 0:
                noTransaction = 0 + helper(i+1,0)
                transaction = -prices[i] + helper(i+1,1)
            elif buy == 1:
                noTransaction = 0 + helper(i+1,1)
                transaction = prices[i] + helper(i+1,0)
            
            dp[i][buy] = max(noTransaction,transaction)
            return dp[i][buy]
            
        dp = [[-1 for i in range(2)] for j in range(n)]
        return helper(0,0)
        