class Solution:
    def missingNumber(self, n, arr):
        sum1 = sum(arr)
        sum2 = 0
        for i in range(1, n+1):
            sum2 += i
        return sum2 - sum1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends