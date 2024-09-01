class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original):
            return []
        duplicate = []
        i = 0
        while i != len(original):
            temp = []
            for j in range(n):
                temp.append(original[i])
                i += 1
            duplicate.append(temp)
        return duplicate