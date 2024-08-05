class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        def helper(i,j,dp):

            if i > j:
                return 0
            if i == j:
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            if s[i] == s[j]:
                return 2 + helper(i+1,j-1,dp)
            one = helper(i+1,j,dp)
            two = helper(i,j-1,dp)

            dp[i][j] = max(one,two)

            return dp[i][j]
        n = len(s)
        dp = [[-1 for i in range(n)] for j in range(n)]
        return helper(0,n-1,dp)



        
        
        