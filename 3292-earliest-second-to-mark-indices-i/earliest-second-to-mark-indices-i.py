class Solution(object):
    def earliestSecondToMarkIndices(self, nums, changeIndices):
        n = len(nums)
        m = len(changeIndices)
        def check(s):
            marked = [0]*n
            for j in reversed(range(s)):
                i = changeIndices[j] - 1
                s = min(s, j+1)
                if not marked[i]:
                    s -= (nums[i] + 1)
                    if s < 0:
                        return False
                    marked[i] = 1
            return all(marked)
        l = 0
        r = m
        while l < r:
            s = (l + r) // 2
            if check(s):
                r = s
            else:
                l = s + 1
        return r if check(r) else -1