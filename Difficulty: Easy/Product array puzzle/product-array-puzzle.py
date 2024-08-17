class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        left = [1] * n
        right = [1] * n
        product = [1] * n
        for i in range(1, n):
            left[i] = nums[i-1] * left[i-1]
        for i in range(n-2, -1, -1):
            right[i] = nums[i+1] * right[i+1]
        for i in range(n):
            product[i] = left[i] * right[i]
        return product

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends