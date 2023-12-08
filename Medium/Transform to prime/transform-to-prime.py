class Solution:
    def minNumber(self, arr,n):
        x=sum(arr)
        def isprime(num):
            for i in range(2,int((num)**(0.5))+1):
                if num%i==0:
                    return False
            return True
        count=0  
        if isprime(x):
            return 0
        while not isprime(x):
            count+=1
            x+=1
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3


t=int(input())
for _ in range(0,t):
    n=int(input())
 #    l=list(map(int,input().split()))
 #    n=l[0]
 #    m=l[1]
    a=list(map(int,input().split()))
   # k = int(input())
  #  b = list(map(int, input().split()))
    ob = Solution()
    ans=ob.minNumber(a,n)
    print(ans)

# } Driver Code Ends