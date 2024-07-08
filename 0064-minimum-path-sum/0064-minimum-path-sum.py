class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for c in range(n):
            dp[0][c] = dp[0][c-1] + grid[0][c] if c else grid[0][c]
        for r in range(m):
            dp[r][0] = dp[r-1][0] + grid[r][0] if r else grid[r][0]

        for r in range(1,m):
            for c in range(1,n):
                dp[r][c] = min(dp[r-1][c],dp[r][c-1]) + grid[r][c]
        
        return dp[-1][-1]



        # n,m = len(grid),len(grid[0])

        # dp = [[0 for j in range(m)] for i in range(n)]
        

        # for i in range(n):
        #     for j in range(m):
        #         if i == 0 and j == 0:
        #             dp[i][j] = grid[i][j]
        #         else:
        #             up = grid[i][j]
        #             if i > 0:
        #                 up += dp[i-1][j]
        #             else:
        #                 up += float("inf")
        #             left = grid[i][j]
        #             if j > 0:
        #                 left += dp[i][j-1]
        #             else:
        #                 left += float("inf")
        #             dp[i][j] = min(up, left)
        
        # return dp[n-1][m-1]



# class Solution:
#     def minPathSum(self, grid: List[List[int]]) -> int:
#         m,n = len(grid), len(grid[0])

#         dp = [[-1 for i in range(n)] for j in range(m)]

#         return self.helper(m-1,n-1,grid,dp)
    

#     def helper(self,i,j,grid,dp):

#         if i == 0 and j == 0:
#             return grid[0][0]
        
#         if i < 0 or j < 0:
#             return float("inf")
        
#         if dp[i][j] != -1:
#             return dp[i][j]

#         up = grid[i][j] + self.helper(i-1,j,grid,dp)
#         left = grid[i][j] + self.helper(i,j-1,grid,dp)
        
#         dp[i][j] = min(up,left)

#         return dp[i][j]