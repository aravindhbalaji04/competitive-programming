class Solution:
    def romanToInt(self, s: str) -> int:
        dick = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        value = i = 0
        while i < len(s):
            if i < len(s)-1 and dick[s[i]] < dick[s[i+1]]:
                value += dick[s[i+1]] - dick[s[i]]
                i += 2
            else:
                value += dick[s[i]]
                i += 1
        return value