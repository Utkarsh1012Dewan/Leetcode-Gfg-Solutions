class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        
        m,n = len(grid),len(grid[0])
        count,r,c = 0,0,n-1
        
        while r < m and c >= 0:
            
            if grid[r][c] < 0:
                count += m - r
                c-=1
            else:
                r+=1
                
        return count
            
#                 [[4,3,2,-1]
#                  ,[3,2,1,-1]
#                  ,[1,1,-1,-2],
#                  [-1,-1,-2,-3]]
                
        