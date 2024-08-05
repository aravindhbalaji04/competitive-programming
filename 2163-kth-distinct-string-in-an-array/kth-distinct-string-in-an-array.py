class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                if k == 1:
                    return arr[i]
                k -= 1
        return ''