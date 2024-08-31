class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = strs[0]
        for i in range(1, len(strs)):
            temp = ''
            for j in range(min(len(s), len(strs[i]))):
                if s[j] == strs[i][j]:
                    temp += s[j]
                else:
                    break
            s = temp
        return s