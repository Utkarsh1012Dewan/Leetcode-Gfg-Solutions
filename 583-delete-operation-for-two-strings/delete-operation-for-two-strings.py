class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        def helper(i,j):

            if i < 0 or j < 0:
                return 0
            if dp[i][j] != -1:
                return dp[i][j]
            if word1[i] == word2[j]:
                return 1 + helper(i-1,j-1)

            one = helper(i-1,j)
            two = helper(i,j-1)

            dp[i][j] = max(one,two)
            return dp[i][j]
            
        n,m = len(word1),len(word2)
        dp = [[-1 for j in range(m)] for i in range(n)]
        ans = helper(n-1,m-1)

        return n+m - (2*ans)
        



        
        