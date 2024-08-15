class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = ten = twen = 0
        for i in bills:
            if i == 5:
                five += 1
            elif i == 10 and five > 0:
                ten += 1
                five -= 1
            elif i == 20 and five > 0 and ten > 0:
                twen += 1
                five -= 1
                ten -= 1
            elif i == 20 and five > 2:
                twen += 1
                five -= 3
            else:
                return False
        return True