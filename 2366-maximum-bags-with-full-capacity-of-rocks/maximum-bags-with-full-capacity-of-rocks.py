class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        ans = []
        for i in range(len(capacity)):
            ans.append(capacity[i]-rocks[i])
        ans.sort()
        count = 0
        for i in range(len(ans)):
            additionalRocks -= ans[i]
            count += 1
            if additionalRocks <= 0:
                if additionalRocks == 0:
                    return count
                return count-1
        return len(ans)