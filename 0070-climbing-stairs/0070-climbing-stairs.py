class Solution:
    def helper(self,n,dp):

        if n <= 1:
            return 1
    
        if n in dp:
            return dp[n]
        one = self.helper(n-1,dp)
        two = self.helper(n-2,dp)

        dp[n] = one+two

        return dp[n]

    
    
    def climbStairs(self, n: int) -> int:
        dp = {}
        return self.helper(n,dp)

    


