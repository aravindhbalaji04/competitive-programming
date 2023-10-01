class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        x = []
        for i in range(len(accounts)):
            value = 0
            for j in range(len(accounts[i])):
                value += accounts[i][j]
                x.append(value)
        return max(x)