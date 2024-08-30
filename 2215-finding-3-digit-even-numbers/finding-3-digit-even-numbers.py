class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        ans = []
        for i in range(len(digits)):
            if digits[i] == 0:
                continue
            else:
                for j in range(len(digits)):
                    for k in range(len(digits)):
                        if digits[k] % 2 == 1 or i == j or j == k or i == k:
                            continue
                        else:
                            ans.append(int(str(digits[i])+str(digits[j])+str(digits[k])))
        return sorted(list(set(ans)))