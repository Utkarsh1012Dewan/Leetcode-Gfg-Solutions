class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        def helper(i,j):

            if i < 0:
                return j+1 
            if j < 0:
                return i+1
            if dp[i][j] != -1:
                return dp[i][j]
            #if words match then no operation is needed
            if word1[i] == word2[j]:
                dp[i][j] = helper(i-1,j-1)
            else:
                #mininmum of replace, insert and delete operations
                dp[i][j] = 1 + min(helper(i-1,j-1),helper(i-1,j),helper(i,j-1))
            return dp[i][j]

        n,m = len(word1),len(word2)
        dp = [[-1 for j in range(m)] for i in range(n)]

        ans = helper(n-1,m-1)

        return ans