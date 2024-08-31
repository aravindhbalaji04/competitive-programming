class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r, c = [1]*len(matrix), [1]*len(matrix[0])
        for i in range(len(matrix)):
            if 0 in matrix[i]:
                for j in range(len(matrix[i])):
                    if matrix[i][j] == 0:
                        r[i], c[j] = 0, 0
        for i in range(len(r)):
            if r[i] == 0:
                for j in range(len(matrix[i])):
                    matrix[i][j] = 0
        for i in range(len(c)):
            if c[i] == 0:
                for j in range(len(matrix)):
                    matrix[j][i] = 0
        return [[]]