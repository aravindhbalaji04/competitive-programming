class Solution:
    def winner(self,arr,n):
        mp = {}
        for i in arr: mp[i] = 0
        for i in arr: mp[i] += 1
        l = [(mp[i], i) for i in mp]
        l = sorted(l, reverse = True)
        curr = l[0][0]
        ans = l[0][1]
        for i in range(len(l)):
            if curr == l[i][0]: ans = l[i][1]
        return [ans, curr]  
        
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        
        n=int(input())
        arr=input().strip().split()
        
        result = Solution().winner(arr,n)
        print(result[0],result[1])
# } Driver Code Ends