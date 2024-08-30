class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = {}
        left = length = 0
        for i in range(len(s)):
            if s[i] in dic:
                left = max(left, dic[s[i]]+1)
            dic[s[i]] = i
            length = max(i-left+1, length)
        return length