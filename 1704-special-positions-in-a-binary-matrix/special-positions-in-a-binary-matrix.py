class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        rows = [0]*len(mat)
        cols = [0]*len(mat[0])
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j]:
                    rows[i] += 1
                    cols[j] += 1
        res = 0
        for i in range(len(rows)):
            for j in range(len(cols)):
                if mat[i][j] and rows[i] == 1 and cols[j] == 1:
                    res += 1
        return res
        