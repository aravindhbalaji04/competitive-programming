class Solution:
    def sequence(self, n):
        x = 1
        ans = 0
        MOD = 10**9+7
        for i in range(1,n+1):
            y = i 
            temp = 1
            while y:
                temp = ((temp%MOD)*(x%MOD))%MOD
                x += 1
                y -= 1
            ans = (ans%MOD + temp%MOD)%MOD
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        N = int(input())
        
        ob = Solution()
        print(ob.sequence(N))
# } Driver Code Ends