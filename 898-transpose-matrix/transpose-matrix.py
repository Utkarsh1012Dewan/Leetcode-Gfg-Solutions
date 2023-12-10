class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        row,col = len(matrix),len(matrix[0])

        new = [[0 for i in range(row)] for j in range(col)]

        for i in range(row):
            for j in range(col):
                new[j][i] = matrix[i][j]
        

        return new
        