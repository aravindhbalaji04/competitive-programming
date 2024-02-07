class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        if len(word1) == len(word2):
            for i in range(len(word1)):
                s += word1[i]
                s += word2[i]
        else:
            if len(word1) > len(word2):
                big = word1
                small = word2
            else:
                big = word2
                small = word1
            for i in range(len(small)):
                s += word1[i]
                s += word2[i]
            new = big[len(small):]
            for i in range(len(big)-len(small)):
                s += new[i]
        return s