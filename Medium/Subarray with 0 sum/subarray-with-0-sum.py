class Solution:
    def subArrayExists(self,arr,n):
        res=set()
        count=0
        if 0 in arr:
            return True
        else:
            for i in range(n):
                count+=arr[i]
                if count==0 or count in res:
                    return True
                res.add(count)
            return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3



def main():
    T=int(input())
    while(T>0):
        
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        if(Solution().subArrayExists(arr,n)):
            print("Yes")
        else:
            print("No")
        
        
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends