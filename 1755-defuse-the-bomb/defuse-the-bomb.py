class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        n = len(code)
        if k == 0:
            for i in range(n):
                ans.append(0)
        elif k > 0:
            for i in range(n):
                val, a, b = 0, 0, i+1
                while a < k:
                    if b == len(code):
                        b = 0
                    val += code[b]
                    a += 1
                    b += 1
                ans.append(val)
        else:
            k *= -1
            for i in range(n):
                val, a, b = 0, 0, i-1
                while a < k:
                    if b == -1:
                        b = len(code)-1
                    val += code[b]
                    a += 1
                    b -= 1
                ans.append(val)
        return ans