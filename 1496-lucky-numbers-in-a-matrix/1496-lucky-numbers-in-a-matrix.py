class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        rows,cols = len(matrix),len(matrix[0])
        min_row, max_col = {},{}

        #getting the max element from every row
        for i in range(rows):
            rmin = float("inf")
            for j in range(cols):
                if matrix[i][j] < rmin:
                    rmin = min(matrix[i][j],rmin)
            min_row[rmin] = i

        #getting the max element from every column
        for j in range(cols):
            cmax = 0
            for i in range(rows):
                if matrix[i][j] > cmax:
                    cmax = max(matrix[i][j],cmax)
            max_col[cmax] = j

        ans = []
        #there can only be one max element
        for i in min_row:
            if i in max_col:
                ans.append(i)
        

        return ans

        

                
            




        