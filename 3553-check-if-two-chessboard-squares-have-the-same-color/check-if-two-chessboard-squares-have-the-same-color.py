class Solution:
    def checkTwoChessboards(self, coordinate1: str, coordinate2: str) -> bool:
        val = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8}
        if val[coordinate1[0]]%2 == int(coordinate1[1])%2:
            c1 = 1
        else:
            c1 = 0
        if val[coordinate2[0]]%2 == int(coordinate2[1])%2:
            c2 = 1
        else:
            c2 = 0
        return c1 == c2