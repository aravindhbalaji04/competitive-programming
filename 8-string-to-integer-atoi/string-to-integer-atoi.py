class Solution:
    def myAtoi(self, s):
        if not s or not s.strip():
            return 0
        is_negative = False
        s = s.strip()
        if s[0] == '+':
            s = s[1:]
        elif s[0] == '-':
            is_negative = True
            s = s[1:]
        s = s.lstrip('0')
        if not s or not s[0].isdigit():
            return 0
        for i in range(len(s)):
            if not s[i].isdigit():
                s = s[:i]
                break
        if s:
            result = int(s)
            if is_negative:
                result = -result
            if result < -2**31:
                return -2**31
            elif result > 2**31 - 1:
                return 2**31 - 1
            return result
        return 0