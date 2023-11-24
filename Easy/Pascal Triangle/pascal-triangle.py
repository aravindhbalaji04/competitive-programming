
class Solution:

	def nthRowOfPascalTriangle(self,n):
	    
	    if n==1:
	        return [1]
	        
	    if n==2:
	        return [1,1]
	    
	    mod=10**9+7
	    res=[1]+[0]*(n-2)+[1]
	    last_row=self.nthRowOfPascalTriangle(n-1)
	    
	    for i in range(1,n-1):
	        res[i]=(last_row[i-1]+last_row[i])%mod
	    
	    return res

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

	tc=int(input())
	while tc > 0:
	    n=int(input())
	    ob = Solution()
	    ans=ob.nthRowOfPascalTriangle(n)
	    for x in ans:
	        print(x, end=" ")
	    print()
	    tc=tc-1
# } Driver Code Ends