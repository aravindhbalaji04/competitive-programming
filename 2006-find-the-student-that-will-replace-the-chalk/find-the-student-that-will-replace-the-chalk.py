class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        i = 0
        k %= sum(chalk)
        while k > 0:
            k -= chalk[i]
            if len(chalk)-1 == i:
                i = 0
            else:
                i += 1
        if k < 0:
            if i-1 == -1:
                return len(chalk)-1
            return i-1
        return i