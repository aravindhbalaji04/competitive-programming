class Solution:
    def minOperation(self, n):
        operation_count = 0
      
        while n > 0:
            if n % 2:
                n -= 1
            else:
                n //= 2
           
            operation_count += 1
       
        return operation_count
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        ob = Solution()
        print(ob.minOperation(n))
# } Driver Code Ends