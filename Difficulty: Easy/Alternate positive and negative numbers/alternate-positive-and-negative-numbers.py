class Solution:
    def rearrange(self,arr):
        n = len(arr)
        pos, neg = [], []
        for i in arr: 
            if i >= 0: 
                pos.append(i)
            else: 
                neg.append(i)
        i = j = k = 0
        while i < len(pos) and j < len(neg):
            if k % 2 == 0: 
                arr[k] = pos[i]
                i += 1
            else:
                arr[k] = neg[j]
                j += 1
            k += 1
        while i < len(pos):
            arr[k] = pos[i]
            k, i = k+1, i+1
        while j < len(neg):
            arr[k] = neg[j]
            k, j = k+1, j+1
        return arr

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ob.rearrange(arr)
        for x in arr:
            print(x, end=" ")
        print()
        tc -= 1

# } Driver Code Ends