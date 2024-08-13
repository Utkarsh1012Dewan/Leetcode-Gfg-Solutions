class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        def helper(i,buy,cap):
            if cap == 0 or i == n:
                return 0
            #if we can buy
            if dp[i][buy][cap] != -1:
                return dp[i][buy][cap]

            if buy == 0:
                noTransaction = 0 + helper(i+1,0,cap)
                transaction = -prices[i] + helper(i+1,1,cap)
            elif buy == 1:
                noTransaction = 0 + helper(i+1,1,cap)
                transaction = prices[i] + helper(i+1,0,cap-1)

            dp[i][buy][cap] = max(transaction,noTransaction)
            return dp[i][buy][cap]

        n = len(prices)
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n)]
        return helper(0,0,2)
        