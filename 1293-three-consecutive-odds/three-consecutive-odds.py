class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        try:
            for i in range(len(arr)):
                if arr[i] % 2 == 1 and arr[i+1] % 2 == 1 and arr[i+2] % 2 == 1:
                    return True
            return False
        except:
            return False