class Solution:
    def numberOfPath (self, n, k, arr):
        def f(i,j,s):
            if s > k:
                return 0
            if i==n-1 and j==n-1 and s+arr[i][j]==k:
                return 1
            if (i,j,s) in dp:
                return dp[(i,j,s)]
            left,right = 0,0
            if i+1 < n:
                left = f(i+1,j,s + arr[i][j])
            if j+1 < n:
                right = f(i,j+1,s + arr[i][j])
            dp[(i,j,s)] = left + right
            return dp[(i,j,s)]
        dp = {}
        return f(0,0,0)

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    ob = Solution()
    t = int (input ())
    for _ in range (t):
        k= int(input())
        n=int(input())
        l = list(map(int, input().split()))
        arr = list()
        c=0
        for i in range(0, n):
            temp = list()
            for j in range(0, n):
                temp.append(l[c])
                c += 1
            arr.append(temp)
        ans = ob.numberOfPath(n, k, arr);
        print(ans)


# } Driver Code Ends