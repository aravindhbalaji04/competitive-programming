class Solution:
    def search(self, pat, txt):
        k=len(pat)
        if len(pat)>len(txt):
            return []
        index=0
        ans=[]
        while index<=len(txt)-len(pat):
            if txt[index]==pat[0]:
                i=index
                j=k-1
                while txt[i]==pat[i-index] and txt[index+j]==pat[j]:
                    i+=1
                    j-=1
                    if i-index>j:
                        ans.append(index+1)
                        break
            index+=1
        return ans
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends