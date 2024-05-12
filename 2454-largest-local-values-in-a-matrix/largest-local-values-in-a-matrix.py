class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        row, col = len(grid), len(grid[0])
        tRow, tCol = row-2, col-2

        maxLocal = [[0 for j in range(tCol)] for i in range(tRow)]

        for r in range(0, tRow):
            for c in range(0, tCol):
                maxVal = 0

                for i in range(r, r+3):
                    for j in range(c, c+3):
                        if grid[i][j] > maxVal:
                            maxVal = max(maxVal, grid[i][j])

                maxLocal[r][c] = maxVal

        return maxLocal




        