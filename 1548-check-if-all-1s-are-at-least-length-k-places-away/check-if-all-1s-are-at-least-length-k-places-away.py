class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        cunt = k
        for i in nums:
            if i == 1:
                if cunt < k:
                    return False
                cunt = 0
            else:
                cunt += 1
        return True