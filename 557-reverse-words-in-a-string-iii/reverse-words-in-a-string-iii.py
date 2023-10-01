class Solution:
    def reverseWords(self, s: str) -> str:
        x = ""
        c = list(map(str, s.split()))
        for _ in range(len(c)):
            x = x + " " + c[_][::-1] 
        return x[1::]