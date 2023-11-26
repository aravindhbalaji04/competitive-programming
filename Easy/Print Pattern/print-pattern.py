class Solution:
    def pattern(self, N):
        # code here
        x=[N]
        while N>0:
            N=N-5
            x.append(N)
        y=x[:len(x)-1]
        
        return x+y[::-1]


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        ans = ob.pattern(N)
        for i in ans:
            print(i, end = " ")
        print()
# } Driver Code Ends