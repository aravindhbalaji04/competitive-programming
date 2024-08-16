class Solution:
    def maximizeTheCuts(self,n,x,y,z):
        dp=[0]*(n+1)
        for i in range(min(x,y,z),n+1):
            if i>=x:
                if i==x:
                    dp[i]=max(dp[i],1)
                else:
                    dp[i]=max(dp[i],dp[i-x]+1 if dp[i-x] else 0 )
            if i>=y:
                if i==y:
                    dp[i]=max(dp[i],1)
                else:
                    dp[i]=max(dp[i],dp[i-y]+1 if dp[i-y] else 0)
            if i>=z:
                if i==z:
                    dp[i]=max(dp[i],1)
                else:
                    dp[i]=max(dp[i],dp[i-z]+1 if dp[i-z] else 0)
        return dp[n]

#{ 
 # Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    t=int(input())
    for tcs in range(t):
        n=int(input())
        x,y,z=[int(x) for x in input().split()]
        
        print(Solution().maximizeTheCuts(n,x,y,z))
# } Driver Code Ends