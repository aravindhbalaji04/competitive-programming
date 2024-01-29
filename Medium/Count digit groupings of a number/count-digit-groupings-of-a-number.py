class Solution:
    def TotalCount(self, s):
        def f(ind, val):
            if ind >= n:
                return 1
            if (ind,val) in dp:
                return dp[(ind,val)]
            cnt, curr = 0,0
            for i in range(ind, n):  
                curr += int(s[i])
                v = int(curr)
                if v >= val:
                    cnt += f(i + 1, v)
            dp[(ind,val)] = cnt
            return cnt
        n = len(s)
        dp = {}
        return f(0, 0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution()
		ans = ob.TotalCount(s)
		print(ans)
# } Driver Code Ends