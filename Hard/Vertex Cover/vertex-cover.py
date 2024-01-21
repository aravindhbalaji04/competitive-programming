from typing import List
from itertools import combinations
class Solution:
    def vertexCover(self, n : int, edges : List[List[int]]) -> int:
        nodes = list(range(1, n+1))
        lo, hi = 0, n
        while lo < hi:
            mid = lo + (hi - lo)//2
            for perm in combinations(nodes, mid):
                perm = set(perm)
                if all(u in perm or v in perm for u, v in edges):
                    hi = mid
                    break
            else:
                lo = mid + 1
        return lo

#{ 
 # Driver Code Starts
class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        
        m = int(input())
        
        
        edges=IntMatrix().Input(m, m)
        
        obj = Solution()
        res = obj.vertexCover(n, edges)
        
        print(res)
        

# } Driver Code Ends