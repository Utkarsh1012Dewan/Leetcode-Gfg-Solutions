class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        ans = [[0 for i in range(n)] for j in range(n)]
        left, right, top, bottom = 0, n-1, 0, n-1

        temp = 1

        while top <= bottom and left <= right:

            for col in range(left,right+1):
                ans[top][col] = temp
                temp +=1
            top +=1

            for row in range(top,bottom+1):
                ans[row][right] = temp
                temp +=1
            right -=1

            for col in range(right,left-1,-1):
                ans[bottom][col] = temp
                temp +=1
            bottom -=1

            for row in range(bottom,top-1,-1):
                ans[row][left] = temp
                temp +=1
            left +=1
        
        return  ans


        