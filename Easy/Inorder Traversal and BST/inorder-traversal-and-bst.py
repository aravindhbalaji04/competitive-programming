class Solution:
    def isRepresentingBST(self, arr, N):
        l=0
        if N<=1:
            return 1
        N-=1
        m=(l+N)//2
        if arr[m]==max(arr[:m+1]) and arr[m]==min(arr[m:]):
            return self.isRepresentingBST(arr[:m],m) and self.isRepresentingBST(arr[m+1:],N-m)
        else:
            return 0


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range (t):
        N = int(input())
        arr = input().split()
        for itr in range(N):
            arr[itr] = int(arr[itr])
        
        ob = Solution()
        print(ob.isRepresentingBST(arr, N))
# } Driver Code Ends