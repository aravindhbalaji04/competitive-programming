class Solution:
    def minValue(self, s, k):
        d={}
        a=list(set(s))
        for i in a:
            v=s.count(i)
            d[i]=v
        v=list(d.values())
        for i in range(k):
            v.sort()
            v[-1]-=1
        sum=0
        for i in v:
            sum+=i**2
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        k = int(input())
        
        ob = Solution()
        print(ob.minValue(s, k))
# } Driver Code Ends