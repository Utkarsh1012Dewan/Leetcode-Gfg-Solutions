class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        
        maxRow = 0
        maxCount = 0
        
        for i in range(len(mat)):
            currCount = 0
            for j in range(len(mat[0])):
                if mat[i][j] == 1:
                    currCount +=1
                if currCount > maxCount:
                    maxRow = i
                maxCount = max(maxCount,currCount)
            
        
        return [maxRow,maxCount]
                