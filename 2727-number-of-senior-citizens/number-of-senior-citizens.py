class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in range(len(details)):
            temp = int(details[i][11:13])
            if temp > 60:
                count += 1
        return count