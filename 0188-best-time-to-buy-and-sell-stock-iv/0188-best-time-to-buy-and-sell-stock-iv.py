class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:

        def helper(i,buy,k):

            if k == 0:
                return 0
            if i == n:
                return 0
            if dp[i][buy][k] != -1:
                return dp[i][buy][k]

            if buy == 0:
                noTran = 0 + helper(i+1,0,k)
                tran = -prices[i] + helper(i+1,1,k)
            elif buy == 1:
                noTran = 0 + helper(i+1,1,k)
                tran = prices[i] + helper(i+1,0,k-1)

            dp[i][buy][k] = max(noTran,tran)
            return dp[i][buy][k]
            
        n = len(prices)
        dp = [[[-1 for i in range(k+1)] for j in range(2)] for s in range(n)]
        return helper(0,0,k)
        