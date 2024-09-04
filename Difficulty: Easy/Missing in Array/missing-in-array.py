class Solution:
    def missingNumber(self, n, arr):
        arr.sort()
        if arr[0] != 1:
            return 1
        for i in range(1, len(arr)):
            if i+1 != arr[i]:
                return i+1
        return len(arr)+1

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