class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        ans = []
        for i in range(len(arr)):
            if arr.count(arr[i]) == 1:
                ans.append(arr[i])
                k -= 1
            if k == 0:
                return ans[-1]
        return ""