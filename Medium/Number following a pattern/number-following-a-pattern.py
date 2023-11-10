class Solution:
    def printMinNumberForPattern(self, pattern):
        result = []
        stack = []
        num = 1
        for char in pattern:
            stack.append(str(num))
            num += 1
            if char == "I":
                result += stack[::-1]
                stack = []
        stack.append(str(num))
        result += stack[::-1]
        return int(''.join(result))
#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        
        S=str(input())

        ob = Solution()
        print(ob.printMinNumberForPattern(S))
# } Driver Code Ends