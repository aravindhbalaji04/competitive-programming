from collections import Counter
class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        d = Counter(arr)
        a = 0
        for i, j in d.items():
            if j == 1:
                a += 1
                if a == k:
                    return i
        return ""