class Solution:
    def maxSum(self, n):  
        def Split(n):
            if n>=(n//2+n//3+n//4):
                return n
            return Split(n//2)+Split(n//3)+Split(n//4)
        return Split(n)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.maxSum(n))
# } Driver Code Ends