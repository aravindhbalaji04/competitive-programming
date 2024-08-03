class Solution:
    def thirdMax(self, arr: List[int]) -> int:
        if len(list(set(arr))) < 3:
            return max(arr)
        else:
            for i in range(2):
                for i in range(arr.count(max(arr))):
                    arr.remove(max(arr))
            return max(arr)