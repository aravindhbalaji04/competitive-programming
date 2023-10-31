class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        n = len(nums)
        for i in range(n):
            answer.append(abs(sum(nums[0:i])-sum(nums[i+1:n])))
        return answer