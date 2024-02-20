class Solution:
    def __init__(self):
        self.mp = {}
    def solve(self, n, s, dictionary, temp):
        if len(temp) > len(s):
            return False
        if s == temp:
            return True
        if temp not in s:
            return False
        if self.mp.get(temp) == 1:
            return True
        for i in range(n):
            ret = self.solve(n, s, dictionary, temp + dictionary[i])
            if ret:
                self.mp[temp + dictionary[i]] = 1
                return True
        return False
    def wordBreak(self, n, s, dictionary):
        self.mp.clear()
        for i in range(n):
            temp = dictionary[i]
            if temp[0] == s[0]:
                ans = self.solve(n, s, dictionary, dictionary[i])
                if ans:
                    return ans
        return False

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	test_case = int(input())

	for _ in range(test_case):
		n = int(input())
		dictionary = [word for word in input().strip().split()]
		s = input().strip()
		ob = Solution()
		res = ob.wordBreak(n, s, dictionary)
		if res:
			print(1)
		else:
			print(0)
# } Driver Code Ends