class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        m = len(text1)
        n = len(text2)

        dp = [[-1 for _ in range(n)] for _ in range(m)]

        return self.helper(m-1,n-1,text1,text2,dp)

    def helper(self,i,j,s,t,dp):

        if i < 0 or j < 0: return 0
        
        if dp[i][j] != -1: return dp[i][j]

        if s[i] == t[j]: return 1 + self.helper(i-1,j-1,s,t,dp)
        
        dp[i][j] =  max(self.helper(i-1,j,s,t,dp),self.helper(i,j-1,s,t,dp))

        return dp[i][j]


        