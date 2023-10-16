class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        x = [1]
        y = 1
        for i in range(1, rowIndex+1):
            z = y*(rowIndex-i+1)//i
            x.append(z)
            y = z
        return x