from collections import Counter
class Solution(object):
    def mostFrequentEven(self, nums):
        even = []
        for i in nums:
            if i % 2 == 0:
                even.append(i)
        if not even:
            return -1
        even = sorted(even)
        ec = Counter(even)
        for i in even:
            if ec[i] == max(ec.values()):
                return i