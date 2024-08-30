class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        dick = {}
        left = length = 0
        for i in range(len(s)):
            if s[i] in dick:
                left = max(left, dick[s[i]]+1)
            dick[s[i]] = i
            length = max(i-left, length)
        return length+1