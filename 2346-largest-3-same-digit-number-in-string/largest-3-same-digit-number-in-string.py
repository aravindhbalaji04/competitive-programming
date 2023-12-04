class Solution:
    def largestGoodInteger(self, num: str) -> str:
        arr = []
        for i in range(2,len(num)):
            if num[i-2] == num[i-1] == num[i]:
                arr.append(int(num[i]*3))
        if len(arr) > 0:
            if max(arr) == 0:
                return "000"
            else:
                return str(max(arr))
        else:
            return ""