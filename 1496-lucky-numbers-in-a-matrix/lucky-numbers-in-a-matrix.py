class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row, col = [], []
        new = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        for i in range(len(matrix)):
            row.append(min(matrix[i]))
        for i in range(len(new)):
            col.append(max(new[i]))
        for i in range(min(len(row), len(col))):
            if row[i] == col[i]:
                return [row[i]]
        if len(row) > len(col):
            for i in range(len(row)):
                if row[i] in col:
                    return [row[i]]
        else:
            for i in range(len(col)):
                if col[i] in row:
                    return [col[i]]
        return []