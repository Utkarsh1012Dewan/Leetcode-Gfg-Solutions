class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        m,n = len(grid), len(grid[0])

        rowOnes = [0]*m
        colOnes = [0]*n

        for i in range(m):
            for j in range(n):
                rowOnes[i] += grid[i][j]
                colOnes[j] += grid[i][j]
        
        for i in range(m):
            for j in range(n):
                grid[i][j] = 2*(rowOnes[i]+colOnes[j]) - m - n
        
        return grid

         


        