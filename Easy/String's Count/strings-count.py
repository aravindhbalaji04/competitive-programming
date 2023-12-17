class Solution:
    def countStr(self, length):
        strings_all_a = 1
        strings_at_most_1_b = length
        strings_at_most_1_c = length
        strings_one_b_one_c = length * (length - 1)
        strings_two_c = (length * (length - 1)) // 2
        strings_one_b_two_c = (length * (length - 1) * (length - 2)) // 2
        total_strings = strings_all_a + strings_at_most_1_b + strings_at_most_1_c + \
                        strings_one_b_one_c + strings_two_c + strings_one_b_two_c
        return total_strings

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        n = int(input())

        solObj = Solution()

        print(solObj.countStr(n))
# } Driver Code Ends