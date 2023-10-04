#User function Template for python3

class Solution:
    def romanToDecimal(self, S): 
        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        sum = 0
        n = len(S)
 
        i = 0
        while i < n :
            if (i != n - 1 and roman[S[i]] < roman[S[i + 1]]):
                sum += roman[S[i + 1]] - roman[S[i]]
                i += 2
                continue
            else:
                sum += roman[S[i]]
            i += 1
        return sum


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        ob = Solution()
        S = input()
        print(ob.romanToDecimal(S))
# } Driver Code Ends