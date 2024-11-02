class Solution:
    def maxSum(self,arr):
        n = len(arr)
        arr.sort()
        total_sum= 0
        for i in range(n//2):
            total_sum-=2*arr[i]
            total_sum+=2*arr[n-i-1]
        return total_sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        ob = Solution()
        ans = ob.maxSum(arr)  # Call maxSum method and store result in ans
        print(ans)  # Print the result
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends