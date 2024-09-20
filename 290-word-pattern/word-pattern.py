class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(' ')
        if len(list(set(pattern))) != len(list(set(s))) or len(pattern) != len(s):
            return False
        freq = {}
        for i in range(len(pattern)):
            if pattern[i] not in freq:
                freq[pattern[i]] = s[i]
            else:
                if freq[pattern[i]] != s[i]:
                    return False
        return True