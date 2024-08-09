class Solution:
    def Maximize(self, arr):
        sum=0
        arr.sort()    
        c=0
        for a1 in arr:
            sum=sum+(c*a1) 
            c=c+1               
        sum=sum%1000000007
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        A = list(map(int, input().strip().split()))
        # k = int(input())
        ob = Solution()
        print(ob.Maximize(A))

# } Driver Code Ends