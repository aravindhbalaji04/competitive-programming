class Solution:
    def longestCommonSubstr(self, str1, str2):
        longest_length = 0  
        for i in range(len(str1)):
            for j in range(i + 1, len(str1) + 1):
                substring = str1[i:j]
                if substring in str2:
                    longest_length = max(longest_length, len(substring))
        return longest_length 

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends