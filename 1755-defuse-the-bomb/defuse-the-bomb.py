class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        ans = []
        n = len(code)
        extended = code*2
        if k == 0:
            return [0]*n
        elif k > 0:
            for i in range(n):
                ans.append(sum(extended[i+1:i+k+1]))
        else:
            for i in range(n):
                print(extended[i-1:i-k])
                ans.append(sum(extended[i+n+k:i+n]))
        return ans