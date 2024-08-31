class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        ans = 0
        for i in range(len(s.strip())-1, -1, -1):
            if s[i].isalpha():
                ans += 1
            else:
                break
        return ans