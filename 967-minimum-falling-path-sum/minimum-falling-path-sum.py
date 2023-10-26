class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        #Tabulation solution
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            dp[0][j] = matrix[0][j]
        
        for i in range(1,m):
            for j in range(n):
                up = dp[i-1][j] 
                left = dp[i-1][j-1] if j > 0 else float('inf')
                right = dp[i-1][j+1] if j+1 < n else float('inf')
                dp[i][j] = matrix[i][j] + min(up, left, right)

        minVal = min(dp[m-1])
        
        return minVal

        


# class Solution:
#     def minFallingPathSum(self, matrix: List[List[int]]) -> int:
#         m = len(matrix)
#         n = len(matrix[0])

#         dp = [[-1 for i in range(n)] for j in range(m)]
#         maxVal = float("inf")

#         for j in range(n):

#             maxVal = min(maxVal,self.helper(m-1,j,matrix,dp))
        
#         return maxVal
    
#     def helper(self,i,j,matrix,dp):

#         if j < 0 or j >= len(matrix[0]):
#             return float("inf")

#         if i == 0:
#             return matrix[0][j]

#         if dp[i][j] != -1:
#             return dp[i][j]

#         up = matrix[i][j] + self.helper(i-1,j,matrix,dp)
#         left = matrix[i][j] + self.helper(i-1,j-1,matrix,dp)
#         right = matrix[i][j] + self.helper(i-1,j+1,matrix,dp)

#         max1 = min(left,right)
#         dp[i][j] =  min(up,max1)

#         return dp[i][j]