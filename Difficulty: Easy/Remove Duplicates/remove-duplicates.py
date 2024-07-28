#User function Template for python3
class Solution:
	def removeDups(self, str):
	    ans = ''
	    for i in range(len(s)):
	        if s[i] not in ans:
	            ans += s[i]
	    return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s = input()

        ob = Solution()
        answer = ob.removeDups(s)

        print(answer)

# } Driver Code Ends