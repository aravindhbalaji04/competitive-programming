class Solution:
    def countSubarrays(self, a,n,L,R):
        def le(x):
            nonlocal a
            ret=0
            start=0
            for idx,val in enumerate(a):
                if val<=x:
                    ret+=idx-start+1
                else:
                    start=idx+1
            return ret
        return le(R)-le(L-1)

#{ 
 # Driver Code Starts
#Initial Template for Python 3



for _ in range(0,int(input())):
    n,l,r = map(int, input().strip().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    v = ob.countSubarrays(arr, n, l, r)
    print(v)
    
# } Driver Code Ends