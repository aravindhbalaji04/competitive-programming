class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ans = list(s)
        for i in range(len(t)):
            if t[i] in ans:
                ans.remove(t[i])
            else:
                return False
        if len(ans) == 0:
            return True
        return False