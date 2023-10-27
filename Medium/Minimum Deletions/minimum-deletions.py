#User function Template for python3

class Solution:
    def minimumNumberOfDeletions(self,S):
        s=S
        s1=S[::-1]
        dp=[[0 for i in range(len(s)+1)] for j in range(len(s)+1)]
        n=len(s)
        for i in range(1,n+1):
            for j in range(1,n+1):
                if(s[i-1]==s1[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        return n-dp[n][n]
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=input()

        ob = Solution()
        print(ob.minimumNumberOfDeletions(S))
# } Driver Code Ends