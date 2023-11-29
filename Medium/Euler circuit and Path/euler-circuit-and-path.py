class Solution:
    def isEulerCircuitExist(self, V, adj):
        even, odd = 0, 0
        for i in range(V):
            if len(adj[i]) % 2 == 0:
                even += 1
            else:
                odd += 1
        if V == even:
            return 2
        if odd == 2:
            return 1
        return 0

#{ 
 # Driver Code Starts


if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		V, E = map(int, input().strip().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isEulerCircuitExist(V, adj)
		print(ans)
# } Driver Code Ends