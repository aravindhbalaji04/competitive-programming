class Solution:
    def AllPossibleStrings(self, s):
        subseq = []
        n = len(s)
        for i in range(1, 2**n):
            x = ""
            for j in range(n):
                if (i >> j) & 1:
                    x += s[j]
            subseq.append(x)
        return sorted(subseq)

#{ 
 # Driver Code Starts

#Initial Template for Python 3

if __name__ == '__main__':
	T=int(input())
	for i in range(T):
		s = input()
		ob = Solution();
		ans = ob.AllPossibleStrings(s)
		for i in ans:
			print(i, end = " ");
		print()
# } Driver Code Ends