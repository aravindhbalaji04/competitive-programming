class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row, col = [], []
        for i in range(len(matrix[0])):
            temp = []
            for j in range(len(matrix)):
                row.append(min(matrix[j]))
                temp.append(matrix[j][i])
            col.append(max(temp))
        if len(row) > len(col):
            for i in range(len(row)):
                if row[i] in col:
                    return [row[i]]
        else:
            for i in range(len(col)):
                if col[i] in row:
                    return [col[i]]
        return []