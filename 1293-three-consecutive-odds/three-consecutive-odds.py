class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        elif len(arr) == 3:
            return arr[0] % 2 == arr[1] % 2 == arr[2] % 2 == 1
        else:
            try:
                for i in range(len(arr)):
                    if arr[i] % 2 == 1:
                        if arr[i+1] % 2 == 1:
                            if arr[i+2] % 2 == 1:
                                return True
                return False
            except:
                return False