class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        dp = [-1]*(n)

        ans1 = self.helper(n-1,cost,dp,n)

        dp=[-1]*(n)

        ans2 = self.helper(n-2,cost,dp,n)

        return min(ans1,ans2)


    def helper(self,index,cost,dp,n):

        if index < 0:
            return 0
        
        if n <= 1:
            return cost[n]
        
        if dp[index] != -1:
            return dp[index]

        left = self.helper(index-1,cost,dp,n) + cost[index]

        right = self.helper(index-2,cost,dp,n) + cost[index]

        dp[index] = min(left,right)

        return dp[index]

        