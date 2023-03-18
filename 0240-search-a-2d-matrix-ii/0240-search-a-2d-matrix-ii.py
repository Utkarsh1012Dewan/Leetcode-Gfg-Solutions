class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS,COLS = len(matrix),len(matrix[0])
        
        row,col = 0, COLS - 1
        
        while row < ROWS and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -=1
            elif matrix[row][col] < target:
                row +=1
            
        return False
        