class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:

        def helper(i,buy):
            if i == n:
                return 0
            if dp[i][buy] != -1:
                return dp[i][buy]

            if buy == 0:
                noTrans = 0 + helper(i+1,0)
                trans = -prices[i] + helper(i+1,1)
            elif buy == 1:
                noTrans = 0 + helper(i+1,1)
                trans = prices[i] - fee + helper(i+1,0)

            dp[i][buy] = max(noTrans,trans)
            return dp[i][buy]

        n = len(prices)
        dp = [[-1 for i in range(2)] for j in range(n)]
        return helper(0,0)



        