class Solution:
    def recamanSequence(self, n):
        prev=0
        i=1
        ans=[0]
        dp={}
        while i<n:
            if prev-i>0 and prev-i not in dp:
                prev-=i
            else:
                prev+=i
            dp[prev]=1
            ans.append(prev)
            i+=1
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.recamanSequence(n)
        for i in range(n):
            print(ans[i],end=" ")
        print()
# } Driver Code Ends