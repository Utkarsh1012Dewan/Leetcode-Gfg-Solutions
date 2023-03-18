class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS,COLS = len(matrix), len(matrix[0])
        l,r = 0, ROWS - 1
        
        while l <= r:
            mid = (l+r)//2
            
            if target > matrix[mid][-1]:
                l = mid + 1
            elif target < matrix[mid][0] :
                r = mid - 1
            else:
                break
        
        if not (l <= r):
            return False
        
        row = (l+r) // 2
        
        left,right = 0, COLS - 1
        
        while left <=right:
            mid = (left+right)//2
            
            if target > matrix[row][mid]:
                left = mid + 1
            elif target < matrix[row][mid]:
                right =  mid - 1
            else:
                return True
        return False
            
        
        