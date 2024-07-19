class Solution:
    def minOperations(self, n: int) -> int:
        arr = []
        total = 0
        for i in range(n):
            arr.append((2*i)+1)
        for i in range(n):
            total += abs(arr[i]-arr[n//2])
        return total//2