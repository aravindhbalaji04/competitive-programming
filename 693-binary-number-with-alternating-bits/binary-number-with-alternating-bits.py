class Solution(object):
    def hasAlternatingBits(self, n):
        s = str(bin(n))
        for i in range(len(bin(n))-1):
            if s[i]==s[i+1]:
                return False
        return True
        