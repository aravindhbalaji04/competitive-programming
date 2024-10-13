class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = j = 0
        while j < len(t):
            if i == len(s):
                return True
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)