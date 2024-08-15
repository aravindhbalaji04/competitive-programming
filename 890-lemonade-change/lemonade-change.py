class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        money = [0,0,0]
        for i in bills:
            if i == 5:
                money[0] += 1
            elif i == 10 and money[0] > 0:
                money[1] += 1
                money[0] -= 1
            elif i == 20 and money[0] > 0 and money[1] > 0:
                money[2] += 1
                money[0] -= 1
                money[1] -= 1
            elif i == 20 and money[0] > 2:
                money[2] += 1
                money[0] -= 3
            else:
                return False
        return True