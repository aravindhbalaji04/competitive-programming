class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        k = sum(nums)
        n = len(nums)
        numOnes = sum(nums[:k])
        numSwaps = k-numOnes
        for i in range(1, n):
            numOnes -= nums[i-1]
            numOnes += nums[(i-1+k)%n]
            numSwaps = min(numSwaps, k-numOnes)
        return numSwaps