#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
class Solution:
    def betterString(self, str1, str2):
        def distinctsubsequence(s):
            n=len(s)
            dp=[0]*(n+1)
            dp[0]=1
            map={}
            for i in range(1,n+1):
                dp[i]=2*dp[i-1]
                ch=s[i-1]
                if ch in map:
                    j=map[ch]
                    dp[i]=dp[i]-dp[j-1]
                map[ch]=i
            return dp[n]
        if distinctsubsequence(str1)>=distinctsubsequence(str2):
            return str1
        else:
            return str2

#{ 
 # Driver Code Starts.
if __name__ == '__main__': 
    t = int(input ())
    for _ in range (t):
        str1 = input()
        str2 = input()
        ob = Solution()
        res = ob.betterString(str1, str2)
        print(res)
# } Driver Code Ends